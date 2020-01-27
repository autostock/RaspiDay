#!/usr/bin/python3

#inspired from
#https://machinelearningmastery.com/regression-tutorial-keras-deep-learning-library-python/

#https://stackoverflow.com/questions/25614749/how-to-import-csv-file-as-numpy-array-in-python

#import pandas
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor



# load dataset
# tmp;hum;bmp;pm25_06;dow;pm25_12
# 6.5;83;1008;2;2;3
# -3.8;79;1023;13;2;19.5
# ...

inf=open('wetter.csv','r') 
X0 = np.genfromtxt (inf, delimiter=";", skip_header=1)
inf.close()



# Trainingsdaten generieren
xl=[]
yl=[]
trainingdata=len(X0)
for i in range(trainingdata):
    list=X0[i].tolist()
    xl.append([list[0], list[1], list[2], list[3], list[4]])
    yl.append([list[5]])

X=np.array(xl)
Y=np.array(yl)

print(X)
print(Y)

# create model
model = Sequential()
model.add(Dense(40, input_dim=5, kernel_initializer='normal', activation='relu'))
model.add(Dense(5, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))
# Compile model

model.compile(loss='mean_squared_error', optimizer='adam')


hist=model.fit(X, Y, epochs=2000, verbose=1)
loss=hist.history['loss']
lastloss=loss[len(loss)-1]

print('')
print('MSE=%f' % (lastloss))
print('pm25_06	pm25_12	learned pm25_12-pm25_06 learned-pm25_06')
predictions= model.predict(X)
for i in range(trainingdata):
    print(X[i, 3], Y[i, 0], predictions[i][0], Y[i, 0]-X[i, 3], predictions[i][0]-X[i, 3])


print('MSE=%f' % (lastloss))

C = np.array([[6.5, 83.0, 1008.0, 2.0, 2.0]]) # expected 3.0
predictions= model.predict(C)
print(predictions)





