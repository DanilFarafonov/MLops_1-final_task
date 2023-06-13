import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import absl.logging


absl.logging.set_verbosity(absl.logging.ERROR)


x_train = pd.read_csv('data/x_train.csv', index_col=0)
y_train = pd.read_csv('data/y_train.csv', index_col=0)


model = Sequential()
model.add(Dense(800, input_dim=784, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())


model.fit(x_train, y_train,
          batch_size=200,
          epochs=25,
          verbose=1)


model.save('model_fashion_mnist')
print('Model training and saving successfully completed')
