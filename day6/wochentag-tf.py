#!/usr/bin/python3

#inspired from
#https://machinelearningmastery.com/regression-tutorial-keras-deep-learning-library-python/

from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.utils import to_categorical
from keras.losses import categorical_crossentropy
from keras.wrappers.scikit_learn import KerasRegressor
import numpy as np
import random

inf=open('2020dow.csv','r')  # Tag,Monat
X0 = np.genfromtxt (inf, delimiter=",")
inf.close()

print(X0)


# Trainingsdaten generieren
xl=[]
yl=[]
trainingdata=len(X0)
for i in range(0, trainingdata):
    list=X0[i].tolist()
    xl.append([list[0], list[1]])
    #v=np.zeros(7)
    #v[round(list[2])]=1
    #yl.append(v)
    yl.append([list[2]])

X=np.array(xl)
Y=np.array(yl)
Y= to_categorical(yl, 7)


print(X[24])
print(Y[24])

#'''

# create model
model = Sequential()
model.add(Dense(20, input_dim=2, activation='relu'))
model.add(Dense(70, activation='softmax'))
model.add(Dense(10, activation='relu'))
#model.add(Dense(1, kernel_initializer='normal'))
model.add(Dropout(rate=0.5))
model.add(Dense(7, activation='softmax'))

# Compile model
model.compile(loss=categorical_crossentropy, optimizer='adam')

model.fit(X, Y, batch_size=100, epochs=1000, verbose=2)

C = np.array([[1, 24.]])  # 24.Januar
predictions= model.predict(C)
print(predictions)

C = np.array([[1, 25.]])  # 25.Januar
predictions= model.predict(C)
print(predictions)

C = np.array([[1, 26.]])  # 25.Januar
predictions= model.predict(C)
print(predictions)

#'''
