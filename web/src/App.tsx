import React from "react";
import logo from "./logo.jpg";
import "./App.css";
import LandingPage from "./LandingPage";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <LandingPage />
      </header>
    </div>
  );
}

export default App;
