"use client"; // This marks the component as a Client Component

import MainLayout from '../components/MainLayout';

export default function Item() {
  const handleTakePhoto = () => {
    alert('Take a Photo functionality not implemented');
  };

  const handleAddItem = () => {
    alert('Add Item functionality not implemented');
  };

  return (
    <MainLayout>
      <div className="flex flex-col items-center justify-center h-screen bg-white p-12 mt-10">
        
        
        <form className=" rounded-lg shadow-lg p-6 max-w-sm w-full">
        <h2 className="text-3xl text-black mb-8 flex items-center justify-center">Recite Upload</h2>
          <div className="flex flex-col items-center mb-8">
            <img
              src="/cloud-computing.png" // Replace with your upload image logo path
              alt="Upload Image"
              className="h-16 w-16 mb-2"
            />
            <p className="text-black text-lg">Upload Image</p>
          </div>
          
          <div className="flex flex-col items-center mb-8">
            <img
              src="/cloud-computing.png" // Replace with your take photo logo path
              alt="Take a Photo"
              className="h-16 w-16 mb-2"
            />
            <p className="text-black text-lg">Take a Photo</p>
          </div>
          
          <button
            onClick={handleAddItem}
            className="bg-[#ff3C00] text-white py-2 px-4 rounded hover:bg-green-600 w-full"
          >
            Add Item
          </button>
        </form>
      </div>
    </MainLayout>
  );
}
