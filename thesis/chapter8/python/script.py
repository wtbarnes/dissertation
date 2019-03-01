"""
Helper functions for plotting some future work results
"""
import astropy.units as u
from hydrad_tools.configure import Configure
import numpy as np


def spatial_heating_profile(s, config_filename):
    """
    Compute heating profile from HYDRAD config parameters
    """
    conf = Configure.load_config(config_filename)
    h = u.Quantity(np.zeros(s.shape), 'erg / (cm^3*s)')
    for e in conf['heating']['events']:
        h += e['rate'] * np.exp(-((s - e['location'])**2)/(2*((e['scale_height'])**2)))
    return h
