def get_plant_labels() -> list[str]:
    return ['Tomato', 'Grape', 'Potato', 'Corn_(maize)', 'Strawberry', 'Apple']


def get_diseases_labels() -> list[str]:
    return ['Tomato___Late_blight', 'Tomato___healthy', 'Grape___healthy',
            'Potato___healthy', 'Corn_(maize)___Northern_Leaf_Blight', 'Tomato___Early_blight',
            'Tomato___Septoria_leaf_spot', 'Strawberry___Leaf_scorch', 'Apple___Apple_scab',
            'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Bacterial_spot', 'Apple___Black_rot',
            'Apple___Cedar_apple_rust', 'Tomato___Target_Spot', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
            'Potato___Late_blight', 'Tomato___Tomato_mosaic_virus', 'Strawberry___healthy',
            'Apple___healthy', 'Grape___Black_rot', 'Potato___Early_blight',
            'Corn_(maize)___Common_rust_', 'Grape___Esca_(Black_Measles)',
            'Tomato___Leaf_Mold', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Corn_(maize)___healthy']


def get_plant_labels_dict() -> dict[str, int]:
    return {'Tomato': 0, 'Grape': 1, 'Potato': 2, 'Corn_(maize)': 3, 'Strawberry': 4, 'Apple': 5}


def get_diseases_labels_dict() -> dict[str, int]:
    return {
        'Tomato___Late_blight': 0, 'Tomato___healthy': 1, 'Grape___healthy': 2, 'Potato___healthy': 3,
        'Corn_(maize)___Northern_Leaf_Blight': 4, 'Tomato___Early_blight': 5, 'Tomato___Septoria_leaf_spot': 6,
        'Strawberry___Leaf_scorch': 7, 'Apple___Apple_scab': 8, 'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 9,
        'Tomato___Bacterial_spot': 10, 'Apple___Black_rot': 11, 'Apple___Cedar_apple_rust': 12,
        'Tomato___Target_Spot': 13, 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 14, 'Potato___Late_blight': 15,
        'Tomato___Tomato_mosaic_virus': 16, 'Strawberry___healthy': 17, 'Apple___healthy': 18, 'Grape___Black_rot': 19,
        'Potato___Early_blight': 20, 'Corn_(maize)___Common_rust_': 21, 'Grape___Esca_(Black_Measles)': 22,
        'Tomato___Leaf_Mold': 23, 'Tomato___Spider_mites Two-spotted_spider_mite': 24, 'Corn_(maize)___healthy': 25
    }
