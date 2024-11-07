export default function InputField({ label, type = "text", placeholder }) {
    return (
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">
          {label}
        </label>
        <input
          type={type}
          className="w-full p-2 border border-gray-300 rounded"
          placeholder={placeholder}
        />
      </div>
    );
  }
  