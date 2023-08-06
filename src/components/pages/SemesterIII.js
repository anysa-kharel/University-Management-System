import React from 'react'

function SemesterIII() {
    const subjects = [
        'English',
        'Economics',
        'Computer Network',
        'Computer Graphics',
        'Filter Design'
        // Add more subjects as needed
      ];
  return (
    <div className="grid grid-cols-3 gap-4">
    {subjects.map((subject, index) => (
      <div key={index} className="bg-white p-4 rounded-md shadow-md">
        <h2 className="text-lg font-semibold">{subject}</h2>
        <p className="text-gray-500 mt-2">Description of {subject}</p>
      </div>
    ))}
  </div>
  )
}

export default SemesterIII
