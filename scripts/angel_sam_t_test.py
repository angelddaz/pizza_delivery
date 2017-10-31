'''
Created on Jan 27, 2017
@author: angelddaz
These are statistical T-tests of many random samples to see if
Samantha's and my tips are statistically different. 
'''
import pandas as pd
import math
import scipy.stats as stats

#Change the following line/path depending on which machine you're working on
path = r'C:\Users\Angel\OneDrive\Documents\data_training\data\RawDelData.csv'
data = pd.read_csv(path)
df = pd.DataFrame(data, columns = ['Tip', 'PersonWhoDelivered'])

'''
H0 : mu_a = mu_s
Ha: mu_a != mu_s 
Degrees of freedom: df = 1298
significance level: 0.05
therefore, critical value = 1.9673
'''

aDels = data.loc[data['PersonWhoDelivered']=='Angel'][['Tip']]
sDels = data.loc[data['PersonWhoDelivered']=='Sammie'][['Tip']]


mu_a = aDels.mean() #Angel Delivery mean = 3.376236
mu_s = sDels.mean() #Sammie Delivery mean = 3.412869

sigma_a = aDels.std() #Angel stdev = 2.184814
sigma_s = sDels.std() #Sammie stdev = 2.040795

variance_a = aDels.std() * aDels.std() #Angel variance = 4.773414
variance_s = sDels.std() * sDels.std() #Sammie variance = 4.164844

n_a = aDels.count() #Angel sample size = 712
n_s = sDels.count() #Sammie sample size = 589

df = n_a + n_s - 2 -1 #n-k-1: degrees of freedom = 1298

#This is where the Hypothesis starts:
#Two Sample T Test
den1 = variance_a/n_a #formula chunk: 0.006704
den2 = variance_s/n_s #formula chunk: 0.007071
den3 = den1+den2      #formula chunk: 0.013775
den = math.sqrt(den3) #denominator value: 0.11736812016136079
num = mu_a - mu_s     #numerator value: -0.036633


t_crit = 1.9673
t_stat = num/den
pval = 1-stats.t.sf(t_stat, df)

if float(t_stat) < float(t_crit):
    print("We fail to reject the null hypothesis that the two means are statistically the same.")
    print("Therefore, we can conclude with some certainty that the two tips means are equal.")
    print('t-statistic = %6.3f pvalue = %6.4f' % (t_stat, pval))
else:
    print("We reject the null hypothesis that the two means are statistically the same.")

#We fail to reject the null hypothesis, and the result is not
#statistically significant at p < .05
#P-Value is 0.3775

#still not statistically significant!
