import React from 'react'
import HeroSection from './components/HeroSection'
<<<<<<< HEAD
import { Routes, Route } from 'react-router-dom'
import Dashboard from './components/Dashboard'
import LectTab from './components/LectTab'
import StuTab from './components/StuTab'


const App = () => {
  return (
   <>

<Routes>
    <Route index element={<HeroSection/>}/>
    <Route exact path="/dashboard" element={<Dashboard/>}/>
    <Route exact path="/lecttab" element={<LectTab/>}/>
    <Route exact path="/stutab" element={<StuTab/>}/>
</Routes>

   </>
=======
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
>>>>>>> 38b4184b0f2f4f385978762bc607c806c135ba05
  )
}

export default App
