# -*- coding: utf-8 -*-
"""deep_learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CkQC8EBOwleGjZbGnur-JkGT-uVmoxcc
"""

import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
import tensorflow_datasets as tfds

"""# **Sample Equation Data**

## load, clean and prepare data
"""

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

"""## build the model"""

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
print(model.summary())

"""## train the model - fit the training data"""

model.fit(xs, ys, epochs=1000, verbose=0)

"""## evaluate the model"""

print(model.predict([10.0]))

"""# **MNIST Dataset**

## load, clean and prepare data
"""

#(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train, y_train = tfds.as_numpy(tfds.load('mnist', as_supervised=True, split='train', batch_size=-1))
x_test, y_test = tfds.as_numpy(tfds.load('mnist', as_supervised=True, split='test', batch_size=-1))

x_train, x_test = x_train / 255.0, x_test / 255.0
print(x_train.shape)
print(x_test.shape)

"""## build the model"""

mnist_model = keras.Sequential([
                                keras.layers.Flatten(input_shape=(28,28,1)),
                                #keras.layers.Dense(128, activation='relu'),
                                keras.layers.Dense(10, activation='softmax')
                                ])
mnist_model.compile(
    optimizer='SGD',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
    )
print(mnist_model.summary())

"""## train the model - fit the training data"""

mnist_model.fit(x_train, y_train, epochs=1, batch_size=1)

"""## evaluate the model"""

mnist_model.evaluate(x_test,y_test,batch_size=1)

"""# **Boston Housing Price Dataset**

## load, clean and prepare data
"""

(x_train, y_train), (x_test, y_test) = keras.datasets.boston_housing.load_data()
print(x_train.shape)

"""## build the model"""

house_model = keras.Sequential([
                                keras.layers.Dense(units=64, input_shape=[x_train.shape[1]], activation='relu'),
                                keras.layers.Dense(units=64, activation='relu'),
                                keras.layers.Dense(units=1, activation='linear')
                                ])
house_model.compile(optimizer='RMSprop', loss='mse', metrics=['mse', 'mae'])
print(house_model.summary())

"""## train the model - fit the training data"""

house_model.fit(x_train, y_train, epochs=1000, verbose=0)

"""## evaluate the model"""

house_model.evaluate(x_test,y_test)

y_test_pred = house_model.predict(x_test).flatten()

f, ax = plt.subplots(figsize = (15,10))
plt.rc('font', size=18)
ax.set_xlabel("Original Price")
ax.set_ylabel("Predicted Price")
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(colors='white')
plt.scatter(x=y_test, y=y_test_pred, color='blue')
z = np.polyfit(y_test, y_test_pred, 1)
p = np.poly1d(z)
plt.plot(y_test,p(y_test),'r')