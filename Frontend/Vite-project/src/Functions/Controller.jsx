import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

const QueryContext = createContext();

export const QueryProvider = ({ children }) => {
  const [question, setQuestion] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState({ data: [] });
  const [queryReady, setQueryReady] = useState(false); 

  const onQuerySubmit = (query) => {
    setQueryReady(true);
    setQuestion(query.trim());
  };

  useEffect(() => {
    const fetchResults = async () => {
      if (!queryReady) return;

      try {
        setIsLoading(true);

        const response = await axios.post(
          'https://hospital-management-llm-backend.onrender.com/post/query',
          { question },
          {
            headers: {
              'Content-Type': 'application/json',
              Accept: 'application/json',
            },
            withCredentials: true,
          }
        );
        setResults(response.data.results);
      } catch (error) {
        console.error('Error sending query:', error.response?.data || error.message);
      } finally {
        setIsLoading(false);
        setQueryReady(false);
      }
    };

    fetchResults();
  }, [queryReady, question]);

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
