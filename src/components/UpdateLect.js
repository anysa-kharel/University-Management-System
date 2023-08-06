import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Link } from 'react-router-dom';

function UpdateLect() {
  const params = useParams();


  
  const [state, setState] = useState({
    id: `${params.id}`, // Initialize id in state
    lecturer_number: '',
    name: '',
    room_number: '',
  });

  


  const fetchData = () => {
    const id = params.id;
    console.log(id)
    
    fetch('http://127.0.0.1:8000/lecturer/update/'+id+'/')
      .then((response) => response.json())
      .then((data) => {
        setState({
          ...state,
          lecturer_number: data.lecturer_number,
          name: data.name,
          room_number: data.room_number,
        });
      });
  };


  useEffect(() => {
    fetchData();
  }, []);

  const changeHandler = (event) => {
    setState({
      ...state,
      [event.target.name]: event.target.value,
    });
    console.log(state)
  };



  const submitForm = () => {
    const id = params.id;
    fetch('http://127.0.0.1:8000/lecturer/update/'+id+'/', {
      method: 'PUT',
      body: JSON.stringify(state),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
    })
      .then((response) => response.json())
      .then((data) => console.log(data));
  };

  useEffect(() => {
    submitForm();
  }, []);



 
  return (
    <>
      <table className="table table-bordered">
        <tbody>
          <tr>
            <th className="py-2">Lecturer Number</th>
            <td className="py-2">
              <input
                value={state.lecturer_number}
                name="lecturer_number"
                onChange={changeHandler}
                type="text"
                className="form-input"
              />
            </td>
          </tr>
          <tr>
            <th className="py-2">Name</th>
            <td className="py-2">
              <input
                value={state.name}
                name="name"
                onChange={changeHandler}
                type="text"
                className="form-input"
              />
            </td>
          </tr>
          <tr>
            <th className="py-2">Room Number</th>
            <td className="py-2">
              <input
                value={state.room_number}
                name="room_number"
                onChange={changeHandler}
                type="text"
                className="form-input"
              />
            </td>
          </tr>
          <tr>
            <td colSpan="2" className="py-2">
              <Link to="/lecttab" onClick={submitForm} className="bg-gray-800 text-white py-2 px-4 rounded">Submit</Link>
            
            </td>
          </tr>
        </tbody>
      </table>
    </>
  );
}

export default UpdateLect;
