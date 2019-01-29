"""
Various functions for plotting and computing the DEM
"""
import numpy as np
import astropy.units as u


def calculate_em(t, T, n, L, bins_T=None):
    # Create bins
    if bins_T is None:
        bins_T = 10**(np.arange(4,8.5,0.05))*u.K
    bins_t = np.concatenate((t[:1], (t[1:] + t[:-1])/2., t[-1:])).value*t.unit
    # Make 2D histogram
    H,_,_ = np.histogram2d(
        T.value, t.value,
        bins=(bins_T.value, bins_t.value),
        weights=np.gradient(t)/np.gradient(t).sum()*L*n.value**2
    )
    return bins_T, H.sum(axis=1)*u.cm**(-5)


def fit_slope(bins_T, EM, T0=1e6*u.K, T1=None):
    T = (bins_T[1:] + bins_T[:-1])/2
    if T1 is None:
        T1 = T[np.argmax(EM)]
    i_fit = np.where(np.logical_and(T >= T0, T <= T1))
    T_fit = np.log10(T[i_fit].value)
    EM_fit = np.log10(EM[i_fit].value)
    a, b = np.polyfit(T_fit, EM_fit, 1)
    return a, 10**b, 10**T_fit


def plot_hist(ax, vals, bins, **kwargs):
    """
    Plot a histogram from bin values
    
    Parameters
    ----------
    ax : Matplotlib axis
    vals : value in each bin
    bins : Bin edges, including the rightmost edge
    kwargs : Plotting keyword arguments
    """
    ymin = ax.get_ylim()[0]
    ax.step(bins[:-1], vals, where='post', **kwargs)
    ax.step(bins[-2:],[vals[-1],vals[-1]], where='pre', **kwargs)
    ax.vlines(bins[0], ymin, vals[0], **kwargs)
    ax.vlines(bins[-1], ymin, vals[-1], **kwargs)
