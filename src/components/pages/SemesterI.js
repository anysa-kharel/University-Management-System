import React from 'react';

function SemesterI() {
  const subjects = [
    'Engineering Mathematics',
    'Engineering Drawing',
    'Engineering Physics',
    'C programming',
    'Digital Logic',
    // Add more subjects as needed
  ];

  return (
    <div className="flex flex-col gap-4">
      {subjects.map((subject, index) => (
        <div key={index} className="bg-white p-4 rounded-md shadow-md">
          <div className="flex items-center justify-between mb-2">
            <h2 className="text-lg font-semibold">{subject}</h2>
            <button className="bg-[#2a5279] text-white py-1 px-4 rounded">Register</button>
          </div>
          <p className="text-gray-500">Description of {subject}</p>
        </div>
      ))}
    </div>
  );
}

export default SemesterI;
