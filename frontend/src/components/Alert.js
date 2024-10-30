// components/Alert.js
export default function Alert({ message, type }) {
  const alertType = {
      success: 'bg-green-100 border-green-400 text-green-700',
      error: 'bg-red-100 border-red-400 text-red-700',
  };

  return (
      <div className={`border-l-4 p-4 ${alertType[type]} mb-4`} role="alert">
          <p className="font-bold">{type === 'success' ? 'Success' : 'Error'}</p>
          <p>{message}</p>
      </div>
  );
}