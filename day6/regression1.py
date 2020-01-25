#!/usr/bin/python3

#inspired from
#https://machinelearningmastery.com/regression-tutorial-keras-deep-learning-library-python/

import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
#from sklearn.model_selection import cross_val_score
#from sklearn.model_selection import KFold
#from sklearn.preprocessing import StandardScaler
#from sklearn.pipeline import Pipeline



# load dataset
dataframe = pandas.read_csv("regression1.csv", delim_whitespace=True, header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
DX = dataset[:,0:1]
DY = dataset[:,1]

X=[]
Y=[[]]
for i in range(100):
    x=i/5.0-5.0
    X.append(x)
    Ye=5*x*x - 3*x+4
    Y[0].append(Ye)

#normalize to [0, 1]
X=X#/100
Y=Y#/48712

print(X)
print(DX)
print(Y)

x=20.0
print(5*x*x - 3*x+4)


# create model
model = Sequential()
model.add(Dense(10, input_dim=1, kernel_initializer='normal', activation='relu'))
model.add(Dense(5, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))
# Compile model
model.compile(loss='mean_squared_error', optimizer='adam')


model.fit(X, Y, nb_epoch=20000, verbose=0)

predictions= model.predict(X)
print(predictions)

for i in range(100):
    print(X[i], Y[i], predictions[i][0])


predictions= model.predict([[3.5]])
print(predictions)
predictions= model.predict([[20.0]])
print(predictions)


