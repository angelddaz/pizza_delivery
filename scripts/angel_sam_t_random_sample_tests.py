'''
Created on Jan 27, 2017
@author: Angel
'''
import pandas as pd
import math
import scipy.stats as stats
import numpy as np

path = r'C:\Users\Angel\OneDrive\Documents\data_training\data\RawDelData.csv'
data = pd.read_csv(path)
df = pd.DataFrame(data, columns = ['Tip', 'PersonWhoDelivered'])
aDels = data.loc[data['PersonWhoDelivered']=='Angel'][['Tip']]
sDels = data.loc[data['PersonWhoDelivered']=='Sammie'][['Tip']]

'''
H0 : mu_a = mu_s
Ha: mu_a != mu_s 
Degrees of freedom: df = 298
significance level: 0.05
therefore, critical value = 1.9673
'''

FTRcount = 0
RejH0count = 0
loop = range(100)
loopcount = len(loop)

ps = []

for i in loop:
    aDels = aDels.sample(n=200)
    sDels = sDels.sample(n=200)
    
    #variables
    mu_a = aDels.mean() 
    mu_s = sDels.mean()   
    sigma_a = aDels.std() 
    sigma_s = sDels.std() 
    variance_a = aDels.std() * aDels.std() 
    variance_s = sDels.std() * sDels.std()
    n_a = aDels.count()
    n_s = sDels.count()
    
    #Two Sample T Test
    df = n_a + n_s - 2 -1 #n1+n2-k-1: degrees of freedom 
    den1 = variance_a/n_a 
    den2 = variance_s/n_s 
    den3 = den1+den2
    den = math.sqrt(den3)
    num = mu_a - mu_s
    t_crit = stats.t.ppf(1-0.025, df)
    t_stat = num/den
    
    pval = stats.t.sf(np.abs(t_stat), df)*2

    #ps.append(float(pval)) 
    #how to append variables into a list, must remember to put into dataframe for statistics after the loop
    
    
    if float(abs(t_stat)) > float(t_crit):
        RejH0count += 1
        #print('t-statistic = %6.3f pvalue = %6.4f' % (t_stat, pval))
    else:
        FTRcount += 1   
print('There were %4.0f amount of random sample t-tests. Out of all of these tests,' % (loopcount))
print('%4.0f failed to reject and, %4.0f rejected the null hypothesis.' % (FTRcount, RejH0count))