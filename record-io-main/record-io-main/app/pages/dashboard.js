"use client"; // This marks the component as a Client Component

import { useState } from 'react';
import MainLayout from '../components/MainLayout';
import { Bar } from 'react-chartjs-2'; // Import Chart.js library
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const initialItems = [
  { id: 1, name: 'Technician A', quantity: 10 },
  { id: 2, name: 'Technician B', quantity: 5 },
  { id: 3, name: 'Technician C', quantity: 8 },
  { id: 4, name: 'Technician D', quantity: 15 },
  { id: 5, name: 'Technician E', quantity: 12 },
  { id: 6, name: 'Technician F', quantity: 9 },
  { id: 7, name: 'Technician G', quantity: 11 },
  { id: 8, name: 'Technician H', quantity: 7 },
  { id: 9, name: 'Technician I', quantity: 14 },
];

export default function RemoveItem() {
  const [items, setItems] = useState(initialItems);
  const [disabledItems, setDisabledItems] = useState(new Set());

  const handleRemoveAll = () => {
    // Implement logic to remove all items
    alert('All items removed');
    setItems([]);
  };

  const handleDisable = (id) => {
    // Add ID to the set of disabled items
    setDisabledItems(prev => new Set(prev).add(id));
    alert(`Item ${id} disabled`);
  };

  // Chart data
  const chartData = {
    labels: items.map(item => item.name),
    datasets: [
      {
        label: 'Quantity',
        data: items.map(item => item.quantity),
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      },
    ],
  };

  return (
    <MainLayout>
      <div className="p-6 mt-32 min-h-screen">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl text-black">All Items</h2>
          <button
            onClick={handleRemoveAll}
            className="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600"
          >
            Delete All
          </button>
        </div>
        {/* Histogram Graph */}
        <div className="mb-6">
          <h3 className="text-xl text-black mb-4">Technician Quantity</h3>
          <Bar data={chartData} options={{ responsive: true }} />
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mb-6">
          {items.map((item) => (
            <div key={item.id} className="bg-white p-4 rounded-lg shadow-lg flex flex-col items-center">
              <div className="relative mb-4">
                <div className="w-24 h-24 border-4 border-[#ff3C00] rounded-full flex items-center justify-center" style={{ margin: '6px' }}>
                  <img
                    src="/user.png" // Replace with your user icon path
                    alt="User Icon"
                    className="h-20 w-20 rounded-full"
                  />
                </div>
              </div>
              <div className="text-center mb-4">
                <p className="text-gray-700 font-semibold">{item.name}</p>
                <p className="text-gray-600">ID: {item.id}</p>
                <p className="text-gray-600">Quantity: {item.quantity}</p>
              </div>
              <button
                onClick={() => handleDisable(item.id)}
                className="bg-[#ff3C00] text-white py-1 px-3 rounded hover:bg-[#ff3C00] hover:bg-opacity-80 relative"
              >
                Disable
                {disabledItems.has(item.id) && (
                  <span className="absolute top-0 right-0 bg-red-600 text-white text-xs rounded-full h-4 w-4 flex items-center justify-center">X</span>
                )}
              </button>
            </div>
          ))}
        </div>

        
      </div>
    </MainLayout>
  );
}
