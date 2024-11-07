export default function Button({ children, onClick, style }) {
    return (
      <button
        className="p-2 bg-[#ff3C00] text-white font-bold rounded hover:bg-gray-400 transition duration-300"
        style={style}
        onClick={onClick}
      >
        {children}
      </button>
    );
  }
  