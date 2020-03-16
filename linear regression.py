# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:17:56 2019

@author: alexius
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab as pl
import numpy as np
from sklearn import linear_model
df = pd.read_csv('FuelConsumptionCo2.csv')
df.head()
#note when do head or describe make sure you pur brakekts 
df.describe()

cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]

viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
viz.hist()
plt.show()

plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='red')
plt.xlabel('ENGINESIZE')
plt.ylabel ('CO2EMISSIONS')
plt.show()


msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]
#note that tilde inversts the argument

plt.scatter(train.ENGINESIZE,train.CO2EMISSIONS,color = 'blue')
#note to access the particular column in the train set its '.'

plt.scatter(train.CYLINDERS,train.CO2EMISSIONS, color = 'red')

regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (train_x, train_y)

print('coefficient: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
#notice this is y=mx+c
plt.xlabel("Engine size")
plt.ylabel("Emission")

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.4f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_ , test_y) )







