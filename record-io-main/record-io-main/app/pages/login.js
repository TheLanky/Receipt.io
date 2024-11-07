export default function Login() {
    return (
      <div
        className="mt-16 flex flex-col items-center justify-center h-screen bg-cover bg-center"
        style={{ backgroundImage: "url('/logo.svg')" }}
      >
        <form className="p-6 rounded-lg w-96 backdrop-blur">
          <h2 className="text-2xl font-bold mb-6 text-center">Login</h2>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Email
            </label>
            <input
              type="email"
              className="w-full p-2 border border-gray-300 rounded"
              placeholder="Enter your email"
            />
          </div>
          <div className="mb-6">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Password
            </label>
            <input
              type="password"
              className="w-full p-2 border border-gray-300 rounded"
              placeholder="Enter your password"
            />
          </div>
          <button
            type="submit"
            className="w-full bg-[#ff3C00] text-white font-bold p-2 rounded hover:bg-blue-600 transition duration-300"
          >
            Login
          </button>
        </form>
      </div>
    );
  }
  