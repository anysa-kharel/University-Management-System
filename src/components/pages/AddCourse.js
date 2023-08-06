import React, { Component } from 'react'

export default class AddCourse extends Component {
    constructor(){
        super();
        this.state={
            registration_id:'',
            student:'',
            module:''


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
       
        fetch('http://127.0.0.1:8000/registration/',{
            method:'POST',
            body:JSON.stringify(this.state),
            headers:{
                'Content-type': 'application/json; charset=UTF-8',
            },
        })
        .then(response=>response.json())
        .then((data)=>console.log(data));

        this.setState({
            
            registration_id:'',
            student:'',
            module:''
        });
    
    }





  render()
  
  {
    return (
     <>

<div className="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md">
    <h2 className="text-2xl font-semibold mb-4">Register for Module</h2>

    <form>
    <div className="mb-4">
            <label for="registration_id" className="block text-sm font-medium text-gray-700">Registration ID</label>
            <input type="text" id="registration_id" name="registration_id" value={this.state.registration_id} onChange={this.changeHandler} className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-primary rounded-md p-2"/>
        </div>

        <div className="mb-4">
            <label for="student" className="block text-sm font-medium text-gray-700">Student </label>
            <input type="text" id="student" name="student" value={this.state.student} onChange={this.changeHandler} className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-primary rounded-md p-2"/>
        </div>

        <div className="mb-4">
            <label for="module" className="block text-sm font-medium text-gray-700">Module</label>
            <input type="text" id="module" name="module" value={this.state.module} onChange={this.changeHandler} className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-primary rounded-md p-2"/>
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
