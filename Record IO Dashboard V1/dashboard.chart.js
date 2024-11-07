"use client"; // This marks the component as a Client Component

import { useState, useEffect } from 'react';
import MainLayout from '../components/MainLayout';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

// Register Chart.js components required for the bar chart
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

// Placeholder data to be replaced by parsed receipt data
const initialItems = [
  { category: 'Groceries', amount: 150 },
  { category: 'Dining', amount: 80 },
  { category: 'Transportation', amount: 40 },
  { category: 'Healthcare', amount: 120 },
];

export default function SpendingDashboard() {
  // State to manage spending items, initially set to placeholder data
  const [items, setItems] = useState(initialItems);

  // Chart data configuration for spending categories and their amounts
  const chartData = {
    labels: items.map(item => item.category), // Categories as chart labels
    datasets: [
      {
        label: 'Spending Amount ($)', // Label for the dataset
        data: items.map(item => item.amount), // Amounts for each category
        backgroundColor: 'rgba(75, 192, 192, 0.2)', // Bar color
        borderColor: 'rgba(75, 192, 192, 1)', // Border color
        borderWidth: 1,
      },
    ],
  };

  return (
    <MainLayout>
      <div className="p-6 mt-32 min-h-screen">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl text-black">Spending Dashboard</h2>
        </div>

        {/* Spending Category Bar Chart */}
        <div className="mb-6">
          <h3 className="text-xl text-black mb-4">Spending by Category</h3>
          <Bar data={chartData} options={{ responsive: true }} /> {/* Render the bar chart */}
        </div>

        {/* Display Individual Spending Items */}
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mb-6">
          {items.map((item, index) => (
            <div key={index} className="bg-white p-4 rounded-lg shadow-lg flex flex-col items-center">
              <div className="text-center mb-4">
                <p className="text-gray-700 font-semibold">{item.category}</p> {/* Display category */}
                <p className="text-gray-600">Amount: ${item.amount}</p> {/* Display amount */}
              </div>
            </div>
          ))}
        </div>
      </div>
    </MainLayout>
  );
}
