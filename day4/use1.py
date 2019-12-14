#!/usr/bin/env python
# coding: utf-8

from keras.models import load_model
import numpy as np, imageio 

model=load_model('./myWeights.hdf5')

im = imageio.imread('./dig5.png')
pixim = np.empty([1,28,28,1])   
for i in range(0,28):
    for j in range(0,28):
        pixim[0][i][j][0] = im[i][j]/255
        
N=1        
font_labels = [5]
probabilities = model.predict(pixim, steps=1)
predicted_labels = np.argmax(probabilities, axis=1)
print(predicted_labels)
print(probabilities)
