"use client";

import { useRouter } from 'next/navigation';

export default function Navbar() {
  const router = useRouter();
  
  // Check if router is defined and accessible
  if (!router) {
    console.log('Router is not available');
  }

  const pageTitles = {
    '/dashboard': 'Dashboard',
    '/item': 'Add Item',
    '/edit': 'Edit Item',
    '/remove-item': 'Remove Item',
    '/history': 'History',
    '/': 'Home',
  };

  // Ensure pathname is defined
  const currentPath = router ? router.pathname : '/';
  const pageTitle = pageTitles[currentPath] || 'RECORD IO';

  return (
    <nav className="bg-[#ff3C00] text-white p-4 fixed w-full flex items-center z-50">
      <div className="flex items-center bg-white" style={{ borderRadius: "80%" }}>
        <img
          src="/nav.svg"
          alt="Logo"
          className="h-20 w-48 rounded-full object-contain mr-4"
        />
      </div>
      <div className="flex-grow text-center">
        <h1 className="text-2xl font-bold mr-20">{pageTitle}</h1>
      </div>
    </nav>
  );
}
