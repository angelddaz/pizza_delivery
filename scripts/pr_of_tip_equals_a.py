'''
Created on Jan 28, 2017

@author: Angel
'''
import pandas as pd
import scipy.stats

path = r'C:\Users\angelddaz\OneDrive\Documents\data_training\data\RawDelData.csv'
data = pd.read_csv(path)

aDels = data.loc[data['PersonWhoDelivered']=='Angel'][['Tip']]
sDels = data.loc[data['PersonWhoDelivered']=='Sammie'][['Tip']]
bDels = aDels+sDels

#variables
mu_a = aDels.mean() 
mu_s = sDels.mean()
sigma_a = aDels.std() 
sigma_s = sDels.std()
variance_a = aDels.std() * aDels.std()
variance_s = sDels.std() * sDels.std()
n_a = aDels.count()
n_s = sDels.count()

X_a = 3 #value of a
X_s = 3
z_a = (X_a-mu_a)/sigma_a
z_s = (X_s-mu_s)/sigma_s
pval_a = scipy.stats.norm.sf(z_a) 
pval_s = scipy.stats.norm.sf(z_s)

print("The probability that I receive a tip larger than %1.0f is %1.4f" % (X_a, pval_a)) 
print("The probability that Sam receives a tip larger than %1.0f is %1.4f" % (X_a, pval_a))

#What about low tips. 1 dollar or lower?
X_a = 1 #value of a
X_s = 1 
z_a = (X_a-mu_a)/sigma_a
z_s = (X_s-mu_s)/sigma_s

pval_a = 1 - scipy.stats.norm.sf(z_a)
pval_s = 1 - scipy.stats.norm.sf(z_s)
print
print("The probability that I receive a tip less than %1.0f is %1.4f" % (X_a, pval_a)) 
print("The probability that Sam receives a tip less than %1.0f is %1.4f" % (X_a, pval_a))
