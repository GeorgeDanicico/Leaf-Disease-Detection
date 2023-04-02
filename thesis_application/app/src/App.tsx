import React, { useState } from 'react';
import { Button, MenuItem, Select, SelectChangeEvent, Input } from '@mui/material';
import "./App.css";

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [selectedModel, setSelectedModel] = useState<string>("mtl")

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

    const response = await fetch("http://localhost:8000/predict/", {
      method: "POST",
      body: formData,
    }).then((response) => 
    {
      return response.json()
    })

    console.log(response)

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
                labelId="demo-simple-select-label"
                id="demo-simple-select"
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

      </div>
    </div>
  );
}

export default App;
