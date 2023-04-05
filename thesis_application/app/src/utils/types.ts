export interface PlantPrediction {
  prediction: string,
  prediction_scores: number[],
}

export interface DiseasePrediction extends PlantPrediction {
  prediction_indices: number[],
}

export interface PredictionResponse {
  class_prediction: PlantPrediction,
  disease_prediction: DiseasePrediction,
}

export interface ChartPrediction {
  name: string,
  value: number,
}