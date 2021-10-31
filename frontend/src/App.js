import logo from "./logo.png";
import "./App.css";

import React, { useState } from "react";

function App() {
  const [iterations, setIterations] = useState(100);
  const [randomState, setRandomState] = useState(1);
  const [learningRate, setLearningRate] = useState(0.01);
  const [predictionResult, setPredictionResult] = useState(
    "Aquí aparecerá tu valor"
  );

  const fetchThings = async () => {
    const url = `http://localhost:5000/prediction?n_iterations=${iterations}&random_state=${randomState}&learning_rate=${learningRate}`;

    const response = await fetch(url)
      .then((response) => response.json())
      .then((data) => data)
      .catch(() => setPredictionResult("Error"));
    return response;
  };

  const handleClick = async () => {
    const things = await fetchThings();
    setPredictionResult(things.msg);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>{predictionResult}</p>
        <input
          type="number"
          onChange={(val) => setIterations(val)}
          placeholder="iteraciones"
        />
        <br />
        <input
          type="number"
          onChange={(val) => setRandomState(val)}
          placeholder="semilla"
        />
        <br />
        <input
          type="number"
          onChange={(val) => setLearningRate(val)}
          placeholder="learning rate"
        />
        <br />
        <input
          type="number"
          onChange={(val) => setLearningRate(val)}
          placeholder="Año que se quiere conocer"
        />
        <br />
        <button onClick={handleClick}>Predecir</button>
      </header>
    </div>
  );
}

export default App;
