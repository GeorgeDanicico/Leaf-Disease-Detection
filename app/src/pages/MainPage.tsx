import React, { useState } from 'react';
import { Button, MenuItem, Select, SelectChangeEvent, Input, CircularProgress } from '@mui/material';
import { PredictionResponse } from '../utils/types';
import { Bar, BarChart, CartesianGrid, Tooltip, XAxis, YAxis } from 'recharts';
import { useGenerateData } from './hooks';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import "./style.css";

function MainPage() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [selectedModel, setSelectedModel] = useState<string>("mtl");
  const [predictionResponse, setPredictionResponse] = useState<PredictionResponse | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const generateData = useGenerateData();


  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSelectedFile(e.target.files?.[0] ?? null);
  }

  const handleModelChange = (e: SelectChangeEvent) => {
    setSelectedModel(e.target.value as string);
  }

  const handleUpload = async () => {
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append('file', selectedFile, selectedFile.name);
    formData.append('type', selectedModel);
    setIsLoading(true);
    const response = await fetch("http://localhost:8000/predict/", {
      method: "POST",
      body: formData,
    }).then((response) => {
      setIsLoading(false);
      return response.json();
    }).catch((err) => {
      setIsLoading(false);
      toast.error("An error has occured.");
      return null;
    })

    if (response !== null) {
      setPredictionResponse(response);
    }
  }

  return (
    <div className="app-content">
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
                <MenuItem value="simple">Custom CNN</MenuItem>
                <MenuItem value="inception">InceptionV3</MenuItem>
              </Select>
            </div>
          </div>

          <Button onClick={handleUpload}>
            {isLoading ? <CircularProgress color="inherit"/> : <span>Submit</span>}
          </Button>
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
                <Bar dataKey="value" fill="#004225" />
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
                <Bar dataKey="value" fill="#004225" />
              </BarChart>
            </div>

          </div>)}
        </div>
        <ToastContainer />
      </div>
  );
}

export default MainPage;
