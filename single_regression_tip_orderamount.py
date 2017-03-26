'''
Created on Jan 28, 2017

@author: Kevin Markham @justmarkham, Angel
tutorial here:
https://github.com/justmarkham/DAT4/blob/master/notebooks/08_linear_regression.ipynb
'''
import pandas as pd
import matplotlib.pyplot as pl
import statsmodels.formula.api as sm

path = r'C:\Users\Angel\OneDrive\Documents\data_training\data\RawDelData.csv'
data = pd.read_csv(path)

x13 = 13.5 #x right bounds for line 30
x25 = 25.5

both = data.loc[data['OrderAmount']>-100.00][['Tip','OrderAmount']]
lm = sm.ols(formula='OrderAmount ~ Tip', data=both).fit()

#This is a prediction algorithm.
#X_new = pd.DataFrame({'Tip': [6]}) 
#X_new.head()
#print(lm.predict(X_new))

X_new = pd.DataFrame({'Tip': [both.Tip.min(), both.Tip.max()]})
X_new.head()

preds = lm.predict(X_new)
ax1 = both.plot(kind='scatter', x='Tip', y='OrderAmount')
pl.xlim(-0.5, x25) #lines 13 and 14
pl.ylim(-0.5, 100)
pl.suptitle('Combined Tips At Every Order Amount', fontsize=18)
pl.title('Linear Regression Analysis',fontsize=15)

ax2 = pl.plot(X_new,preds, c='red', linewidth=2)
pl.legend(ax2, ('Y = 16.43+1.59X',), loc='best') #Need a trailing comma in legend
pl.show()

print("conf_ints are:\n" + str(lm.conf_int())+ "\n") #Does not include 0
print("R^2 is:\n" + str(lm.rsquared) + "\n")   #R^2 = 0.1321
print("pvals are: \n" + str(lm.pvalues))

'''
At a 95% confidence level: 
Confidence interval is Tip: 1.37 -- 1.82
Rsquared: 0.13
P-Value(Tips): 6.35e-42
Model: Y = 16.43 + 1.59X
Y = Order Amount
X = Tip Amount

There is a small, yet statistically significant, correlation between order amounts and tip amounts. 
This model falls apart quickly as tips increase past $10 because people usually don't tip in the double digits. 
There is also a large margin of error with the model, as the R^2 value is relatively low at 0.13.
'''
