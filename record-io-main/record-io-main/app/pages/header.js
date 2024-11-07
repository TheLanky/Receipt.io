"use client"; // Marks the component as a Client Component

import { useRouter } from "next/navigation";

export default function Header() {
  const router = useRouter();

  return (
    <header
      className="w-full h-screen bg-cover bg-center flex flex-col justify-center items-center"
      style={{ backgroundImage: "url('/logo.svg')" }}
    >
      <div className="mt-48 rounded-lg">
        <button
          className="w-full mb-4 p-2 bg-[#ff3C00] text-white font-bold rounded hover:bg-gray-400 transition duration-300"
          style={{ width: "150%" }}
          onClick={() => router.push("/signUp")}
        >
          Sign Up
        </button>
        <button
          className="p-2 bg-[#ff3C00] text-white font-bold rounded hover:bg-gray-400 transition duration-300"
          style={{ width: "150%" }}
          onClick={() => router.push("/login")}
        >
          Login
        </button>
      </div>
    </header>
  );
}
    