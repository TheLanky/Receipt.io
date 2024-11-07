"use client"; // This marks the component as a Client Component

import { useState } from 'react';
import MainLayout from '../components/MainLayout';

const initialRecords = [
  { stop: 'A', id: 1, name: 'Item A', quantity: 10, cost: 100 },
  { stop: 'B', id: 2, name: 'Item B', quantity: 5, cost: 50 },
  { stop: 'C', id: 3, name: 'Item C', quantity: 8, cost: 80 },
  { stop: 'D', id: 4, name: 'Item D', quantity: 15, cost: 150 },
  { stop: 'E', id: 5, name: 'Item E', quantity: 12, cost: 120 },
  { stop: 'F', id: 6, name: 'Item F', quantity: 9, cost: 90 },
  { stop: 'G', id: 7, name: 'Item G', quantity: 11, cost: 110 },
  { stop: 'H', id: 8, name: 'Item H', quantity: 7, cost: 70 },
  { stop: 'I', id: 9, name: 'Item I', quantity: 14, cost: 140 },
  { stop: 'J', id: 10, name: 'Item J', quantity: 6, cost: 60 },
];

export default function History() {
  const [records, setRecords] = useState(initialRecords);

  return (
    <MainLayout>
      <div className="p-6 mt-32 min-h-screen">
        {/* Overall History Card */}
        <div className="bg-white p-6 rounded-lg shadow-lg mb-8">
          <h2 className="text-2xl font-semibold mb-4">Overall History</h2>
          <div className="grid grid-cols-4 gap-4 mb-4">
            <div className="text-center">
              <h3 className="text-lg font-medium mb-2">Today</h3>
              <p className="text-xl font-bold">12</p>
              <p className="text-gray-600">Items</p>
            </div>
            <div className="text-center">
              <h3 className="text-lg font-medium mb-2">This Week</h3>
              <p className="text-xl font-bold">50</p>
              <p className="text-gray-600">Items</p>
            </div>
            <div className="text-center">
              <h3 className="text-lg font-medium mb-2">Last Month</h3>
              <p className="text-xl font-bold">200</p>
              <p className="text-gray-600">Items</p>
            </div>
            <div className="text-center">
              <h3 className="text-lg font-medium mb-2">Issues</h3>
              <p className="text-xl font-bold">5</p>
              <p className="text-gray-600">Reports</p>
            </div>
          </div>
        </div>

        {/* Records Table */}
        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h2 className="text-2xl font-semibold mb-4">Records</h2>
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Stop</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Item ID</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Item Name</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Quantity</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Cost</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"></th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {records.map((record) => (
                <tr key={record.id}>
                  <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{record.stop}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{record.id}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{record.name}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{record.quantity}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${record.cost}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    <button className="bg-blue-500 text-white py-1 px-3 rounded hover:bg-blue-600">Details</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </MainLayout>
  );
}
