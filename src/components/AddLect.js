import React, { Component } from 'react'

export default class AddLect extends Component {

    constructor(){
        super();
        this.state={
            lecturer_number:'',
            name:'',
            room_number:''
        }
        this.changeHandler=this.changeHandler.bind(this);
        this.submitForm=this.submitForm.bind(this);
    }


    changeHandler(event){
        this.setState({
            [event.target.name]:event.target.value
        });
    }


    submitForm(){
        fetch('http://127.0.0.1:8000/lecturer/',{
            method:'POST',
            body:JSON.stringify(this.state),
            headers:{
                'Content-type': 'application/json; charset=UTF-8',
            },
        })
        .then(response=>response.json())
        .then((data)=>console.log(data));

        this.setState({
            lecturer_number:'',
            name:'',
            room_number:''
        });
    }



  render() {
    return (
     <>

<div className="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md">
    <h2 className="text-2xl font-semibold mb-4">Lecturer Information</h2>

    <form>
        <div className="mb-4">
            <label for="lectNumber" className="block text-sm font-medium text-gray-700">Lecturer Number</label>
            <input type="text" id="lectNumber" name="lecturer_number" value={this.state.lecturer_number} onChange={this.changeHandler} className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-primary rounded-md p-2"/>
        </div>

        <div className="mb-4">
            <label for="name" className="block text-sm font-medium text-gray-700">Name</label>
            <input type="text" id="name" name="name" value={this.state.name} onChange={this.changeHandler} className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-primary rounded-md p-2"/>
        </div>

        <div className="mb-4">
            <label for="roomNumber" className="block text-sm font-medium text-gray-700">Room Number</label>
            <input type="text" id="roomNumber" name="room_number" value={this.state.room_number} onChange={this.changeHandler} className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-primary rounded-md p-2"/>
        </div>


        <div className="flex justify-end">
            {/* <button type="button" className="mr-2 px-4 py-2 text-sm font-medium text-gray-700 bg-gray-300 border border-gray-300 rounded-md hover:bg-gray-400 focus:outline-none focus:ring focus:ring-gray-200">
                Cancel
            </button> */}
            <button type="submit" onClick={this.submitForm} className="px-4 py-2 text-sm font-medium text-white bg-primary border border-transparent rounded-md hover:bg-primary-focus focus:outline-none focus:ring focus:ring-indigo-300">
                Save
            </button>
        </div>
    </form>
</div>












     </>
    )
  }
}
