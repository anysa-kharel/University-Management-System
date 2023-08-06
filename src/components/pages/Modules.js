
import React, { useState } from 'react';
import { Space, Typography, Card, Statistic } from 'antd';
import { MdOutlineLibraryBooks } from 'react-icons/md';
import {BiSearch} from 'react-icons/bi';
import SemesterI from './SemesterI';
import { Link } from 'react-router-dom';




function Modules() {


  
  const options = [
    { label: 'Semester-I', link:"/semester1", value: 'option1' },
    { label: 'Semester-II', value: 'option2' },
    { label: 'Semester-III', value: 'option3' },
  ];

  const [selectedOption, setSelectedOption] = useState('');

  const handleOptionChange = (value) => {
    setSelectedOption(value);
    
  };

  return (
    <div>
      <Typography.Title level={6}>Courses of all Faculties </Typography.Title>
      <Space direction='horizontal'>
  
        <Electronics
          icon={<MdOutlineLibraryBooks style={{ color: "#2a5279", borderRadius: 20, fontSize: 40, padding: 8 }} />}
          title={"Electronics Faculty"}
          options={options}
          selectedOption={selectedOption}
          onChange={handleOptionChange}
        />
         <Computer
          icon={<MdOutlineLibraryBooks style={{ color: "#2a5279", borderRadius: 20, fontSize: 40, padding: 8 }} />}
          title={"Computer Faculty"}
         
        />
         <Geomatics
          icon={<MdOutlineLibraryBooks style={{ color: "#2a5279", borderRadius: 20, fontSize: 40, padding: 8 }} />}
          title={"Geomatics Faculty"}
          
        />
         <Automobile
          icon={<MdOutlineLibraryBooks style={{ color: "#2a5279", borderRadius: 20, fontSize: 40, padding: 8 }} />}
          title={"Automobile Faculty"}
          
        />
        
      </Space>
    </div>
  );
}

function Electronics({ title, icon, options, selectedOption, onChange }) {
  const [
    field,setField
 ]=useState("");

 const handleClick=(e)=>{
  console.log("clicked")
  return (<SemesterI/>
  
  );
 }
 
  return (
    <Card>
      <Space direction='horizontal'>
        {icon}
        <Statistic title={title} />
      

        <select
            value={field}
            onChange={(e) => setField(e.currentTarget.value)}
          >
            <option value="">Sector, Interested field</option>
            <option value="Environment">Environment</option>
            <option value="Business">Business</option>
            <option value="Public health">Public health</option>
            <option value="Technology">Technology</option>
            <option value="Others">Others</option>
          </select>
          
          <Link to="/semester1">
            <BiSearch size={20} />
          </Link>

      </Space>
    </Card>
  );
}

function Computer({ title, icon, options, selectedOption, onChange }) {
  return (
    <Card>
      <Space direction='horizontal'>
        {icon}
        <Statistic title={title} />
        <select value={selectedOption} onChange={(event) => onChange(event.target.value)}>
          <option value="">Select an option</option>
        
        </select>
      </Space>
    </Card>
  );
}

function Geomatics({ title, icon, options, selectedOption, onChange }) {
  return (
    <Card>
      <Space direction='horizontal'>
        {icon}
        <Statistic title={title} />
        <select value={selectedOption} onChange={(event) => onChange(event.target.value)}>
          <option value="">Select an option</option>
       
        </select>
      </Space>
    </Card>
  );
}

function Automobile({ title, icon, options, selectedOption, onChange }) {
  return (
    <Card>
      <Space direction='horizontal'>
        {icon}
        <Statistic title={title} />
        <select value={selectedOption} onChange={(event) => onChange(event.target.value)}>
          <option value="">Select an option</option>
         
        </select>
      </Space>
    </Card>
  );
}


export default Modules;






