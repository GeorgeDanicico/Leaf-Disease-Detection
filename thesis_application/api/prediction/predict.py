from fastapi import File
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from io import BytesIO
from PIL import Image

plant_labels: list[str] = ['Tomato', 'Grape', 'Potato', 'Corn_(maize)', 'Strawberry', 'Apple']
diseases_labels: list[str] = ['Tomato___Late_blight', 'Tomato___healthy', 'Grape___healthy',
                   'Potato___healthy', 'Corn_(maize)___Northern_Leaf_Blight', 'Tomato___Early_blight',
                   'Tomato___Septoria_leaf_spot', 'Strawberry___Leaf_scorch', 'Apple___Apple_scab',
                   'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Bacterial_spot', 'Apple___Black_rot',
                   'Apple___Cedar_apple_rust', 'Tomato___Target_Spot', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                   'Potato___Late_blight', 'Tomato___Tomato_mosaic_virus', 'Strawberry___healthy',
                   'Apple___healthy', 'Grape___Black_rot', 'Potato___Early_blight',
                   'Corn_(maize)___Common_rust_', 'Grape___Esca_(Black_Measles)',
                   'Tomato___Leaf_Mold', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Corn_(maize)___healthy']

diseases_labels_dict: dict = {'Tomato___Late_blight': 0, 'Tomato___healthy': 1, 'Grape___healthy': 2, 'Potato___healthy': 3, 'Corn_(maize)___Northern_Leaf_Blight': 4, 'Tomato___Early_blight': 5, 'Tomato___Septoria_leaf_spot': 6, 'Strawberry___Leaf_scorch': 7, 'Apple___Apple_scab': 8, 'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 9, 'Tomato___Bacterial_spot': 10, 'Apple___Black_rot': 11, 'Apple___Cedar_apple_rust': 12, 'Tomato___Target_Spot': 13, 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 14, 'Potato___Late_blight': 15, 'Tomato___Tomato_mosaic_virus': 16, 'Strawberry___healthy': 17, 'Apple___healthy': 18, 'Grape___Black_rot': 19, 'Potato___Early_blight': 20, 'Corn_(maize)___Common_rust_': 21, 'Grape___Esca_(Black_Measles)': 22, 'Tomato___Leaf_Mold': 23, 'Tomato___Spider_mites Two-spotted_spider_mite': 24, 'Corn_(maize)___healthy': 25}
plant_labels_dict: dict = {'Tomato': 0, 'Grape': 1, 'Potato': 2, 'Corn_(maize)': 3, 'Strawberry': 4, 'Apple': 5}

def read_imagefile(data) -> Image.Image:
    image = Image.open(BytesIO(data))
    image = image.resize((224, 224))
    print(image.size)
    return image


def predict_classes(image: Image) -> list[str]:
    model = load_model('./prediction/model.h5')
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    prediction1, prediction2 = model.predict(img_array)
    predicted_output1 = np.argmax(prediction1)
    predicted_output2 = np.argmax(prediction2)
    predicted_class_name1: str = list(plant_labels_dict.keys())[predicted_output1]
    predicted_class_name2: str = list(diseases_labels_dict.keys())[predicted_output2]

    print(f'The predicted output for image is: {predicted_class_name1} and {predicted_class_name2}')

    return [predicted_class_name1, predicted_class_name2]
