'''
Created on Feb 8, 2017

@author: angelddaz
'''
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np

df = pd.read_csv(r'C:\Users\angelddaz\OneDrive\Documents\data_training\data\RawDelData.csv')


print df.tail()
plt.figure(figsize=(15, 6))
plt.scatter(df.OrderAmount, df.TipPercent, s=10, alpha=0.3)
plt.xlabel('OrderAmount') 
plt.ylabel('Tip Percentage')

plt.xlim(-0.5, df.OrderAmount.max())
plt.ylim(-0.5, df.TipPercent.max())

#points linearly space on tips
x = pd.DataFrame({'OrderAmount': np.linspace(df.OrderAmount.min(), df.OrderAmount.max(), 100)})

#1st order polynomial
poly_1 = smf.ols(formula='TipPercent ~ 1 + OrderAmount', data=df).fit()
plt.plot(x.OrderAmount, poly_1.predict(x), 'b-', label='Poly n=1 $R^2$=%.2f' % poly_1.rsquared, alpha=0.95)
#2nd order polynomial
poly_2 = smf.ols(formula='TipPercent ~ 1 + OrderAmount + I(OrderAmount ** 2.0)', data=df).fit()
plt.plot(x.OrderAmount, poly_2.predict(x), 'g-', label='Poly n=2 $R^2$=%.2f' % poly_2.rsquared, alpha=0.95)
#3rd order polynomial
poly_3 = smf.ols(formula='TipPercent ~ 1 + OrderAmount + I(OrderAmount ** 2.0) + I(OrderAmount ** 3.0)', data=df).fit()
plt.plot(x.OrderAmount, poly_3.predict(x), 'r-', alpha=0.95, label='Poly n=3 $R^2$=%.2f' % poly_3.rsquared)

plt.legend()
plt.show()