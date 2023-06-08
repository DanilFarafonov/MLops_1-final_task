from fastapi import FastAPI, UploadFile
from PIL import Image
import tensorflow as tf
import io
import os
import numpy as np


def get_best_model():
    models = os.listdir('models/')
    models_dict = dict()

    for model in models:
        score = float(model.split('_')[1])
        models_dict[score] = model

    scores = list(models_dict.keys())
    top_score = max(scores)
    top_model_name = models_dict[top_score]
    top_model = tf.keras.models.load_model('models/' + top_model_name)
    return top_model


app = FastAPI()
model = get_best_model()


cloth_types = {0: 'Футболка', 1: 'Брюки', 2: 'Свитер', 3: 'Платье', 4: 'Пальто',
               5: 'Туфли', 6: 'Рубашка', 7: 'Кроссовки', 8: 'Сумка', 9: 'Ботинки'}


@app.get("/")
def root():
    """
    Test function
    :return: greetings
    """
    return {"message": "Сервис для классификации одежды по изображению."
                       "\nНейронная сеть обучена на датасете fashion_mnist."}


@app.post("/predict/")
def predict(photo: UploadFile):
    """
    Predicts the type of clothing from a given picture
    :param photo: UploadFile
    :return: type of clothing
    """
    file_bytes = photo.file.read()
    image = Image.open(io.BytesIO(file_bytes))
    pixels = np.empty((28, 28))

    for i in range(28):
        for j in range(28):
            current_pixel = image.getpixel((i, j)) / 255
            pixels[j][i] = current_pixel

    pixels = pixels.reshape(1, 784)
    predictions = model.predict(pixels)
    cloth_number = np.argmax(predictions, axis=1)[0]
    cloth_class = cloth_types[cloth_number]

    return {'message': cloth_class}
