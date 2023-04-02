from fastapi import FastAPI, UploadFile
from fastapi.params import File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from prediction.predict import predict_classes, read_imagefile
from pydantic import BaseModel

app = FastAPI()

class Predictions(BaseModel):
    class_prediction: str
    disease_prediction: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
)

@app.post("/predict/")
async def predict_disease(file: UploadFile = File(...)):
    pred = predict_classes(read_imagefile(await file.read()))
    json_response = jsonable_encoder(Predictions(class_prediction=pred[0], disease_prediction=pred[1]))
    return JSONResponse(content=json_response)
