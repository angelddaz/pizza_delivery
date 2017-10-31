'''
Created on Jan 28, 2017

@author: Angel
'''
import pandas as pd
import matplotlib.pyplot as pl
import math

path = r'C:\Users\angelddaz\OneDrive\Documents\data_training\data\RawDelData.csv'
data = pd.read_csv(path)

aDels = data.loc[data['PersonWhoDelivered']=='Angel'][['Tip']]
sDels = data.loc[data['PersonWhoDelivered']=='Sammie'][['Tip']]
bDels = aDels+sDels

lista = aDels['Tip'].tolist() #single df col >> py list so that the data is plottable:
listb = sDels['Tip'].tolist()
listc = lista+listb

def getBin(x):
    count = len(x)
    binN = math.sqrt(count-1)-1
    binN = math.floor(binN)
    return binN


#Now to plot them separately
pl.xlim(-0.5,15)
pl.hist(lista,bins=getBin(lista))
pl.show()

pl.xlim(-0.5,15)
pl.hist(listb,bins=getBin(listb))
pl.show()

pl.xlim(-0.5,15)
pl.hist(listc,bins=getBin(listc))
pl.show()


#Plotting a & b overlay
pl.xlim(-0.5,15)
pl.hist(lista,bins=getBin(listb), label='Angel')

pl.xlim(-0.5,15)
ax2 = pl.hist(listb,bins=getBin(listb), label='Sammie')
pl.legend(loc='best')
pl.show()


#Plotting a, b, & c separated in the same image
fig = pl.figure()
ax1 = fig.add_subplot(2, 2, 1)
pl.xlim(-0.5,15)
pl.ylim(0, 250)
ax1.hist(lista,bins=getBin(lista))
ax1.set_title('Angel Deliveries')
ax1.set_ylabel('Count of Tips')
ax1.set_xlabel('Tip Dollar Amount')

ax2 = fig.add_subplot(2, 2, 3)
ax2.hist(listb,bins=getBin(listb))
pl.xlim(-0.5,15)
pl.ylim(0, 250)
ax2.set_title('Sammie Deliveries')
ax2.set_ylabel('Count of Tips')
ax2.set_xlabel('Tip Dollar Amount')

ax3 = fig.add_subplot(2, 2, 2)
ax3.hist(listc, bins=getBin(listc))
pl.ylim(0, 250)
pl.xlim(-0.5,15)
ax3.set_title('Combined Deliveries')
ax3.set_xlabel('Tip Dollar Amount')
pl.show()