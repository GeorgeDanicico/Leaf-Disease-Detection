import React, { useState } from 'react';
import { Button, MenuItem, Select, SelectChangeEvent, Input } from '@mui/material';
import "./App.css";
import { ChartPrediction, PlantPrediction, DiseasePrediction, PredictionResponse } from './utils/types';
import { Bar, BarChart, CartesianGrid, Legend, Tooltip, XAxis, YAxis } from 'recharts';
import { DISEASES_LABELS, PLANT_LABELS } from './utils/helper';

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [selectedModel, setSelectedModel] = useState<string>("mtl")
  const [predictionResponse, setPredictionResponse] = useState<PredictionResponse | null>(null)

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSelectedFile(e.target.files?.[0] ?? null);
  }

  const handleModelChange = (e: SelectChangeEvent) => {
    setSelectedModel(e.target.value as string);
  }

  const generateData = (prediction: PredictionResponse, type: string) => {

    let scores: number[];
    let labels: string[];
    let data: ChartPrediction[] = [];
    if (type === "class") {
      scores = prediction.class_prediction.prediction_scores;
      labels = PLANT_LABELS;
    } else {
      scores = prediction.disease_prediction.prediction_scores;
      labels = []

      prediction.disease_prediction.prediction_indices.forEach(index => labels.push(DISEASES_LABELS[index]));
    }
    
    for (var i = 0; i < scores.length; i++) {
      var obj: ChartPrediction = {name: labels[i],
         value: scores[i]};
      data.push(obj);
    }

    return data;
  }

  const handleUpload = async () => {
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append('file', selectedFile, selectedFile.name);
    formData.append('type', selectedModel);

    const response = await fetch("http://localhost:8000/predict/", {
      method: "POST",
      body: formData,
    }).then((response) => 
    {
      return response.json()
    })

    console.log(response)
    setPredictionResponse(response);

  }

  return (
    <div className="App">
      <div className="App-header">
        <div>
          <div>
            <h1>Leaf Disease Detection</h1>
          </div>

          <div className="controls">
            <div>
              <p>Please load an image.</p>
              <Input type="file" name="imageLoad" onChange={handleFileInput}/>
            </div>

            <div>
              <p>Select a model</p>
              <Select
                value={selectedModel}
                onChange={handleModelChange}
              >
                <MenuItem value="mtl">Multi-Task Learning</MenuItem>
                <MenuItem value="simple">Simple CNN</MenuItem>
                <MenuItem value="inception">InceptionV3</MenuItem>
              </Select>
            </div>
          </div>

          <Button onClick={handleUpload}>Find</Button>
        </div>

        <div className="content">
          {predictionResponse !== null && (<div>
            <p>Plant: {predictionResponse.class_prediction.prediction}</p>
            <p>Disease Detected: {predictionResponse.disease_prediction.prediction}</p>

            <div>
              <BarChart
                width={800}
                height={300}
                data={generateData(predictionResponse, "class")}
                margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" fontSize={20}/>
                <YAxis />
                <Tooltip />
                <Bar dataKey="value" fill="#8884d8" />
              </BarChart>
            </div>

            <div>
              <BarChart
                width={800}
                height={300}
                data={generateData(predictionResponse, "disease")}
                margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" fontSize={20}/>
                <YAxis />
                <Tooltip />
                <Bar dataKey="value" fill="#8884d8" />
              </BarChart>
            </div>

          </div>)}
        </div>
      </div>
    </div>
  );
}

export default App;
