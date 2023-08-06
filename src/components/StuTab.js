import React,{Component} from 'react';
import AddStudent from './AddStudent';
import { Link } from 'react-router-dom';


class StuTab extends Component{

constructor(){
    super();
    this.state={
        data:[]
    };
}



fetchData(){
    fetch('http://127.0.0.1:8000/student/')
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
      fetch('http://127.0.0.1:8000/student/update/'+id+'/',{
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
        <td>{e.student_id}</td>
        <td>{e.student_number}</td>
        <td>{e.name}</td>
        <td>
                    <Link to={'/updates/'+e.student_id} className="btn bg-primary text-white mr-2">Update</Link>
                    <button onClick={()=>this.deleteData(e.student_id)} className="btn text-white bg-red-600">Delete</button>
                </td>
      </tr>


        );
  return (
   <>
   
             {/* BUtton  */}
              <div className="pe-0">

             <button className="btn  hover:bg-primary-focus bg-primary btn-primary " onClick={()=>window.my_modal_3.showModal()}>Add Student</button>
              <dialog id="my_modal_3" className="modal modal-bottom sm:modal-middle">
              <form method="dialog" className="modal-box">
             
              <p className="py-4"><AddStudent/></p>
              <div className="modal-action">
           
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
        <th>S.N.</th>
        <th>Student No</th>
        <th>Name</th>
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

export default StuTab
