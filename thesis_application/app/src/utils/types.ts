export interface Prediction {
  prediction: string,
  prediction_scores: number[],
}

export interface PredictionResponse {
  class_prediction: Prediction,
  disease_prediction: Prediction,
}

export interface ChartPrediction {
  name: string,
  value: number,
}