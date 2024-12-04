// App.jsx
import React, { useState } from 'react';
// import App from './App.jsx'

import QueryBuilder from './Compounds/QueryBuilder';
import ResultsTable from './Compounds/ResultsTable';
import Header from './Compounds/Header'

import { QueryProvider } from './Functions/Controller';

function App() {

  return (
    <QueryProvider>
      <div>
        <Header />
        <QueryBuilder />
        <ResultsTable />
      </div>
    </QueryProvider>
  );
}

export default App;