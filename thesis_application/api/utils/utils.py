from io import BytesIO

from PIL import Image

from utils.dto import Prediction


class PredictionUtils:
    @staticmethod
    def read_image_file(data) -> Image.Image:
        image = Image.open(BytesIO(data))
        image = image.resize((224, 224))
        print(image.size)
        return image

    @staticmethod
    def get_plant_labels_mtl() -> list[str]:
        return ['Tomato', 'Grape', 'Potato', 'Corn (maize)', 'Strawberry', 'Apple']

    @staticmethod
    def get_diseases_labels_mtl() -> list[str]:
        return ['Tomato Late blight', 'Tomato healthy', 'Grape healthy',
                'Potato healthy', 'Corn Northern Leaf Blight', 'Tomato Early blight',
                'Tomato Septoria leaf spot', 'Strawberry Leaf scorch', 'Apple scab',
                'Tomato Yellow Leaf Curl Virus', 'Tomato Bacterial spot', 'Apple Black rot',
                'Apple Cedar rust', 'Tomato Target Spot', 'Grape Leaf blight (Isariopsis Leaf Spot)',
                'Potato Late blight', 'Tomato mosaic virus', 'Strawberry healthy',
                'Apple healthy', 'Grape Black rot', 'Potato Early blight',
                'Corn Common rust ', 'Grape Esca (Black Measles)',
                'Tomato Leaf Mold', 'Tomato Spider mites', 'Corn healthy']

    @staticmethod
    def get_plant_labels_dict_mtl() -> dict[str, int]:
        return {'Tomato': 0, 'Grape': 1, 'Potato': 2, 'Corn': 3, 'Strawberry': 4, 'Apple': 5}

    @staticmethod
    def get_diseases_labels_dict_mtl() -> dict[str, int]:
        return {
            'Tomato Late blight': 0, 'Tomato healthy': 1, 'Grape healthy': 2, 'Potato healthy': 3,
            'Corn Northern Leaf Blight': 4, 'Tomato Early blight': 5, 'Tomato Septoria leaf spot': 6,
            'Strawberry Leaf scorch': 7, 'Apple scab': 8, 'Tomato Yellow Leaf Curl Virus': 9,
            'Tomato Bacterial spot': 10, 'Apple Black rot': 11, 'Apple Cedar rust': 12,
            'Tomato Target Spot': 13, 'Grape Leaf blight (Isariopsis Leaf Spot)': 14, 'Potato Late blight': 15,
            'Tomato mosaic virus': 16, 'Strawberry healthy': 17, 'Apple healthy': 18,
            'Grape Black rot': 19,
            'Potato Early blight': 20, 'Corn (maize) Common rust ': 21, 'Grape Esca (Black Measles)': 22,
            'Tomato Leaf Mold': 23, 'Tomato Spider mites': 24, 'Corn healthy': 25
        }

    @staticmethod
    def get_plant_labels() -> list[str]:
        return ['Apple', 'Corn', 'Grape', 'Potato', 'Strawberry', 'Tomato']

    @staticmethod
    def get_diseases_labels() -> list[str]:
        return ['Apple scab', 'Apple Black rot', 'Apple Cedar rust', 'Apple healthy',
                'Corn Common rust ', 'Corn Northern Leaf Blight', 'Corn healthy',
                'Grape Black rot', 'Grape Esca (Black Measles)', 'Grape Leaf blight (Isariopsis Leaf Spot)',
                'Grape healthy', 'Potato Early blight', 'Potato Late blight', 'Potato healthy',
                'Strawberry Leaf scorch', 'Strawberry healthy', 'Tomato Bacterial spot',
                'Tomato Early blight', 'Tomato Late blight', 'Tomato Leaf Mold',
                'Tomato Septoria leaf spot', 'Tomato Spider',
                'Tomato Target Spot', 'Tomato Yellow Leaf Curl Virus', 'Tomato mosaic virus',
                'Tomato healthy']

    @staticmethod
    def get_plant_labels_dict() -> dict[str, int]:
        return {'Apple': 0, 'Corn': 1, 'Grape': 2, 'Potato': 3, 'Strawberry': 4, 'Tomato': 5}

    @staticmethod
    def get_diseases_labels_dict() -> dict[str, int]:
        return {'Apple scab': 0, 'Apple Black rot': 1, 'Apple Cedar rust': 2,
                'Apple healthy': 3, 'Corn Common rust ': 4, 'Corn Northern Leaf Blight': 5,
                'Corn healthy': 6, 'Grape Black rot': 7, 'Grape Esca (Black Measles)': 8,
                'Grape Leaf blight (Isariopsis Leaf Spot)': 9, 'Grape healthy': 10, 'Potato Early blight': 11,
                'Potato Late blight': 12, 'Potato healthy': 13, 'Strawberry Leaf scorch': 14,
                'Strawberry healthy': 15, 'Tomato Bacterial spot': 16, 'Tomato Early blight': 17,
                'Tomato Late blight': 18, 'Tomato Leaf Mold': 19, 'Tomato Septoria leaf spot': 20,
                'Tomato Spider mites': 21, 'Tomato Target Spot': 22,
                'Tomato Yellow Leaf Curl Virus': 23, 'Tomato mosaic virus': 24,
                'Tomato healthy': 25}

    @staticmethod
    def sort_predictions_by_name(predictions: list[Prediction]):
        predictions.sort(key=lambda x: x.name)
        return predictions
