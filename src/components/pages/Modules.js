
import React, { useState } from 'react';
import { Space, Typography, Card, Statistic } from 'antd';
import { MdOutlineLibraryBooks } from 'react-icons/md';
import AddCourse from './AddCourse';

function Modules() {

  
  const options = [
    { label: 'Semester-I', value: 'option1' },
    { label: 'Semester-II', value: 'option2' },
    { label: 'Semester-III', value: 'option3' },
  ];

  const [selectedOption, setSelectedOption] = useState('');

  const handleOptionChange = (value) => {
    setSelectedOption(value);
    // Additional logic or actions based on the selected value can be performed here.
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
          options={options}
          selectedOption={selectedOption}
          onChange={handleOptionChange}
        />
         <Geomatics
          icon={<MdOutlineLibraryBooks style={{ color: "#2a5279", borderRadius: 20, fontSize: 40, padding: 8 }} />}
          title={"Geomatics Faculty"}
          options={options}
          selectedOption={selectedOption}
          onChange={handleOptionChange}
        />
         <Automobile
          icon={<MdOutlineLibraryBooks style={{ color: "#2a5279", borderRadius: 20, fontSize: 40, padding: 8 }} />}
          title={"Automobile Faculty"}
          options={options}
          selectedOption={selectedOption}
          onChange={handleOptionChange}
        />
        
      </Space>
    </div>
  );
}

function Electronics({ title, icon, options, selectedOption, onChange }) {
  return (
    <Card>
      <Space direction='horizontal'>
        {icon}
        <Statistic title={title} />
        <select value={selectedOption} onChange={(event) => onChange(event.target.value)}>
          <option value="">Select an option</option>
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))
          }
        </select>
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
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))
          }
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
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))
          }
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
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))
          }
        </select>
      </Space>
    </Card>
  );
}


export default Modules;
