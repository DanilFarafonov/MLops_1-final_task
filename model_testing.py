import pandas as pd
import tensorflow as tf


x_test = pd.read_csv('data/x_test.csv', index_col=0)
y_test = pd.read_csv('data/y_test.csv', index_col=0)


model = tf.keras.models.load_model('model_fashion_mnist')


score = model.evaluate(x_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])