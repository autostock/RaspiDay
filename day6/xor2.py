#!/usr/bin/python3

#from
#https://blog.thoughtram.io/machine-learning/2016/11/02/understanding-XOR-with-keras-and-tensorlow.html

#stop if accuracy reaches baseline
#https://stackoverflow.com/questions/53500047/stop-training-in-keras-when-accuracy-is-already-1-0

import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.callbacks import Callback

class TerminateOnBaseline(Callback):
    """Callback that terminates training when either acc or val_acc reaches a specified baseline
    """
    def __init__(self, monitor='acc', baseline=0.9):
        super(TerminateOnBaseline, self).__init__()
        self.monitor = monitor
        self.baseline = baseline

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        acc = logs.get(self.monitor)
        #print(self.monitor)
        #print(acc)
        #print(logs)
        if acc is not None:
            #print(self.baseline)
            if acc >= self.baseline:
                print('Epoch %d: Reached baseline %f>=%f, terminating training' % (epoch, acc, self.baseline))
                self.model.stop_training = True


# the four different states of the XOR gate
training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")

# the four expected results in the same order
target_data = np.array([[0],[1],[1],[0]], "float32")

print(training_data)
print(target_data)

model = Sequential()
model.add(Dense(16, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])

model.fit(training_data, target_data, callbacks = [TerminateOnBaseline(monitor='binary_accuracy', baseline=0.8)], nb_epoch=2000, verbose=0)

predictions= model.predict(training_data).round()
print(predictions)

predictions = model.predict(np.array([[0,0]], "float32")).round()
print(predictions)

predictions = model.predict(np.array([[1,0]], "float32")).round()
print(predictions)


