# Import the necessary libraries
import numpy as np
import scipy.stats as stats
 
# Given information
T = 30
n = 5
m = 5

E = (n * (n+m+1)) / 2
Var = (n * m * (n+m+1)) / 12
alpha = 0.1
 
# compute the z-score
z_score = (T - E) / np.sqrt(Var)
print('Z-Score :',z_score)
 
# Approach 1: Using Critical Z-Score
 
# Critical Z-Score
z_critical = stats.norm.ppf(1-alpha)
print('Critical Z-Score :',z_critical)
 
# Hypothesis
if z_score >  z_critical:
    print("Reject Null Hypothesis")
else:
  print("Fail to Reject Null Hypothesis")
 
# Approach 2: Using P-value
     
# P-Value : Probability of getting less than a Z-score
p_value = 1-stats.norm.cdf(z_score)
 
print('p-value :',p_value) 
print('2P: ', (2 * p_value))
 
# Hypothesis
if p_value <  alpha:
    print("Reject Null Hypothesis")
else:
  print("Fail to Reject Null Hypothesis")