import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./routes/Home";
import About from "./routes/About";
import Contact from "./routes/Contact";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Protocol from "./routes/Protocol";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" exact element={<Home />} />
          <Route path="/about" element={<About/>} />
          <Route path="/contact" element={<Contact/>} />
          <Route path="/protocol" element={<Protocol/>} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;