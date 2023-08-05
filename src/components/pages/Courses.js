// import React, { useEffect, useState } from 'react';
// import { useParams } from 'react-router-dom';

// function Courses() {
//   const { faculty } = useParams(); // Get the selected faculty from the URL

//   const [courses, setCourses] = useState([]);

//   useEffect(() => {
//     // Fetch API data for the selected faculty (e.g., using Axios or fetch)
//     // Replace 'YOUR_API_ENDPOINT' with the actual API endpoint for the selected faculty
//     fetch('YOUR_API_ENDPOINT')
//       .then((response) => response.json())
//       .then((data) => {
//         setCourses(data);
//       })
//       .catch((error) => {
//         console.error('Error fetching courses:', error);
//       });
//   }, [faculty]); // Fetch courses whenever the faculty changes

//   return (
//     <div>
//       <h2>{faculty} Courses</h2>
//       <ul>
//         {courses.map((course) => (
//           <li key={course.id}>{course.name}</li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default Courses;
