from typing import Any

from fastapi import File
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from io import BytesIO
from PIL import Image

from utils.utils import get_plant_labels_dict, get_diseases_labels_dict


def read_image_file(data) -> Image.Image:
    image = Image.open(BytesIO(data))
    image = image.resize((224, 224))
    print(image.size)
    return image


def load_ml_models(model_type: str) -> Any:
    if model_type == 'mtl':
        return load_model('./ml_models/mtl.h5')
    if model_type == 'simple_cnn':
        return load_model('./ml_models/simple_plant.h5'), load_model('./ml_models/simple_disease.h5')
    if model_type == 'inception':
        return load_model('./ml_models/inception_plant.h5'), load_model('./ml_models/inception_disease.h5')


def numpy_to_array(numpy_array) -> list[float]:
    return_list: list[float] = []
    for i in range(numpy_array.shape[1]):
        return_list.append(numpy_array[0][i])

    return return_list


def get_predictions(img_array, model_type: str):
    if model_type == 'mtl':
        model = load_ml_models(model_type)
        return model.predict(img_array)

    plant_model, disease_model = load_ml_models(model_type)
    return plant_model.predict(img_array), disease_model.predict(img_array)


def predict_classes(model_type: str, image: Image) -> list[Any]:
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    prediction1, prediction2 = get_predictions(img_array, model_type)

    predicted_output1 = np.argmax(prediction1)
    predicted_output2 = np.argmax(prediction2)
    predicted_class_name1: str = list(get_plant_labels_dict().keys())[predicted_output1]
    predicted_class_name2: str = list(get_diseases_labels_dict().keys())[predicted_output2]

    print(f'The predicted output for image is: {predicted_class_name1} and {predicted_class_name2}')

    return [predicted_class_name1, numpy_to_array(prediction1), predicted_class_name2, numpy_to_array(prediction2)]
