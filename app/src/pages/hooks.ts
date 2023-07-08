import { useCallback } from "react";
import { ChartPrediction, PredictionResponse } from "../utils/types";

const generateData = (prediction: PredictionResponse, type: string) => {

  let scores: number[] = [];
  let labels: string[] = [];
  let data: ChartPrediction[] = [];
  let responseScores = []

  if (type === "class") {
    responseScores = prediction.class_prediction.prediction_scores;
  } else {
    responseScores = prediction.disease_prediction.prediction_scores;
  }

  responseScores.forEach(prediction => {
    labels.push(prediction.name)
    scores.push(prediction.prediction)
  })
  
  for (var i = 0; i < scores.length; i++) {
    var obj: ChartPrediction = {name: labels[i],
       value: scores[i]};
    data.push(obj);
  }

  return data;
}

export const useGenerateData = () => {
  return useCallback((prediction: PredictionResponse, type: string) => generateData(prediction, type), [])
};