'''
Created on Feb 18, 2017

@author: angelddaz
This logistic regression doesn't work and I'm stuck as how to how debug and create
a smooth line between 0 and 1 of isMale. I will hopefully have someone to reach out to
soon.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

data = pd.read_csv(r'C:\Users\angelddaz\OneDrive\Documents\data_training\data\RawDelData.csv')
data['isMale'] = pd.Categorical(data.GenderOfTipper).codes

logreg = LogisticRegression(C=1e9)
feature_cols = ['Tip']
X = data[feature_cols]
y = data.isMale
logreg.fit(X,y)
data['tip_pred_class'] = logreg.predict(X)
plt.scatter(data.Tip, data.isMale)
plt.plot(data.Tip, data.tip_pred_class, color='red')
plt.xlabel('Tip')
plt.ylabel('isMale')
plt.grid()
plt.title("First One")
plt.show()

data['tip_pred_prob'] = logreg.predict_proba(X)[:,1]
print data.columns
#plot the class predictions
plt.scatter(data.Tip, data.isMale)
plt.plot(data.Tip, data.tip_pred_prob, color='red')
plt.xlabel('Tip')
plt.ylabel('isMale')
plt.grid()
plt.show()
