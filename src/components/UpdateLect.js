import React, { Component } from 'react';

export default class UpdateLect extends Component {
  constructor() {
    super();
    this.state = {
      id: '', // Initialize id in state
      lecturer_number: '',
      name: '',
      room_number: '',
    };

    this.changeHandler = this.changeHandler.bind(this);
    this.submitForm = this.submitForm.bind(this);
  }

  componentDidMount() {
   
      this.fetchData();
 
  }

  // Input Change Handler
  changeHandler(event) {
    this.setState({
      [event.target.name]: event.target.value,
    });
  }

  // Submit Form
  submitForm() {
    var id=this.props.match.params.id;
    fetch('http://127.0.0.1:8000/lecturer/update/'+id+'/', {
      method: 'PUT',
      body: JSON.stringify(this.state),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
    })
      .then((response) => response.json())
      .then((data) => console.log(data));
  }

  fetchData() {
    var id=this.props.match.params.id;
    fetch('http://127.0.0.1:8000/lecturer/update/'+id)
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          lecturer_number: data.lecturer_number,
          name: data.name,
          room_number: data.room_number,
        });
      });
      
  }

  render() {
    return (
      <>
        <table className="table table-bordered">
          <tbody>
            <tr>
              <th className="py-2">Lecturer Number</th>
              <td className="py-2">
                <input
                  value={this.state.lecturer_number}
                  name="lecturer_number"
                  onChange={this.changeHandler}
                  type="text"
                  className="form-input"
                />
              </td>
            </tr>
            <tr>
              <th className="py-2">Name</th>
              <td className="py-2">
                <input
                  value={this.state.name}
                  name="name"
                  onChange={this.changeHandler}
                  type="text"
                  className="form-input"
                />
              </td>
            </tr>
            <tr>
              <th className="py-2">Room Number</th>
              <td className="py-2">
                <input
                  value={this.state.room_number}
                  name="room_number"
                  onChange={this.changeHandler}
                  type="text"
                  className="form-input"
                />
              </td>
            </tr>
            <tr>
              <td colSpan="2" className="py-2">
                <button
                  onClick={this.submitForm}
                  className="bg-gray-800 text-white py-2 px-4 rounded"
                >
                  Submit
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </>
    );
  }
}
