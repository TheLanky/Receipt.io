"use client"; // This marks the component as a Client Component

import MainLayout from '../components/MainLayout';
import { useState } from 'react';

export default function EditProfile() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: '',
    contact: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Profile updated!');
  };

  return (
    <MainLayout>
      <div className="flex flex-col items-center justify-center h-screen p-4 mt-32">
        <h2 className="text-2xl text-black font-bold mb-6">Edit Profile</h2>
        
        <form onSubmit={handleSubmit} className="bg-white p-4 rounded-lg shadow-lg w-full max-w-sm">
          <div className="mb-4 text-center">
            <p className="text-gray-700 mb-2">Upload or drag photo</p>
            <img
              src="/user.png" // Replace with your user icon path
              alt="User Icon"
              className="h-20 w-20 mx-auto mb-2"
            />
            <input
              type="file"
              className="block mx-auto mb-4 border rounded-md p-1 text-gray-700"
              // Placeholder for file input handling
            />
          </div>

          <div className="mb-3">
            <label className="block text-gray-700 mb-1 text-sm" htmlFor="name">Name</label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="block w-full border rounded-md p-1 text-sm"
              required
            />
          </div>

          <div className="mb-3">
            <label className="block text-gray-700 mb-1 text-sm" htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="block w-full border rounded-md p-1 text-sm"
              required
            />
          </div>

          <div className="mb-3">
            <label className="block text-gray-700 mb-1 text-sm" htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="block w-full border rounded-md p-1 text-sm"
              required
            />
          </div>

          <div className="mb-3">
            <label className="block text-gray-700 mb-1 text-sm" htmlFor="confirmPassword">Confirm Password</label>
            <input
              type="password"
              id="confirmPassword"
              name="confirmPassword"
              value={formData.confirmPassword}
              onChange={handleChange}
              className="block w-full border rounded-md p-1 text-sm"
              required
            />
          </div>

          <div className="mb-3">
            <label className="block text-gray-700 mb-1 text-sm" htmlFor="contact">Contact</label>
            <input
              type="text"
              id="contact"
              name="contact"
              value={formData.contact}
              onChange={handleChange}
              className="block w-full border rounded-md p-1 text-sm"
              required
            />
          </div>

          <div className="text-center">
            <button
              type="submit"
              className="bg-[#ff3C00] text-white py-1 px-4 rounded hover:bg-green-600 text-sm"
            >
              Update
            </button>
          </div>
        </form>
      </div>
    </MainLayout>
  );
}
