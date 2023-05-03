export interface PredictionMap {
  name: string,
  prediction: number,
}

export interface PredictionDTO {
  prediction: string,
  prediction_scores: PredictionMap[],
}

export interface PredictionResponse {
  class_prediction: PredictionDTO,
  disease_prediction: PredictionDTO,
}

export interface ChartPrediction {
  name: string,
  value: number,
}