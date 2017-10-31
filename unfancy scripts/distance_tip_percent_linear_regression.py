import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import statsmodels.formula.api as sm
from statsmodels.api import add_constant

path = r'C:\Users\angelddaz\OneDrive\Documents\Data Training\data\RawDelData.csv'
data = pd.read_csv(path)

stats = data.loc[data['OrderAmount']>-100.00][['TipPercent','Distance']]

lm = sm.ols(formula='TipPercent ~ Distance', data=stats).fit()
lm.params 	#Intercept: 15.553768	#Distance: 0.315809
#################################################################################
X_new = pd.DataFrame({'Distance': [0.9]}) ##Predicting Tip Percentage with Distance
X_new.head()
lm.predict(add_constant(X_new), transform=False)
#################################################################################
X_new = pd.DataFrame({'Distance': [stats.Distance.min(), stats.Distance.max()]})
X_new.head()


preds = lm.predict(add_constant(X_new), transform=False)
ax1 = stats.plot(kind='scatter', x='Distance', y='TipPercent')
ax1.text(7, 90, r'Rsquared: 0.002', fontsize=15)
pl.ylabel('Tip Percentage of Order')
pl.xlabel('Distance From Store in Miles')
pl.xlim(-.25, 8.7)
pl.ylim(-2.5, 105)
#pl.xticks(min(X_new), max(X_new)+0.5, 1.0)
pl.suptitle('Distances At Every Tip Percentage of Order Amount', fontsize=18)
pl.title('Linear Regression Analysis',fontsize=15)

ax2 = pl.plot(X_new,preds, c='red', linewidth=2)
pl.legend(ax2, ('Y = 15.55 + 0.32X',), loc='best') 		#Need a trailing comma in legend
lm.summary()						#so that it all displays.
pl.show()						 

### HOW confident am I in this model?
### print the confidence intervals for the model coefficients
#lm.conf_int() 	#INCLUDES 0: -0.075 -- 0.706
### print the R-squared value for the model
#lm.rsquared   	#R^2 = 0.002
### print the p-values for the model coefficients
#lm.pvalues 	#Above 0.05 at 0.113

#Since we did all of the digging in 'SingleRegression-'Distance'+'Tip'.txt'
#There's no need to repeat the same procress when even this model has a terrible
#goodness of fit and is not statistically significant.
#We can say with a lot of confidence, that distance from the store does not affect
#tip amounts.