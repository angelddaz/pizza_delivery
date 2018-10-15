# -*- coding: utf-8 -*-
"""
@author: angel
"""

## shift+enter to run selected code in vs code.

#%matplotlib inline
from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import matplotlib.mlab as mlab
import statsmodels.formula.api as sm
from statsmodels.api import add_constant
import math
import scipy.stats as stats
import seaborn as sns
#%matplotlib inline
sns.set(style="ticks")

#url = 'https://raw.githubusercontent.com/angelddaz/pizza_delivery/master/RawDelData.csv'
csv = r'C:\Users\angel\OneDrive\Documents\other\data_training\data\RawDelData.csv'
data = pd.read_csv(csv) 

print('\n')
print(data.head())

# time for some plots

ylabel = 'Tip Amount'
xlabel = 'Order Amount'
#####################################################
def create_scatter(df, title_name):
    pl.scatter(df.OrderAmount, df.Tip)
    n = len(df)
    pl.title('n = %s' %n, fontsize=22)
    pl.suptitle(title_name, fontsize=22)
    pl.ylabel(ylabel, fontsize=18)
    pl.xlabel(xlabel, fontsize=18)
    pl.ylim(-0.25, 15) #The right bound excludes outliers in the visualization but not the sample count
    pl.xlim(-0.30, 80) #DITTO the comment above
    pl.rcParams['figure.figsize'] = (15, 10)
    pl.show()

create_scatter(data, 'All Deliveries')
#####################################################

x = data['OrderAmount']
y = data['Tip']
xyplot = sns.jointplot(x, y, kind="reg", color="#33528c", size=15, dropna=True)
pl.show()
#####################################################

#bplots = sns.factorplot("GenderOfTipper", "Tip", "PersonWhoDelivered", data, kind="box", size=8)
#bplots.set_axis_labels('',ylabel)

#####################################################

xyplots = sns.FacetGrid(data, col="GenderOfTipper", row="PersonWhoDelivered", size=5)
xyplots.map(pl.scatter,"OrderAmount","Tip")
pl.show()
#####################################################

xyplot = sns.jointplot(x, y, kind="hex", color="#33528c", size=15, dropna=True)
xyplot.set_axis_labels(xlabel,ylabel)
pl.show()
#####################################################

def create_hist(df, title_name):
    x = df.Tip
    n = len(df)
    bin_width = create_bin_width(df)    #two function calls to make the code a bit more modular and easier to use 
                                        #when creating multiple histograms on the same axes.
    bin_num = create_bin_num(df, bin_width)
    sigma = df.Tip.std()
    mu = df.Tip.mean()
    n, bins, patches = pl.hist(x, bin_num, normed=1, facecolor='green', alpha=0.75, edgecolor='black',linewidth=1.2)
    # add a 'best fit' line
    y = mlab.normpdf( bins, mu, sigma)
    l = pl.plot(bins, y, 'r--', linewidth=1)
    pl.grid(True)
    
    n = len(df)
    pl.suptitle(title_name, fontsize=22)
    pl.title('n = %s' %n, fontsize=22)
    pl.ylabel(ylabel, fontsize=18)
    pl.xlabel(xlabel, fontsize=18)
    pl.rcParams['figure.figsize'] = (15, 10)
    pl.show()
    
def create_bin_width(df):
    x = df.Tip
    n = len(df)
    '''The Freedman-Diaconis rule is very robust and works well in practice. 
    The bin-width is set to max-min/h
    where: h = 2∗IQR∗n^(−1/3)'''
    q75, q25 = np.percentile(x, [75 ,25])
    iqr = q75 - q25
    h = 2*iqr*n**(1.0/3)
    range = x.max() - x.min()
    bin_width = range/h
    return bin_width

def create_bin_num(df, bin_width):
    x = df.Tip
    range = x.max() - x.min()
    bin_num = math.floor(range/bin_width)
    return bin_num

create_hist(data, "Histogram of All Deliveries")

#####################################################
sam_tip = data.loc[data['PersonWhoDelivered']=='Sammie']
create_hist(sam_tip, 'All of Sam Deliveries')
#####################################################
angel_tip = data.loc[data['PersonWhoDelivered']=='Angel']
create_hist(angel_tip, 'All of Angel Deliveries')
#####################################################
df_x = angel_tip
df_y = sam_tip
x_bin_width = create_bin_width(df_x)
y_bin_width = x_bin_width #create_bin_width(df_y) #same bin widths
x_bin_num = create_bin_num(df_x, x_bin_width) #Different bin widths, I'm not sure if this is the way to do it
y_bin_num = x_bin_num #create_bin_num(df_y, y_bin_width) #same bin numbers
df_x = angel_tip.Tip #re-instantiating these variables because the two functions I created change them
df_y = sam_tip.Tip   #Maybe not the most efficient method.
pl.hist(df_x, x_bin_num, alpha=0.5, label='Angel Deliveries', edgecolor='black',linewidth=1.2)
pl.hist(df_y, y_bin_num, alpha=0.5, label='Sam Deliveries', edgecolor='black',linewidth=1.2)
pl.legend(loc='best')
angel_n = len(angel_tip)
sam_n = len(sam_tip)
pl.suptitle("All Angel and Sam Deliveries", fontsize=22)
pl.title('Angel_n = %d \n Sam_n = %d'% (angel_n, sam_n), fontsize=19)
pl.xlabel(xlabel, fontsize=18)
pl.rcParams['figure.figsize'] = (15, 10)
pl.show()

angel_n = angel_n * 1.0
p = sam_n / angel_n
print ("Overall Proportion of Delivery count is : %s Sam deliveries for every one Angel Delivery" %p)

#####################################################

#####################################################

#####################################################

#####################################################

#####################################################


# we need tip amount and person who delivered
df = pd.DataFrame(data, columns = ['Tip', 'PersonWhoDelivered'])
print('n\Tip Amount and Person Who Delivered dataframe')
print(df.head())

# and then we split up the data into two different columns or arrays
aDels = data.loc[data['PersonWhoDelivered']=='Angel'][['Tip']]
sDels = data.loc[data['PersonWhoDelivered']=='Sammie'][['Tip']]

#both deliveries
bDels = aDels+sDels

# now let's collect our ingredients
n_a = aDels.count()
print('\nCount of my deliveries')
print(n_a)
n_s = sDels.count()
print('\nCount of Sam\'s deliveries')
print(n_s)

mu_a = aDels.mean()
print('\nMy Tip Amount Average')
print(mu_a)
mu_s = sDels.mean()
print('\nSam\'s Tip Amount Average')
print(mu_s)

# standard deviations
sigma_a = aDels.std()
print('\nMy Tip Amount Standard Deviation')
print(sigma_a)
sigma_s = sDels.std()
print('\nSam\'s Tip Amount Standard Deviation')
print(sigma_s)

sigmasquared_a = aDels.std() * aDels.std()
print('\nMy Tip Amount Variance')
print(sigmasquared_a)
sigmasquared_s = sDels.std() * sDels.std()
print('\nSam\'s Tip Amount Variance')
print(sigmasquared_s)

degfreedom = n_a + n_s - 2 -1 #n-k-1: degrees of freedom = 1298
print('\nDegrees of Freedom')
print(degfreedom)


# Our null hypothesis is that there is no difference between my tip
# and Sam's tip average tips.

#Two Sample T Test

# first I calculated the denominator, chunk by chunk
# hand coded because I didn't know any better
den1 = sigmasquared_a/n_a
den2 = sigmasquared_s/n_s
den3 = den1+den2
den = math.sqrt(den3)
print('\nOur Denominator Value')
print(den)

num = mu_a - mu_s
print('\nOur Numerator Value')
print(num)

t_stat = num/den
print('\nFinally Our t-statistic')
print(t_stat)


print('\nH0 : mu_a == mu_s')
print('Ha: mu_a != mu_s')
print('Degrees of freedom: df = 1298')
print('significance level: 0.05')
print('therefore, critical value = 1.9673')

tcrit = 1.9673
print('\n')
print(t_stat)

pval = stats.t.sf(np.abs(t_stat), degfreedom)
print(pval)
print('\nWe fail to reject the null hypothesis, and the result is not')
print('statistically significant at p < .05')

# Although Sam had a tip amount average 4 cents higher than me
# We cannot say they were statistically different

#####################################################

#####################################################

#####################################################

#####################################################


#Querying our data!
# Grabbing only tip and distance
stats = data.loc[data['OrderAmount']>-100.00][['Tip','Distance']]
#This is the model magic
lm = sm.ols(formula='Tip ~ Distance', data=stats).fit()
print('\n')
print(lm.params)

#####################################################
X_new = pd.DataFrame({'Distance': [stats.Distance.min(), stats.Distance.max()]})
X_new.head()
#making the line with our observed distances
preds = lm.predict(add_constant(X_new), transform=False)
#plotting our scatter plot
ax1 = stats.plot(kind='scatter', x='Distance', y='Tip')
#Making it pretty
ax1.text(7, 20, r'Rsquared: 0.011', fontsize=15)
pl.ylabel('Tip Amount in Dollars', fontsize=18)
pl.xlabel('Distance From Store in Miles', fontsize=18)
pl.xlim(-0.25, 8.7)
pl.ylim(-0.30, 25.2)
pl.suptitle('Distances At Every Tip Amount', fontsize=22)
pl.title('Linear Regression Analysis',fontsize=15)
pl.rcParams['figure.figsize'] = (15, 10)
#plotting our line
ax2 = pl.plot(X_new,preds, c='red', linewidth=2)
pl.legend(ax2, ('Y = 3.0295 + 0.1588X',), loc='best')
pl.show()

#####################################################
print lm.summary()

#####################################################
X_new = pd.DataFrame({'Distance': [stats.Distance.min(), stats.Distance.max()]})
X_new.head()
#making the line with our observed distances
preds = lm.predict(add_constant(X_new), transform=False)
#plotting our scatter plot
ax1 = stats.plot(kind='scatter', x='Distance', y='Tip')
#Making it pretty
pl.ylabel('Tip Amount in Dollars', fontsize=18)
pl.xlabel('Distance From Store in Miles', fontsize=18)
pl.xlim(-0.25, 8.7)
pl.ylim(-0.30, 25.2)
pl.suptitle('Tip Amounts at every Distance', fontsize=22)
pl.rcParams['figure.figsize'] = (15, 10)

#####################################################

tips = data.loc[data['Distance']>=0][['Tip']]
tipmean = tips.mean()
print('\n')
print(tipmean)

tips = data.loc[data['Distance']>=5][['Tip']]
fartipmean = tips.mean()
print('\n')
print(fartipmean)

#####################################################

filtered = data.loc[data['Distance']<5.00][['Tip', 'Distance']]

lm = sm.ols(formula='Tip ~ Distance', data=filtered).fit()
lm.params     #Intercept:3.3         #OrderAmount: 0.02

X_new = pd.DataFrame({'Distance': [filtered.Distance.min(), filtered.Distance.max()]})
preds = lm.predict(add_constant(X_new), transform=False)
ax1 = filtered.plot(kind='scatter', x='Distance', y='Tip')
ax1.text(4, 20, r'Rsquared: 0.000', fontsize=15)
pl.xlim(-0.25, 5)
pl.ylim(-0.30, 25.2)
pl.ylabel('Tip', fontsize=18)
pl.xlabel('Distance From Store in Miles', fontsize=18)
#pl.xticks(min(X_new), max(X_new)+0.5, 1.0)
pl.suptitle('Distances Less Than 5 Miles At Every Tip Amount', fontsize=24)
pl.title('Linear Regression Analysis',fontsize=22)
ax2 = pl.plot(X_new,preds, c='red', linewidth=2)
pl.legend(ax2, ('Y = 3.3 + 0.0194X',), loc='best')         #Need a trailing comma in legend
lm.summary()                            #so that it all displays.
pl.rcParams['figure.figsize'] = (15, 10)
pl.show()

#####################################################