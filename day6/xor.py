#!/usr/bin/python3

#from
#https://blog.thoughtram.io/machine-learning/2016/11/02/understanding-XOR-with-keras-and-tensorlow.html

import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

# the four different states of the XOR gate
training_data = np.array([[0,0, 4],[0,1, 5],[1,0, 6],[1,1, 7]], "float32")

# the four expected results in the same order
target_data = np.array([[0],[1],[1],[0]], "float32")

model = Sequential()
model.add(Dense(16, input_dim=3, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])

model.fit(training_data, target_data, nb_epoch=200, verbose=2)

predictions= model.predict(training_data).round()
print(predictions)

predictions = model.predict(np.array([[0,0]], "float32")).round()
print(predictions)

predictions = model.predict(np.array([[1,0]], "float32")).round()
print(predictions)


