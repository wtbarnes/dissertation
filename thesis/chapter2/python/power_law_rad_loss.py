"""
Quick implementation of the Raymond-Klimchuk power-law radiative loss function.
See Eq. 3 of Klimchuk et al. (2008)
"""
import numpy as np
import astropy.units as u


@u.quantity_input
def power_law_rad_loss(T: u.K) -> u.erg * u.cm**3 / u.s:
    """
    Raymond-Klimchuk power-law radiative loss function. See Eq. 3 of Klimchuk et al. (2008)
    
    Arguments:
        T {u.K} -- [description]
    
    Returns:
        [type] -- [description]
    """
    log_temperature = np.log10(T.to(u.K).value)

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

    return chi * T.to(u.K).value**alpha * u.erg * u.cm**3 / u.s
