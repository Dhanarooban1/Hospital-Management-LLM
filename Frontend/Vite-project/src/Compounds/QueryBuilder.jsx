  // QueryBuilder.jsx
  import React, { useState } from 'react';
  import { Search, RefreshCw } from 'lucide-react';
  import {useQueryContext } from '../Functions/Controller';

  function QueryBuilder() {
    const { question, setQuestion, isLoading, onQuerySubmit } = useQueryContext();
    
    const commonQueries = [
      "Show all patients admitted this week",
      "List patients with pending lab results",
      "Find patients with diabetes",
      "Show emergency room visits today"
    ];

    return (
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Query Builder</h2>
        
        <form onSubmit={(e)=>e.preventDefault()} className="space-y-4">
          <div className="relative">
            <textarea
              value={question}
              onChange={(e)=>setQuestion(e.target.value)}
              className="w-full h-32 p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="Enter your query here..."
              />
            <button
              type="submit"
              disabled={isLoading}
              onClick={(e) => {onQuerySubmit(question)}}
              className="absolute bottom-4 right-4 bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 flex items-center space-x-2"
            >
              {isLoading ? (
                <RefreshCw className="h-5 w-5 animate-spin" />
              ) : (
                <Search className="h-5 w-5" />
              )}
              <span>Execute Query</span>
            </button>
          </div>
        </form>

        <div className="mt-6">
          <h3 className="text-sm font-medium text-gray-700 mb-3">Common Queries</h3>
          <div className="grid grid-cols-2 gap-2">
            {commonQueries.map((q, index) => (
              <button
                key={index}
                onClick={() => {
                  setQuestion(q);
                  onQuerySubmit(q);
                }}
                className="text-left text-sm text-gray-600 hover:text-blue-600 p-2 rounded-md hover:bg-blue-50"
              >
                {q}
              </button>
            ))}
          </div>
        </div>
      </div>
    );
  }

  export default QueryBuilder;