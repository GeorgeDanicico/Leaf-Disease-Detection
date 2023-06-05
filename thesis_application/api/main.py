from typing import Annotated

from fastapi import FastAPI, UploadFile, Form
from fastapi.params import File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from prediction.predict import PredictionService

from utils.dto import PredictionResponse, PredictionDTO

app = FastAPI()

origins = ["*"]  # Replace with your own list of allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict/")
async def predict_disease(type: Annotated[str, Form()], file: UploadFile = File(...)):
    image = await file.read()
    prediction_service = PredictionService(type, image)
    pred = prediction_service.predict_classes()

    print(f'Received type from fe: {type}')
    plant_prediction = PredictionDTO(prediction=pred[0], prediction_scores=pred[1])
    disease_prediction = PredictionDTO(prediction=pred[2], prediction_scores=pred[3])

    json_response = jsonable_encoder(PredictionResponse(class_prediction=plant_prediction, disease_prediction=disease_prediction))
    return JSONResponse(content=json_response)
