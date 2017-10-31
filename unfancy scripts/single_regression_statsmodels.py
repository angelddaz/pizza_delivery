'''
Created on Feb 3, 2017

@author: angelddaz
tip_distance
'''
import pandas as pd
import matplotlib.pyplot as pl
import statsmodels.formula.api as sm
from statsmodels.api import add_constant

data = pd.read_csv(r'C:\Users\angelddaz\OneDrive\Documents\data_training\data\RawDelData.csv')

stats = data.loc[data['OrderAmount']>-100.00][['Tip','Distance']]

lm = sm.ols(formula='Tip ~ Distance', data=stats).fit()
print lm.params

X_new = pd.DataFrame({'Distance': [0.9]}) ##Predicting Tip with Distance
X_new.head()
lm.predict(add_constant(X_new), transform=False)

X_new = pd.DataFrame({'Distance': [stats.Distance.min(), stats.Distance.max()]})
X_new.head()


preds = lm.predict(add_constant(X_new), transform=False)
ax1 = stats.plot(kind='scatter', x='Distance', y='Tip')
ax1.text(7, 20, r'Rsquared: 0.011', fontsize=15)
pl.xlabel('Tip Amount in Dollars')
pl.xlabel('Distance From Store in Miles') 
pl.xlim(-0.25, 8.7)
pl.ylim(-0.30, 25.2)
#pl.xticks(min(X_new), max(X_new)+0.5, 1.0)
pl.suptitle('Distances At Every Tip Amount', fontsize=18)
pl.title('Linear Regression Analysis',fontsize=15)

ax2 = pl.plot(X_new,preds, c='red', linewidth=2)
pl.legend(ax2, ('Y = 3.0295 + 0.1588X',), loc='best')         #Need a trailing comma in legend
print lm.summary()                        #so that it all displays.
pl.show()                         


#First we need to query the data that's past 5, 6, and 7 miles to see what's going on.
far = data.loc[data['Distance']>=5.00][['Tip','Area(text)', 'Distance']]
#This gives us 38 deliveries. 33 of which are Hidden Springs deliveries.
#Wealthier neighborhoods tip more, not because of distance. To support this claim
#let's look at Garden City data, which is closer, poorer, and tips worse.
far['Distance'].mean() # = 7.4789
far['Tip'].mean() # = 5.0882

gc = data.loc[data['Area(text)']=='Garden City'][['Tip','Area(text)', 'Distance']]
gc['Distance'].mean() # = 2.5480
gc['Tip'].mean() # = 2.9583

#So let's run the same linear correlation model but without these Hidden Springs rich
#people skewing our data.
#################################################################################
filtered = data.loc[data['Distance']<5.00][['Tip', 'Distance']]

lm = sm.ols(formula='Tip ~ Distance', data=filtered).fit()
lm.params     #Intercept:3.3         #OrderAmount: 0.02

X_new = pd.DataFrame({'Distance': [filtered.Distance.min(), filtered.Distance.max()]})
X_new.head()

preds = lm.predict(add_constant(X_new), transform=False)
ax1 = filtered.plot(kind='scatter', x='Distance', y='Tip')
ax1.text(4, 20, r'Rsquared: 0.000', fontsize=15)
pl.xlim(-0.25, 5)
pl.ylim(-0.30, 25.2)
pl.ylabel('Tip')
pl.xlabel('Distance From Store in Miles')
#pl.xticks(min(X_new), max(X_new)+0.5, 1.0)
pl.suptitle('Distances Less Than 5 Miles At Every Tip Amount', fontsize=18)
pl.title('Linear Regression Analysis',fontsize=15)

ax2 = pl.plot(X_new,preds, c='red', linewidth=2)
pl.legend(ax2, ('Y = 3.3 + 0.0194X',), loc='best')         #Need a trailing comma in legend
lm.summary()                            #so that it all displays.
pl.show()
#################################################################################
#The filtered model without the 38 farthest deliveries is now nearly flat.
#For every mile increased, there can be an increase of 16 cents but Rsquared is 0.
#Virtually no relation between distance and amount people tip.

#The intercept for this model is 10 cents lower than total sample average.
#Just looking at the scatter plot also gives a hint that tips of every amount can
#be found at nearly every distance amount.