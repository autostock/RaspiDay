#!/usr/bin/python3

#inspired from
#https://machinelearningmastery.com/regression-tutorial-keras-deep-learning-library-python/

import numpy as np
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.wrappers.scikit_learn import KerasRegressor
#from sklearn.model_selection import cross_val_score
#from sklearn.model_selection import KFold
#from sklearn.preprocessing import StandardScaler
#from sklearn.pipeline import Pipeline


# load dataset
#dataframe = pandas.read_csv("regression1.csv", delim_whitespace=True, header=None)
#dataset = dataframe.values
# split into input (X) and output (Y) variables
#DX = dataset[:,0:1]
#DY = dataset[:,1]


def f(x):
    return math.sin(x)

X=np.zeros((100, 1), "float32")
Y=np.zeros((100, 1), "float32")
for i in range(100):
    x=i/5.0-5.0
    X[i, 0]=x
    Y[i, 0]=f(x)


#normalize to [0, 1]
#X=X/100
#Y=Y/48712

print(X)
print(Y)

epochs=10000
bestloss=math.inf
best=None
i=0
while i<20:
    # create model
    model = Sequential()
    model.add(Dense(10, input_dim=1, kernel_initializer='normal', activation='relu'))
    model.add(Dense(5, kernel_initializer='normal', activation='relu'))
    #model.add(Dropout(rate=0.5)) # hier immer deutlich schlechtere Resultate
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')

    #hist=model.fit(X, Y, callbacks = [TerminateOnBaseline(monitor='loss', baseline=limit)], epochs=10000, verbose=0)
    hist=model.fit(X, Y, epochs=epochs, verbose=0)

    loss=hist.history['loss']
    #print(loss)
    tmp=loss[len(loss)-1]
    print('%d\tbestMSE=%f\tactual=%f' % (i, bestloss, tmp))
    if tmp<bestloss:
        bestloss=tmp
        best=model
    i+=1

print('trying harder with best so far ...')

bestWeights = best.get_weights()
i=0
while i>=0:
    hist=best.fit(X, Y, epochs=epochs, verbose=0)
    loss=hist.history['loss']
    #print(loss)
    tmp=loss[len(loss)-1]
    print('%d\tbestMSE=%f\tactual=%f' % (i, bestloss, tmp))
    if tmp>=bestloss:
        break
    bestloss=tmp
    bestWeights = best.get_weights()
    i+=1

best.set_weights(bestWeights)

print('')
print('MSE=%f' % (bestloss))
print('trained	target	learned')
predictions= best.predict(X)
for i in range(100):
    print(X[i, 0], Y[i, 0], predictions[i][0])


#test
x=1.3
y=f(x)
predictions= best.predict([[x]])
print('')
print('test:')
print('x=%f expected=%f actual=%s' % (x, y, predictions[0][0]))


