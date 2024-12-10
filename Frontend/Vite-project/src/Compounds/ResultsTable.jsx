import React, { useState } from 'react';
import { ArrowUpDown, Search, AlertCircle } from 'lucide-react';
import { useQueryContext } from '../Functions/Controller';

const ResultsTable = () => {
  const { results = [] } = useQueryContext(); // Default to an empty array
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });
  const [searchTerm, setSearchTerm] = useState('');

  const transformedResults = Array.isArray(results)
    ? results.map((row) => ({
        id: row[0],
        name: row[1],
        age: row[2],
        gender: row[3],
        condition: row[4],
      }))
    : [];


  const sortedResults = [...transformedResults].sort((a, b) => {
    if (!sortConfig.key) return 0;
    const aValue = a[sortConfig.key] || '';
    const bValue = b[sortConfig.key] || '';
    return sortConfig.direction === 'asc'
      ? aValue > bValue ? 1 : -1
      : aValue < bValue ? 1 : -1;
  });

  const filteredResults = sortedResults.filter((item) =>
    Object.values(item).some((value) =>
      value?.toString().toLowerCase().includes(searchTerm.toLowerCase())
    )
  );

  const requestSort = (key) => {
    let direction = 'asc';
    if (sortConfig.key === key && sortConfig.direction === 'asc') {
      direction = 'desc';
    }
    setSortConfig({ key, direction });
  };

  if (!Array.isArray(results)) {
    return (
      <div className="flex items-center justify-center h-64 bg-gray-50 rounded-lg">
        <div className="text-center">
          <AlertCircle className="w-12 h-12 mx-auto text-gray-400 mb-4" />
          <p className="text-gray-600">No results available</p>
        </div>
      </div>
    );
  }

  return (
    <div className="w-full space-y-4">
      <div className="relative">
        <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-5 w-5" />
        <input
          type="text"
          placeholder="Search results..."
          className="w-full pl-10 pr-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

      <div className="overflow-x-auto rounded-lg border border-gray-200 bg-white">
        <table className="w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              {['ID', 'Name', 'Age', 'Gender', 'Condition'].map((header, index) => (
                <th
                  key={index}
                  className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100 transition-colors"
                  onClick={() => requestSort(header.toLowerCase())}
                >
                  <div className="flex items-center space-x-1">
                    <span>{header}</span>
                    <ArrowUpDown className="h-4 w-4" />
                  </div>
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {filteredResults.map((item, index) => (
              <tr key={item.id || index} className="hover:bg-gray-50 transition-colors">
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{item.id || "N/A"}</td>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{item.name || "Unknown"}</td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{item.age || "N/A"}</td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{item.gender || "N/A"}</td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{item.condition || "N/A"}</td>
              </tr>
            ))}
          </tbody>
        </table>
        {filteredResults.length === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-500">No matching results found</p>
          </div>
        )}
      </div>
      <div className="text-sm text-gray-500">
        Showing {filteredResults.length} of {transformedResults.length} results
      </div>
    </div>
  );
};

export default ResultsTable;
