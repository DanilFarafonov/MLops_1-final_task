from fastapi import FastAPI, UploadFile
from PIL import Image
from tensorflow import keras
import io
import os


def get_best_model():
    models = os.listdir('models/')
    models_dict = dict()

    for model in models:
        score = float(model.split('_')[1])
        models_dict[score] = model

    scores = list(models_dict.keys())
    top_score = max(scores)
    top_model_name = models_dict[top_score]
    top_model = keras.models.load_model(top_model_name)
    return top_model


app = FastAPI()
model = get_best_model()


@app.get("/")
def root():
    """
    Test function
    :return: greetings
    """
    return {"message": "Сервис для классификации одежды по изображению."
                       "\nНейнонная сеть обучена на датасете fashion_mnist."}


@app.post("/predict/")
def predict(photo: UploadFile):
    """
    Predicts the type of clothing from a given picture
    :param photo: UploadFile
    :return: type of clothing
    """
    file_bytes = photo.file.read()
    image = Image.open(io.BytesIO(file_bytes))

    return {}
