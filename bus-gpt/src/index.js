import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App.js';
import 'bulma/css/bulma.min.css';
import './App.css';

const container = document.getElementById('root');
const root = createRoot(container);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);