import React from 'react'
import HeroSection from './components/HeroSection'
import { Routes, Route } from 'react-router-dom'
import Dashboard from './components/Dashboard'
import LectTab from './components/LectTab'
import StuTab from './components/StuTab'
import Dashboardstudent from './components/Dashboard/Dashboardstudent';
import Dashboardadmin from './components/Dashboard/Dashboardadmin';
import Dashboardteacher from './components/Dashboard/Dashboardteacher';
import SemesterI from './components/pages/SemesterI'
import SemesterII from './components/pages/SemesterII'
import SemesterIII from './components/pages/SemesterIII'
import Modules from './components/pages/Modules'

import UpdateLect from './components/UpdateLect'
import UpdateStu from './components/UpdateStu'


const App = () => {
  return (
   <>

<Routes>
    <Route index element={<HeroSection/>}/>
    <Route exact path="/dashboard" element={<Dashboard/>}/>
    <Route exact path="/lecttab" element={<LectTab/>}/>
    <Route exact path="/stutab" element={<StuTab/>}/>
    <Route exact path="/2" element={<Dashboardadmin/>}/>
   <Route exact path="/1" element={<Dashboardstudent/>}/>
   <Route exact path="/3" element={<Dashboardteacher/>}/>
<<<<<<< HEAD
   <Route exact path='/modules' element={<Modules/>}></Route> 
   <Route  exact path="/semester1" element={<SemesterI/>}></Route>
=======
   <Route exact path="/modules" component={Modules} />
   <Route path="/semester1" component={SemesterI} />
>>>>>>> 6e26da9db8aadf3ce112990d332c727de5c134c7
   <Route path="/semester2" component={SemesterII} />
   <Route path="/semester3" component={SemesterIII} />
   
   <Route exact path="/update/:id" element={<UpdateLect/>} />
   <Route exact path="/updates/:id" element={<UpdateStu/>} />
</Routes>
<<<<<<< HEAD
=======



>>>>>>> 6e26da9db8aadf3ce112990d332c727de5c134c7
   </>

  );
}



export default App
