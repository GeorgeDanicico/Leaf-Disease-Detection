from typing import Any

from fastapi import File
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from io import BytesIO
from PIL import Image

from utils.dto import Prediction
from utils.utils import get_plant_labels_dict_mtl, get_diseases_labels_dict_mtl, get_plant_labels_dict, \
    get_plant_labels_mtl, get_plant_labels, get_diseases_labels_mtl, get_diseases_labels, sort_predictions_by_name


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


def get_predicted_plant(predicted_output, model_type: str):
    if model_type == 'mtl':
        return get_plant_labels_mtl()[predicted_output]
    return get_plant_labels()[predicted_output]


def get_predicted_disease(predicted_output, model_type: str):
    if model_type == 'mtl':
        return get_diseases_labels_mtl()[predicted_output]
    return get_diseases_labels()[predicted_output]


def get_biggest_predictions(prediction, nr: int, model_type: str):
    prediction_indices = (-prediction).argsort()[0][:nr]
    result = []

    for index in prediction_indices:
        prediction_name = get_predicted_disease(index, model_type)
        result.append(Prediction(name=prediction_name, prediction=prediction[0][index]))

    print(f'here {result}')

    return result


def format_prediction1(numpy_array, model_type: str):
    return_list: list[Prediction] = []
    plant_labels = get_plant_labels()

    for i in range(numpy_array.shape[1]):
        return_list.append(Prediction(name=plant_labels[i], prediction=numpy_array[0][i]))

    return return_list


def predict_classes(model_type: str, image: Image) -> list[Any]:
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    prediction1, prediction2 = get_predictions(img_array, model_type)
    predicted_output1 = np.argmax(prediction1)
    predicted_output2 = np.argmax(prediction2)
    predicted_class_name1: str = get_predicted_plant(predicted_output1, model_type)
    predicted_class_name2: str = get_predicted_disease(predicted_output2, model_type)
    prediction1_values = format_prediction1(prediction1, model_type)
    prediction2_top_3 = get_biggest_predictions(prediction2, 3, model_type)

    return [predicted_class_name1, sort_predictions_by_name(prediction1_values), predicted_class_name2,
            sort_predictions_by_name(prediction2_top_3)]

