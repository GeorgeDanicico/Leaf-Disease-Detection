import { DISEASES_LABELS, PLANT_LABELS } from "./helper";
import { ChartPrediction, PredictionMap, PredictionResponse } from "./types";

// export const generateData = (prediction: PredictionResponse, type: string) => {

//   let scores: PredictionMap[];
//   let labels: string[];
//   let data: ChartPrediction[] = [];
//   if (type === "class") {
//     scores = prediction.class_prediction.prediction_scores;
//     labels = PLANT_LABELS;
//   } else {
//     scores = prediction.disease_prediction.prediction_scores;
//     labels = []

//     prediction.disease_prediction.prediction_indices.forEach(index => labels.push(DISEASES_LABELS[index]));
//   }
  
//   for (var i = 0; i < scores.length; i++) {
//     var obj: ChartPrediction = {name: labels[i],
//        value: scores[i]};
//     data.push(obj);
//   }

//   return data;
// }