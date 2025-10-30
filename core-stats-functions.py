# import packages for simulation and data visualization
import numpy as np
import matplotlib.pyplot as plt
import random
import math
from scipy import stats

#define functions to calculate the minimum sample size for given parameters, and p-value to determine statistical significance

def min_sample_size(relative_lift, #expected relative lift from control
                    control_mean, #baseline conversion rate
                    alpha = 0.05, 
                    power = 0.8, 
                    r = 0.5, #proportion allocated to treatment
                    is_two_tailed = True):
    
    def z_alpha():
        if is_two_tailed:
            return stats.norm.ppf(1 - alpha/2)
        else:
            return stats.norm.ppf(1 - alpha)
    def z_beta():
        return stats.norm.ppf(power)
    
    mde = control_mean * relative_lift #convert to absolute lift
    treatment_mean = control_mean + mde
    var = (treatment_mean * (1 - treatment_mean)) / r + (control_mean * (1 - control_mean)) / (1 - r)
    
    n_total = var*((z_alpha() + z_beta()) / mde) ** 2 
    
    return np.ceil(n_total)    


def p_value(n_total, 
            control_mean, 
            treatment_mean, #observed treatment conversion rate
            r = 0.5, #proportion allocated to treatment
            is_two_tailed = True):
    
    n_treatment = int(n_total*r)
    n_control = n_total - n_treatment
    
    p_pooled = (control_mean * n_control + treatment_mean * n_treatment) / n_total
    se = np.sqrt(p_pooled * (1 - p_pooled) * (1/n_control + 1/n_treatment))  # standard error using pooled variance
    
    z_stat = (treatment_mean - control_mean) / se
    
    if is_two_tailed:
        p = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    else:
        p = 1 - stats.norm.cdf(z_stat)
    
    return p

def is_stat_sig(p_value, alpha = 0.05):
    return p_value < alpha
    
    
