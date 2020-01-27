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

def flatten(m, d):
    v=np.zeros(12+31)
    v[   round(m-1)]=1
    v[12+round(d-1)]=1
    return v

def prediction(m, d):
    p= model.predict(np.array([flatten(m, d)]))[0]
    max=0
    idx=0
    for i in range(0, 7):
        if max<p[i]:
            idx=i
            max=p[i]
    v=np.zeros(7)
    v[idx]=1
    return v


inf=open('2020dow.csv','r')  # Monat, Tag, dow
X0 = np.genfromtxt (inf, delimiter=",")
inf.close()

print(X0)

# Trainingsdaten generieren
xl=[]
yl=[]
trainingdata=len(X0)
for i in range(0, trainingdata):
    list=X0[i].tolist()
    xl.append(flatten(list[0], list[1]))
    yl.append([list[2]])

X=np.array(xl)
Y=np.array(yl)
Y= to_categorical(yl, 7)

# create model
model = Sequential()
model.add(Dense(20, input_dim=12+31, activation='relu'))
#model.add(Dense(70, activation='softmax'))
#model.add(Dense(5, activation='relu'))
#model.add(Dense(1, kernel_initializer='normal'))
#model.add(Dropout(rate=0.5))
model.add(Dense(7, activation='softmax'))

# Compile model
model.compile(loss=categorical_crossentropy, optimizer='adam')

#model.fit(X, Y, batch_size=100, epochs=1000, verbose=2)
model.fit(X, Y, epochs=1000, verbose=0)

error=0
for i in range(0, len(X)):
    list=X0[i].tolist()
    m=list[0]
    d=list[1]
    y=prediction(m, d)
    if (y!=Y[i]).any():
        print('problem %d %d:\texpected=%s; actual=%s' % (m, d, Y[i], y))
        error+=1

print('%d errors in %d training datas' % (error, len(X)))


print('%d.%d actual is %s' % (25, 1, prediction(1, 25)))   # 25.Januar

