// Conteúdo para: frontend_react/src/App.js

import React from 'react';
import ParceirosPage from './pages/ParceirosPage';
import './App.css'; // O CSS padrão do React

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* Aqui você pode adicionar sua sidebar/layout depois */}
        <ParceirosPage />
      </header>
    </div>
  );
}

export default App;