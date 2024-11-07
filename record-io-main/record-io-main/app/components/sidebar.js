"use client";

import Link from 'next/link';

export default function Sidebar() {
  const handleLogout = () => {
    // Implement your logout logic here
    console.log('Logout clicked');
  };

  return (
    <div className="bg-white text-white w-64 h-full fixed top-0 left-0 z-40 flex flex-col justify-between" style={{ fontSize: "0.8rem" }}>
      <div className="pt-16">
        <ul className="space-y-2 p-12">
          <li className="flex items-center space-x-2">
            <img src="/home.png" alt="Dashboard" className="h-6 w-6" />
            <Link href="/dashboard" className="block p-4 hover:bg-[#ff3C00] text-black">
              Dashboard
            </Link>
          </li>
          <li className="flex items-center space-x-2">
            <img src="/add.png" alt="Add Item" className="h-6 w-6" />
            <Link href="/item" className="block p-4 hover:bg-[#ff3C00] text-black">
              Add Item
            </Link>
          </li>
          <li className="flex items-center space-x-2">
            <img src="/user.png" alt="Edit Item" className="h-6 w-6" />
            <Link href="/edit-item" className="block p-4 hover:bg-[#ff3C00] text-black">
              Edit Item
            </Link>
          </li>
          <li className="flex items-center space-x-2">
            <img src="/forbidden.png" alt="Remove Item" className="h-6 w-6" />
            <Link href="/remove-item" className="block p-4 hover:bg-[#ff3C00] text-black">
              Remove Item
            </Link>
          </li>
          <li className="flex items-center space-x-2">
            <img src="/transaction-history.png" alt="History" className="h-6 w-6" />
            <Link href="/history" className="block p-4 hover:bg-[#ff3C00] text-black">
              History
            </Link>
          </li>
        </ul>
      </div>
      <div className="flex items-center space-x-2 ml-10 p-4 hover:bg-[#ff3C00] text-black cursor-pointer text-center" onClick={handleLogout}>
        <img src="/logout.png" alt="Logout" className="h-6 w-6" />
        <span>Logout</span>
      </div>
    </div>
  );
}
