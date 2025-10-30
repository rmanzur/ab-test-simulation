def ab_test_sim(n_total, #total number of experiment units (n_control and n_treatment)
                control_mean, 
                relative_lift, 
                r =0.5, 
                n_simulations=10000, #number of simulations
                alpha=0.05,
                is_two_tailed = True):

    sig_count = 0 #number of simulations with statistically significant result
    pvalue_list = [] 
    n_treatment = int(n_total*r)
    n_control = n_total - n_treatment
    treatment_mean = control_mean*(1+ relative_lift)
    
    for _ in range(n_simulations):
        conv_control = np.random.binomial(n_control, control_mean) 
        conv_treatment = np.random.binomial(n_treatment, treatment_mean)
        
        # Calculate statistical significance
        p = p_value(n_total, control_mean = conv_control/n_control, treatment_mean = conv_treatment/n_treatment, r = r, is_two_tailed = is_two_tailed)
        pvalue_list.append(p)
        sig_indicator = is_stat_sig(p, alpha)
        
        if sig_indicator:
            sig_count += 1
            
    #if no actual difference exists then rate is the false positive rate (alpha) but if a difference exists then rate is the true positive rate (power)   
       
    rate = sig_count / n_simulations
    return rate, pvalue_list
