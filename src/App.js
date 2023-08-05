import React from 'react'
import HeroSection from './components/HeroSection'
import {  Route, Routes } from 'react-router-dom';
import Dashboardstudent from './components/Dashboard/Dashboardstudent';
import Dashboardadmin from './components/Dashboard/Dashboardadmin';
import Dashboardteacher from './components/Dashboard/Dashboardteacher';

const App = () => {
  return (
   <div className='app'>
<Routes>
    <Route index element={<HeroSection/>}/>
   <Route exact path="/2" element={<Dashboardadmin/>}/>
   <Route exact path="/1" element={<Dashboardstudent/>}/>
   <Route exact path="/3" element={<Dashboardteacher/>}/>

</Routes>
    
   </div>
  )
}

export default App
