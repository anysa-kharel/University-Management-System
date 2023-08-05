import React from 'react';
import { FiBell } from 'react-icons/fi'; // Import the notification icon

const Topbar = () => {
  return (
    <>
      <div>
        <div className="navbar  bg-[#2a5279]">
          <div className="flex-1">
            {/* <a className="btn btn-ghost normal-case text-xl">Welcome</a> */}
          </div>
          <div className="flex-none">
            <div className="dropdown dropdown-end">
              <label tabIndex={0} className="btn btn-ghost btn-circle">
                <div className="indicator">
                  <FiBell className="h-6 w-6 text-white" /> {/* Replace the cart icon with the notification icon */}
                  {/* <span className="badge badge-sm indicator-item">8</span> */}
                </div>
              </label>
              <div
                tabIndex={0}
                className="mt-3 z-[1] card card-compact dropdown-content w-52 bg-base-100 shadow"
              >
                {/* <div className="card-body"> */}
                  
                  {/* <div className="card-actions"> */}
                    {/* <button className="btn btn-primary btn-block">View cart</button> */}
                  {/* </div> */}
                {/* </div> */}
              </div>
            </div>
            <div className="dropdown dropdown-end">
              <label tabIndex={0} className="btn btn-ghost btn-circle avatar">
                <div className="w-10 rounded-full">
                  <img src="https://purepng.com/public/uploads/large/purepng.com-standing-girlwomenpeoplepersonsfemale-1121525092280vwte3.png" alt="Avatar" />
                </div>
              </label>
              <ul
                tabIndex={0}
                className="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
              >
                <li>
                  <a className="justify-between">
                    Profile
                    <span className="badge">New</span>
                  </a>
                </li>
                <li><a>Settings</a></li>
                <li><a>Logout</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Topbar;
