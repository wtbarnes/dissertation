"""
Quick implementation of the Raymond-Klimchuk power-law radiative loss function.
See Eq. 3 of Klimchuk et al. (2008)
"""
import numpy as np
import astropy.units as u


@u.quantity_input
def power_law_rad_loss(T: u.K, kind='klimchuk') -> u.erg * u.cm**3 / u.s:
    """
    Raymond-Klimchuk power-law radiative loss function. See Eq. 3 of Klimchuk et al. (2008)
    
    Arguments:
        T {u.K} -- [description]
    
    Returns:
        [type] -- [description]
    """
    log_temperature = np.log10(T.to(u.K).value)

    if kind == 'klimchuk':
        chi = np.ones(T.shape) * 1.96e-27
        alpha = np.ones(T.shape) * 1.0/2.0

        chi = np.where(log_temperature <= 7.63, 5.49e-16, chi)
        alpha = np.where(log_temperature <= 7.63, -1.0, alpha)

        chi = np.where(log_temperature <= 6.90, 3.46e-25, chi)
        alpha = np.where(log_temperature <= 6.90, 1.0/3.0, alpha)

        chi = np.where(log_temperature <= 6.55, 3.53e-13, chi)
        alpha = np.where(log_temperature <= 6.55, -3.0/2.0, alpha)

        chi = np.where(log_temperature <= 6.18, 1.90e-22, chi)
        alpha = np.where(log_temperature <= 6.18, 0.0, alpha)

        chi = np.where(log_temperature <= 5.67, 8.87e-17, chi)
        alpha = np.where(log_temperature <= 5.67, -1.0, alpha)

        chi = np.where(log_temperature <= 4.97, 1.09e-31, chi)
        alpha = np.where(log_temperature <= 4.97, 2.0, alpha)
    elif kind == 'rtv':
        # Not valid above 1e7
        chi = np.ones(T.shape) * np.nan
        alpha = np.ones(T.shape) * np.nan

        chi = np.where(log_temperature <= 7, 10**(-17.73), chi)
        alpha = np.where(log_temperature <= 7, -2/3, alpha)

        chi = np.where(log_temperature <= 6.3, 10**(-21.94), chi)
        alpha = np.where(log_temperature <= 6.3, 0., alpha)

        chi = np.where(log_temperature <= 5.75, 10**(-10.4), chi)
        alpha = np.where(log_temperature <= 5.75, -2.0, alpha)

        chi = np.where(log_temperature <= 5.4, 10**(-21.2), chi)
        alpha = np.where(log_temperature <= 5.4, 0.0, alpha)

        chi = np.where(log_temperature <= 4.9, 10**(-31), chi)
        alpha = np.where(log_temperature <= 4.9, 2, alpha)

        chi = np.where(log_temperature <= 4.6, 10.**(-21.85), chi)
        alpha = np.where(log_temperature <= 4.6, 0.0, alpha)

        # Not valid below 10^4.3
        chi = np.where(log_temperature <= 4.3, np.nan, chi)
    else:
        raise ValueError('Unrecognized power-law fit type.')

    return chi * T.to(u.K).value**alpha * u.erg * u.cm**3 / u.s
