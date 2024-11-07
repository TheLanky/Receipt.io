"use client"; // This marks the component as a Client Component

import { useState } from 'react';
import MainLayout from '../components/MainLayout';

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

  const handleRemoveAll = () => {
    // Implement logic to remove all items
    alert('All items removed');
    setItems([]);
  };

  const handleDisable = (id) => {
    // Implement logic to disable an item
    alert(`Item ${id} disabled`);
  };

  return (
    <MainLayout>
      <div className="p-6 mt-32 min-h-screen">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl text-black">All Technicians</h2>
          <button
            onClick={handleRemoveAll}
            className="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600"
          >
            Remove All
          </button>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
          {items.map((item) => (
            <div key={item.id} className="bg-white p-4 rounded-lg shadow-lg flex flex-col items-center">
              <div className="relative mb-4">
                <div className="w-16 h-16 border-4 border-[#ff3C00] rounded-full flex items-center justify-center" style={{ margin: '6px' }}>
                  <img
                    src="/user.png" // Replace with your user icon path
                    alt="User Icon"
                    className="h-12 w-12 rounded-full"
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
                className="bg-[#ff3C00] text-white py-1 px-3 rounded hover:bg-[#ff3C00] hover:bg-opacity-80"
              >
                Disable
              </button>
            </div>
          ))}
        </div>
      </div>
    </MainLayout>
  );
}
