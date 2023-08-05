import React,{Component} from 'react';
import AddStudent from './AddStudent';


class StuTab extends Component{

constructor(){
    super();
    this.state={
        data:[]
    };
}


fetchData(){
    fetch('http://127.0.0.1:8000/student')
    .then(response=>response.json())
    .then((data)=>{
    this.setState({data:data});
    console.log(data);
    });
    }
    

    componentDidMount()
    {
    this.fetchData();
    }



    render()
    {

        const lectData=this.state.data;
        const rows=lectData.map((e)=>
        <tr>
        {/* <th>1</th> */}
        <td>{e.student_number}</td>
        <td>{e.name}</td>
        {/* <td>{e.room_number}</td> */}
      </tr>


        );
  return (
   <>
   
             {/* BUtton  */}
              <div className="pe-0">

             <button className="btn  hover:bg-primary-focus bg-primary btn-primary " onClick={()=>window.my_modal_3.showModal()}>Add Student</button>
              <dialog id="my_modal_3" className="modal modal-bottom sm:modal-middle">
              <form method="dialog" className="modal-box">
              {/* <h3 className="font-bold text-lg">Hello!</h3> */}
              <p className="py-4"><AddStudent/></p>
              <div className="modal-action">
              {/* if there is a button in form, it will close the modal */}
              <button className="btn">Close</button>
              </div>
              </form>
              </dialog>
              </div>



         {/* Table  */}
   <div className="">
   
        
 <table className="table">
    {/* head */}
    <thead>
      <tr>
        {/* <th></th> */}
        <th>Student No</th>
        <th>Name</th>
        {/* <th>Room No</th> */}
      </tr>
    </thead>
    <tbody>

    {rows}


    </tbody>
  </table>
</div>
   
   
   </>
  )
}}

export default StuTab
