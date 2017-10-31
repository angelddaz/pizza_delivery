'''
Created on Feb 2, 2017
@author: angelddaz
tip_orderamount_distance
'''
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # @UnusedImport
#querying the data
path = r'C:\Users\Angel\OneDrive\Documents\data_training\data\RawDelData.csv'
data = pd.read_csv(path)
xADels = data.loc[data['Tip']>=-5][['OrderAmount']]
yADels = data.loc[data['Tip']>=-5][['Distance']]
zADels = data.loc[data['Tip']>=-5][['Tip']]
#random samples
nsize = 300
X = xADels.sample(n=nsize)
Y = yADels.sample(n=nsize)
Z = zADels.sample(n=nsize)
#create scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, color='gray', marker='s')
#formatting
ax.set_xlabel('Order Amount')
ax.set_ylabel('Distance From Store')
ax.set_zlabel('Tip')
ax.set_xlim(-0.5, 80) #lines 13 and 14
ax.set_ylim(-0.2, 9.5)
ax.set_zlim(-0.5, 25.5)
#done
plt.show()