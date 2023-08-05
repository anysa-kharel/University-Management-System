import React from 'react';
import { useState } from 'react';
import Dashboard from "./Dashboard";
import { Link } from 'react-router-dom';

function LoginModal(props) {

const [user,setUser]=useState("");
const [pass,setPass]=useState("");

const handleClick = () =>
{
  if(user==="123" && pass==="123")
{
//  <Link to="/dashboard"/>
<Dashboard/>
console.log("Correct User Password");
}
else{
  console.log("Incorrect");  
}

}




  return (
                <div className=" flex items-center justify-center  bg-opacity-80">
                <div className="w-full max-w-md p-8 bg-white border border-gray-300 shadow-lg rounded-lg">
                <form>
                <h3 className="text-xl font-semibold mb-4 text-primary-focus  text-center ">Login as {props.title}</h3>

                <div className="mb-4">
                {/* <label htmlFor="user" className="block font-medium mb-2">
                Username
                </label> */}
                <input
                type="username"
                id="user"
                className="w-full px-4 py-2 border rounded-lg focus:outline-none bg-transparent"
                onChange={(e)=>setUser(e.currentTarget.value)}
                placeholder="Username"
                />
                </div>

                <div className="mb-4">
                {/* <label htmlFor="password" className="block font-medium mb-2">
                Password
                </label> */}
                <input
                type="password"
                id="password"
                className="w-full px-4 py-2 border rounded-lg focus:outline-none bg-transparent"
                onChange={(e)=>setPass(e.currentTarget.value)}
                placeholder="Password"
                />
                </div>

                <div className="mb-4">
                <div className="flex items-center">
                <input
                type="checkbox"
                id="customCheck1"
                className="custom-control-input checkbox-primary-focus"
                />
                <label
                htmlFor="customCheck1"
                className="custom-control-label ml-2 text-primary"
                >
                Remember me
                </label>
                </div>
                </div>

                <div className="flex justify-center">
                <button
                type="login"
                className="w-full px-4 py-2 bg-primary hover:bg-primary-focus text-white rounded-lg focus:outline-none"
                onClick={handleClick}
                >
                Login
                </button>
                </div>
                </form>

                <p className="text-right mt-4 text-primary">
                Forgot Password?
                </p>
                </div>
                </div>
  );
}

export default LoginModal;