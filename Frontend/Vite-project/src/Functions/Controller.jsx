// QueryContext.js
import React, { createContext, useContext, useState } from 'react';
import axios from 'axios';

const QueryContext = createContext();

export const QueryProvider = ({ children }) => {
  const [question, setQuestion] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState({ data: [] });

  const onQuerySubmit = async (query) => {
    try {
      setIsLoading(true);
      const response = await axios.post('http://localhost:5000/post/query', 
        { question: query.trim() },
        {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          withCredentials: true
        }
      );
      setResults(response.data);
      return response.data;
      
    } catch (error) {
      console.error('Error sending query:', error.response?.data || error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <QueryContext.Provider
      value={{
        question,
        setQuestion,
        isLoading,
        onQuerySubmit,
        results,
      }}
    >
      {children}
    </QueryContext.Provider>
  );
};

export const useQueryContext = () => useContext(QueryContext);
