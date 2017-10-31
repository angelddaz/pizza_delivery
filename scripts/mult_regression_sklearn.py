'''
Created on Jan 28, 2017

@author: Angel
tip_orderamount_whodel

TODO: how to create a complete regression analysis with dummy variable, 
    not just coefficients.
'''
import pandas as pd
import numpy as np
from sklearn.linear_model.base import LinearRegression

path = r'C:\Users\Angel\OneDrive\Documents\data_training\data\RawDelData.csv'
data = pd.read_csv(path)

data["isAngel"] = ""
data["isAngel"] = np.nan
dat = data.loc[data['OrderAmount']>-100.00][['Tip','OrderAmount','PersonWhoDelivered', 'isAngel']]

dat.loc[dat.PersonWhoDelivered == 'Angel', ['isAngel']] = 1
dat.loc[dat.PersonWhoDelivered == 'Sammie', ['isAngel']] = 0
feature_cols = ['OrderAmount', 'isAngel']
X = dat[feature_cols]
y = dat.Tip
lm = LinearRegression()
lm.fit(X, y)

print "Tips can be modeled by Y = 1.61 + 0.0829X_1 - 0.0533X2"
print "In other words, tips go up by 8 cents for every dollar"
print "increase in order amount and decrease by 5 cents if Angel is making the delivery."