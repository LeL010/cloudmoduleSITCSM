import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import KommunicateChat from './pages/Index';
import ContactUs from './pages/ContactUs';
import 'bulma/css/bulma.min.css';
import './App.css';

const App = () => {
  return (
    <Router>
      <div>
        <nav className="navbar is-primary">
          <div className="navbar-brand">
            <a className="navbar-item" href="/">
              My App
            </a>
          </div>
          <div className="navbar-menu">
            <div className="navbar-start">
              <Link className="navbar-item" to="/">Home</Link>
              <Link className="navbar-item" to="/contact">Contact Us</Link>
            </div>
          </div>
        </nav>
        <Routes>
          <Route path="/" element={<KommunicateChat />} />
          <Route path="/contact" element={<ContactUs />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;