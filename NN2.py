import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.python.keras.callbacks import History

fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (x_test, y_test) = fashion_mnist.load_data()

print(X_train_full.shape)
print(X_train_full.dtype)

X_valid, X_train = X_train_full[:5000]/255.0, X_train_full[5000:]/255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28,28]))
model.add(keras.layers.Dense(300, activation="relu"))
model.add(keras.layers.Dense(100, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax"))

print(model.summary())
#"binary_crossentropy"
#activation="sigmoid"
#model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])

#history = model.fit(X_train, y_train, epochs=30, validation_data=(X_valid, y_valid))
#print(history)


x = np.array([[1.0, 1.0, 1.0, 1.0, 1.0],
              [1.0, 1.0, 1.0, 1.0, 0.0],
              [1.0, 1.0, 1.0, 0.0, 0.0],
              [1.0, 1.0, 0.0, 0.0, 0.0],
              [1.0, 0.0, 0.0, 0.0, 0.0]])
y = np.array([[1.0],
              [0.8],
              [0.6],
              [0.5],
              [0.4]])

model2 = keras.models.Sequential()
model2.add(keras.layers.Flatten(input_shape=[5,1]))
model2.add(keras.layers.Dense(5, activation="sigmoid"))
model2.add(keras.layers.Dense(5, activation="sigmoid"))
model2.add(keras.layers.Dense(1, activation="sigmoid"))

model2.compile(loss="binary_crossentropy", optimizer="sgd", metrics=["accuracy"])
print(model2.summary())

asd = model2.fit(x,y,epochs=10000, validation_data=(x,y))