# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 11:37:39 2014

@author: sm1fg

Generate a 1D non-magnetic atmosphere vector based on an empirical model
based on observational data, or specify an analytical hydrostatic
equilibrium atmosphere.

This code adapted directly from the SWAT-Sheffield pysac code
https://github.com/SWAT-Sheffield/pysac/blob/master/pysac/mhs_atmosphere/hs_model/hs_atmosphere.py
"""
import numpy as np
from scipy.interpolate import UnivariateSpline
import astropy.table
from astropy.table import Table
import astropy.units as u
from astropy.constants import k_B, m_p

__all__ = ['read_VAL3c_MTW', 'interpolate_atmosphere']


def read_VAL3c_MTW(VAL_file, MTW_file=None, mu=0.602):
    """
    Read in the data from Table 12 in Vernazza (1981) and combine with
    McWhirter (1975).

    Parameters
    ----------
    VAL_file : string
        The data file for the VAL3c atmosphere

    MTW_file : string
        The data file for the McWhirter atmosphere. if None,
        only the VAL atmosphere is returned.

    mu : float
        The mean molecular weight ratio for the corona. defaults to 0.6.

    Returns
    -------
    data : `astropy.table.Table`
        The combined data, sorted by Z.
    """
    VAL3c = Table.read(VAL_file, format='ascii', comment='#')
    VAL3c['Z'].unit = u.km
    VAL3c['rho'].unit = u.Unit('g cm-3')
    VAL3c['p'].unit = u.Unit('dyne/cm^2')
    VAL3c['T'].unit = u.K
    VAL3c['n_i'].unit = u.one/u.cm**3
    VAL3c['n_e'].unit = u.one/u.cm**3
    # Calculate the mean molecular weight ratio
    VAL3c['mu'] = 4.0/(3*0.74+1+VAL3c['n_e']/VAL3c['n_i'])
    # VAL3c['mu'] = 4.0/(3*0.74+1+VAL3c['n_e'].quantity/VAL3c['n_i'].quantity)

    if MTW_file:
        MTW = Table.read(MTW_file, format='ascii', comment='#')
        MTW['Z'].unit = u.km
        MTW['T'].unit = u.K
        MTW['p'].unit = u.Unit('dyne cm-2')
        MTW['rho'] = (MTW['p'] / k_B / MTW['T'] * m_p * mu).to('g cm-3')
        MTW['mu'] = mu
        data = astropy.table.vstack([VAL3c, MTW], join_type='inner')
    else:
        data = VAL3c

    data.sort('Z')

    return data


def interpolate_atmosphere(data, Z, s=0.25):
    """ This module generates a 1d array for the model plasma preesure, plasma
    density, temperature and mean molecular weight.
    """
    hdata = np.array(u.Quantity(data['Z']).to(u.m))
    # interpolate total pressure, temperature and density profiles
    pdata_f = UnivariateSpline(hdata, np.array(np.log(data['p'])),k=1, s=s)
    Tdata_f = UnivariateSpline(hdata, np.array(np.log(data['T'])),k=1, s=s)
    rdata_f = UnivariateSpline(hdata, np.array(np.log(data['rho'])),k=1, s=s)
    #s=0.0 to ensure all points are strictly used for ionisation state
    muofT_f = UnivariateSpline(hdata, np.array(np.log(data['mu'])),k=1, s=0.0)

    outdata = Table()
    outdata['Z'] = Z
    outdata['p'] = np.exp(pdata_f(Z.to(u.m))) * data['p'].unit
    outdata['T'] = np.exp(Tdata_f(Z.to(u.m))) * data['T'].unit
    outdata['rho'] = np.exp(rdata_f(Z.to(u.m))) * data['rho'].unit
    outdata['mu'] = np.exp(muofT_f(Z.to(u.m))) * u.one

    return outdata
