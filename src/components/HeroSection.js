    
import React from 'react';
import LoginModal from './LoginModal';

const HeroSection = () => {
  return (
    <>
      
          {/* Top Section  */}


                <div className="flex justify-center gap-y-3 flex-col items-center mb-4">
                <div><img
                src="https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Tribhuvan_University_logo.svg/1200px-Tribhuvan_University_logo.svg.png"
                alt="TU-logo"
                className="h-16"
                />
                </div> 

                <div><h2 className="text-primary-focus font-bold text-5xl ">Tribhuwan University</h2></div>

                <div><h2 className="text-primary font-semibold text-2xl ">Pashchimanchal Campus</h2></div>

                <div><h2 className="text-primary font-medium text-1xl ">Lamachaur, Pokhara, Nepal</h2></div>
                </div>
        
        




         {/* Card Section  */}

         {/* Student */}

                      <div className="flex flex-col font-sans items-center md:flex-row md:justify-center md:items-start">
                      <div className="card-compact w-80 md:w-96 bg-gray-100 shadow-xl mb-4 md:mb-0 md:mr-4">
                      <figure className="px-10 pt-10">
                      <img
                      src="https://cdn-icons-png.flaticon.com/512/30/30523.png?w=740&t=st=1690734234~exp=1690734834~hmac=5042c64a37816dfb62cc052d2c9b803ad51020a4002e391c6f516010b2b75a78"
                      alt="Student"
                      className="rounded-xl outline-none"
                      />
                      </figure>
                      <div className="card-body items-center text-center">
                      <h2 className="card-title text-primary-focus">Student Login</h2>
                      <p className="text-neutral font-medium">
                      Welcome to your learning journey, where curiosity and dedication unlock a world of knowledge, leading to endless possibilities.
                      </p>
                      <div className="card-actions">
                      <button className="btn  hover:bg-primary-focus bg-primary btn-primary" onClick={()=>window.my_modal_5.showModal()}>Login As Student</button>
                      <dialog id="my_modal_5" className="modal modal-bottom sm:modal-middle">
                      <form method="dialog" className="modal-box">
                      {/* <h3 className="font-bold text-lg">Hello!</h3> */}
                      <p className="py-4"><LoginModal title={"Student"} id={1}/></p>
                      <div className="modal-action">
                      {/* if there is a button in form, it will close the modal */}
                      <button className="btn">Close</button>
                      </div>
                      </form>
                      </dialog>

                      </div>
                      </div>
                      </div>




                                     {/* Admin  */}
              <div className="card-compact w-80 md:w-96 bg-gray-100 shadow-xl mb-4 md:mb-0 md:mx-4">
              <figure className="px-10 pt-10">
              <img
              src="https://cdn-icons-png.flaticon.com/512/44/44357.png?w=740&t=st=1690736776~exp=1690737376~hmac=91dfef1ba1acf2a50fa89673d54e1ee0ec0168947c4b3b9e4734100529b8148f"
              alt="Admin"
              className="rounded-xl outline-none"
              />
              </figure>
              <div className="card-body items-center text-center">
              <h2 className="card-title text-primary-focus">Admin Login</h2>
              <p className="text-neutral font-medium">
              Welcome, administrator! Embrace your power, manage with integrity, and impact the organization for success!
              </p>
              <div className="card-actions">
              <button className="btn  hover:bg-primary-focus bg-primary btn-primary" onClick={()=>window.my_modal_4.showModal()}>Login As Admin</button>
              <dialog id="my_modal_4" className="modal modal-bottom sm:modal-middle">
              <form method="dialog" className="modal-box">
              {/* <h3 className="font-bold text-lg">Hello!</h3> */}
              <p className="py-4"><LoginModal title={"Admin"} id={2}/></p>
              <div className="modal-action">
              {/* if there is a button in form, it will close the modal */}
              <button className="btn">Close</button>
              </div>
              </form>
              </dialog>
              </div>
              </div>
              </div>



                    {/* Teacher */}

              <div className="card-compact w-80 md:w-96 bg-gray-100 shadow-xl">
              <figure className="px-10 pt-10">
              <img
              src="https://cdn-icons-png.flaticon.com/512/90/90477.png?w=740&t=st=1690734320~exp=1690734920~hmac=42268fdf1b14f81674d67a13329ef8cba9c25f3c1e4f196efc210a3d9a1bc2f5"
              alt="Teacher"
              className="rounded-xl outline-none"
              />
              </figure>
              <div className="card-body items-center text-center">
              <h2 className="card-title text-primary-focus">Teacher Login</h2>
              <p className="text-neutral font-medium">
              Unleash the power of knowledge as superheroes in the classroom! Inspire the future and shape a brighter tomorrow together!
              </p>
              <div className="card-actions">
              <button className="btn  hover:bg-primary-focus bg-primary btn-primary" onClick={()=>window.my_modal_3.showModal()}>Login As Teacher</button>
              <dialog id="my_modal_3" className="modal modal-bottom sm:modal-middle">
              <form method="dialog" className="modal-box">
              {/* <h3 className="font-bold text-lg">Hello!</h3> */}
              <p className="py-4"><LoginModal title={"Teacher"} id={3}/></p>
              <div className="modal-action">
              {/* if there is a button in form, it will close the modal */}
              <button className="btn">Close</button>
              </div>
              </form>
              </dialog>
              </div>
              </div>
              </div>
              </div>
      
    </>
  );
};

export default HeroSection;






