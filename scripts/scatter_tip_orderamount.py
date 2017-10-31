'''
Created on Jan 28, 2017

@author: angelddaz
'''
import pandas as pd
import matplotlib.pyplot as pl

path = r'C:\Users\angelddaz\OneDrive\Documents\data_training\data\RawDelData.csv'
data = pd.read_csv(path)
xlist = data.loc[data['Tip']>-100.00][['Tip']]  #"querying" the data
ylist = data.loc[data['OrderAmount']>-100.00][['OrderAmount']]
listx = xlist['Tip'].tolist()
listy = ylist['OrderAmount'].tolist()
listx = [round(elem, 2) for elem in listx] #Rounding every element to two decimals.
listy = [round(elem, 2) for elem in listy]

#a scatter plot of every tip amount at every order amount
x13 = 13.5
x25 = 25.5
pl.xlim(-0.5, x13) #change the x limit here depending on preference.
pl.ylim(-0.5, 100)
pl.xlabel('Tip Amount')
pl.ylabel('Order Amount')
pl.title('Combined Tips at every Order Amount')
pl.scatter(listx, listy)
pl.show()