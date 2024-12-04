// Header.jsx
import React from 'react';
import { Activity } from 'lucide-react';

function Header() {
  return (
    <header className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center">
            <Activity className="h-8 w-8 text-blue-600" />
            <h1 className="ml-3 text-2xl font-bold text-gray-900">HealthQuery Pro</h1>
          </div>
          <nav className="flex space-x-8">
            <a href="#dashboard" className="text-gray-700 hover:text-blue-600">Dashboard</a>
            <a href="#patients" className="text-gray-700 hover:text-blue-600">Patients</a>
            <a href="#analytics" className="text-gray-700 hover:text-blue-600">Analytics</a>
          </nav>
        </div>
      </div>
    </header>
  );
}

export default Header;