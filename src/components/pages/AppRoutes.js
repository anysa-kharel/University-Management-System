import React from 'react'
import {Route,Routes } from 'react-router-dom'
import Dashboardadmin from '../Dashboard/Dashboardadmin'
import Modules from './Modules'

function AppRoutes() {
  return (
  
    <Routes>
      <Route path='/' element={<Dashboardadmin/>}></Route> 
      <Route path='/modules' element={<Modules/>}></Route> 
     
    </Routes>
  
  )
}

export default AppRoutes
