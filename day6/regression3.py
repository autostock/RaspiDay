#!/usr/bin/python3

#inspired from
#https://machinelearningmastery.com/regression-tutorial-keras-deep-learning-library-python/
#
#https://github.com/keras-team/keras/issues/341

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
    if x<=1:
        return x
    x0=0
    x1=1
    for i in range(x-1):
        x2=x0+x1
        x0=x1
        x1=x2
    return 1.0*x2

X=np.zeros((100, 1), "float32")
Y=np.zeros((100, 1), "float32")
for i in range(100):
    x=i
    X[i, 0]=x
    Y[i, 0]=f(x)

ysacle=2.4e+16
#normalize to some sensefull intervall 
#X=X/100
Y=Y/ysacle

print(X)
print(Y)

epochs=10000
limit=10.0
bestloss=math.inf
best=None
i=0
while i<20 and bestloss>limit:
    # create model
    model = Sequential()
    model.add(Dense(10, input_dim=1, kernel_initializer='normal', activation='relu'))
    model.add(Dense(5, kernel_initializer='normal', activation='relu'))
    #model.add(Dropout(rate=0.5)) # hierdurch immer deutlich schlechtere Resultate
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
print('MSE = %f' % (bestloss))
predictions= best.predict(X)
for i in range(100):
    print(X[i], (ysacle*Y[i]).round(), (ysacle*predictions[i][0]).round())


#test
x=103
y=f(x)
predictions= best.predict([[x]])
print('test:')
print('x=%f expected=%f actual=%s' % (x, y, (ysacle*predictions[0][0]).round()))


