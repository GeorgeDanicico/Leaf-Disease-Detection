from typing import Any
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np

from utils.dto import Prediction
from utils.utils import PredictionUtils


class PredictionService:
    def __init__(self, model_type: str, image):
        self.__model_type = model_type
        self.__image = self.__load_image(image)

    @staticmethod
    def __load_image(image):
        img = PredictionUtils.read_image_file(image)
        img_array = img_to_array(img)
        return np.expand_dims(img_array, axis=0)

    def __load_ml_models(self) -> Any:
        if self.__model_type == 'mtl':
            return load_model('./ml_models/mtl.h5')
        if self.__model_type == 'simple_cnn':
            return load_model('./ml_models/simple_plant.h5'), load_model('./ml_models/simple_disease.h5')
        if self.__model_type == 'inception':
            return load_model('./ml_models/inception_plant.h5'), load_model('./ml_models/inception_disease.h5')

    def __get_predictions(self):
        if self.__model_type == 'mtl':
            model = self.__load_ml_models()
            return model.predict(self.__image)

        plant_model, disease_model = self.__load_ml_models()
        return plant_model.predict(self.__image), disease_model.predict(self.__image)

    def __get_predicted_plant(self, predicted_output):
        return PredictionUtils.get_plant_labels()[predicted_output]

    def __get_predicted_disease(self, predicted_output):
        return PredictionUtils.get_diseases_labels()[predicted_output]

    def __get_biggest_predictions(self, prediction, nr: int):
        prediction_indices = (-prediction).argsort()[0][:nr]
        result = []

        for index in prediction_indices:
            prediction_name = self.__get_predicted_disease(index)
            result.append(Prediction(name=prediction_name, prediction=prediction[0][index]))

        return result

    def __format_prediction(self, numpy_array):
        return_list: list[Prediction] = []
        plant_labels = PredictionUtils.get_plant_labels()

        for i in range(numpy_array.shape[1]):
            return_list.append(Prediction(name=plant_labels[i], prediction=numpy_array[0][i]))

        return return_list

    def predict_classes(self) -> list[Any]:
        prediction1, prediction2 = self.__get_predictions()
        predicted_output1 = np.argmax(prediction1)
        predicted_output2 = np.argmax(prediction2)
        predicted_class_name1: str = self.__get_predicted_plant(predicted_output1)
        predicted_class_name2: str = self.__get_predicted_disease(predicted_output2)
        prediction1_values = self.__format_prediction(prediction1)
        prediction2_top_3 = self.__get_biggest_predictions(prediction2, 3)

        print(prediction1_values)

        return [predicted_class_name1, PredictionUtils.sort_predictions_by_name(prediction1_values),
                predicted_class_name2, PredictionUtils.sort_predictions_by_name(prediction2_top_3)]
