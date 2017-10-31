import pandas as pd
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as pl
from scipy.optimize import curve_fit
from scipy.optimize import leastsq
import statsmodels.formula.api as sm
from statsmodels.api import add_constant

#################################################################################################
path = r'C:\Users\Angel\OneDrive\Documents\Data Training\data\loglinear.csv'
data = pd.read_csv(path)
xlist = data.loc[data['LN_TipPercent']>0.00][['LN_TipPercent']]                 #"querying" the data
ylist = data.loc[data['LN_TipPercent']>0.00][['LN_OrderAmount']]
x = xlist['LN_TipPercent'].tolist()
y = ylist['LN_OrderAmount'].tolist()

x = np.array(x, dtype=float) #transform your data in a numpy array of floats 
y = np.array(y, dtype=float) #so the curve_fit can work
pl.scatter(x, y)
pl.show()

##############################################################################################

lm = sm.ols(formula='LN_OrderAmount ~ LN_TipPercent', data=data).fit()
lm.params 	 

#X_new = pd.DataFrame({'TipPercent': [stats.TipPercent.min(), stats.TipPercent.max()]})
#X_new.head()

preds = lm.predict(add_constant(x), transform=False)

ax1 = pl.scatter(x, y)
#pl.ylim(-0.5, 100)
pl.suptitle('Tip Percentages At Every Order Amount', fontsize=18)
pl.title('Log-Linear Regression Analysis',fontsize=15)

ax2 = pl.plot(x, preds, c='red', linewidth=2)
pl.legend(ax2, ('Y = 2.65 + 0.14X',), loc='best')	#Need a trailing comma in legend
lm.summary()						#so that it all displays.
pl.show()

#Everything is statistically significant but there is a very low R^2
#Not sure what these results mean.
#I also filtered out the 0 tip because they were log(x) = -18