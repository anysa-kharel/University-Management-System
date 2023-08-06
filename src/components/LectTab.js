import React,{Component} from 'react';
import AddLect from "./AddLect";
import { Link } from 'react-router-dom';


class LectTab extends Component{

constructor(){
    super();
    this.state={
        data:[]
    };
}


fetchData(){
    fetch('http://127.0.0.1:8000/lecturer/')
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

    deleteData(id){
      fetch('http://127.0.0.1:8000/lecturer/update/'+id+'/',{
          method:'DELETE',
          body:JSON.stringify(this.state),
      })
      .then(response=>response)
      .then((data)=>{
          if(data){
              this.fetchData();
          }
      });
  }


    render()
    {

        const lectData=this.state.data;
        const rows=lectData.map((e)=>
        <tr>
        {/* <th>1</th> */}
        <td>{e.id}</td>
        <td>{e.lecturer_number}</td>
        <td>{e.name}</td>
        <td>{e.room_number}</td>
        <td>
                    <Link to={'/update/'+e.id} className="btn bg-primary text-white mr-2">Update</Link>
                    <button onClick={()=>this.deleteData(e.id)} className="btn text-white bg-red-600">Delete</button>
                </td>
      </tr>


        );
  return (
   <>
   

       {/* BUtton  */}
       <div className="pe-0">

<button className="btn  hover:bg-primary-focus bg-primary btn-primary " onClick={()=>window.my_modal_3.showModal()}>Add Lecturer</button>
 <dialog id="my_modal_3" className="modal modal-bottom sm:modal-middle">
 <form method="dialog" className="modal-box">
 
 <p className="py-4"><AddLect/></p>
 <div className="modal-action">

 <button className="btn">Close</button>
 </div>
 </form>
 </dialog>
 </div>




   <div className="overflow-x-auto">
  <table className="table">
    {/* head */}
    <thead>
      <tr>
        {/* <th></th> */}
        <th>S.N.</th>
        <th>Lecturer No</th>
        <th>Name</th>
        <th>Room No</th>
        <th>Actions</th>
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

export default LectTab
