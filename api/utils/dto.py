from pydantic import BaseModel


class Prediction(BaseModel):
    name: str
    prediction: float


class PredictionDTO(BaseModel):
    prediction: str
    prediction_scores: list[Prediction]


class PredictionResponse(BaseModel):
    class_prediction: PredictionDTO
    disease_prediction: PredictionDTO