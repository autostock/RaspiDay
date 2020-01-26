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
#dataframe = pandas.read_csv("regression1.csv", delim_whitespace=True, header=None)
#dataset = dataframe.values
# split into input (X) and output (Y) variables
#DX = dataset[:,0:1]
#DY = dataset[:,1]


def f(x):
    return 5*x*x - 3*x+4

X=[]
Y=[]
for i in range(100):
    x=i
    X.append(x)
    Y.append(f(x))

#normalize to [0, 1]
#X=X/100
#Y=Y/48712

print(X)
print(Y)


limit=10.0
bestloss=1000000.0
best=None
while bestloss>limit:
    # create model
    model = Sequential()
    model.add(Dense(10, input_dim=1, kernel_initializer='normal', activation='relu'))
    model.add(Dense(5, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')

    #hist=model.fit(X, Y, callbacks = [TerminateOnBaseline(monitor='loss', baseline=limit)], epochs=10000, verbose=0)
    hist=model.fit(X, Y, epochs=10000, verbose=0)

    loss=hist.history['loss']
    #print(loss)
    tmp=loss[len(loss)-1]
    print(tmp)
    if tmp<bestloss:
        bestloss=tmp
        best=model

print(bestloss)

predictions= best.predict(X)
for i in range(100):
    print(X[i], Y[i], predictions[i][0])


#test
x=20.0
y=f(x)
predictions= best.predict([[x]])
print('')
print('x=%f expected=%f actual=%s' % (x, y, predictions[0][0]))


