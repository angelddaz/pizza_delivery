import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import statsmodels.formula.api as sm
from statsmodels.api import add_constant

path = r'C:\Users\angelddaz\OneDrive\Documents\Data Training\data\RawDelData.csv'
data = pd.read_csv(path)

stats = data.loc[data['OrderAmount']>-100.00][['TipPercent','OrderAmount']]

lm = sm.ols(formula='OrderAmount ~ TipPercent', data=stats).fit()
lm.params 	#Intercept:25.515787 	#OrderAmount:-21.116315 
#################################################################################
X_new = pd.DataFrame({'TipPercent': [0.9]}) ##Predicting Order Amounts with Tip %
X_new.head()
lm.predict(add_constant(X_new), transform=False)
#################################################################################
X_new = pd.DataFrame({'TipPercent': [stats.TipPercent.min(), stats.TipPercent.max()]})
X_new.head()

xticks = np.arange(0,1.2,0.1)
preds = lm.predict(add_constant(X_new), transform=False)
ax1 = stats.plot(kind='scatter', x='TipPercent', y='OrderAmount')
pl.xlim(-0.030, 1.1)
pl.xticks(xticks)
pl.ylim(-0.5, 100)
pl.suptitle('Tip Percentages At Every Order Amount', fontsize=18)
pl.title('Linear Regression Analysis',fontsize=15)

ax2 = pl.plot(X_new,preds, c='red', linewidth=2)
pl.legend(ax2, ('Y = 25.52-21.12X',), loc='best')	#Need a trailing comma in legend
lm.summary()						#so that it all displays.
pl.show()						 


### HOW confident am I in this model?
### print the confidence intervals for the model coefficients
#lm.conf_int() 	#Does not include 0
### print the R-squared value for the model
#lm.rsquared   	#R^2 = 0.052
### print the p-values for the model coefficients
#lm.pvalues 	#0 for both