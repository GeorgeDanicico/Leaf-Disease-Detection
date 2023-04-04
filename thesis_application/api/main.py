from typing import Annotated

from fastapi import FastAPI, UploadFile, Form
from fastapi.params import File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from prediction.predict import predict_classes, read_image_file
from pydantic import BaseModel

app = FastAPI()


class Prediction(BaseModel):
    prediction: str
    prediction_scores: list[float]


class PredictionDTO(BaseModel):
    class_prediction: Prediction
    disease_prediction: Prediction

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
)


@app.post("/predict/")
async def predict_disease(type: Annotated[str, Form()], file: UploadFile = File(...)):
    image = await file.read()
    pred = predict_classes('mtl', read_image_file(image))

    print(f'Received type from fe: {type}')
    plant_prediction = Prediction(prediction=pred[0], prediction_scores=pred[1])
    disease_prediction = Prediction(prediction=pred[2], prediction_scores=pred[3])

    json_response = jsonable_encoder(PredictionDTO(class_prediction=plant_prediction, disease_prediction=disease_prediction))
    return JSONResponse(content=json_response)
