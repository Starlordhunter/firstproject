import React, { useState } from 'react';
import './App.css';
import Login from './components/login';
import Students from './components/students';
import Teachers from './components/teachers';
import Principal from './components/principal';
import { Router,Route,Routes, Link} from 'react-router-dom';
import ProtectedRoutes from './ProtectedRoutes';


function App() {

  const [token, setToken] = useState('');
  const [role, setRole] = useState();

  const userLogin = (tok) => {
    // console.log(tok);
    setToken(tok);
    
  }

  const userRole = (rol) =>{

    setRole(rol)
  }

  return (
    <div className='App'>
      {/* <Login userLogin={userLogin}/>
      <Teachers token={token}/>
      <Students token={token}/>
      <Principal token={token}/> */}
      <nav
        style={{
          borderBottom: "solid 1px",
          paddingBottom: "1rem",
        }}
      >
        <Link to="/login">Log in</Link> |{" "}
        <Link to="/teachers">Teachers</Link> |{" "}
        <Link to="/students">Students</Link> |{" "}
        <Link to="/principal">Principal</Link>
      </nav>

      <Routes>
        <Route path='/login' element={<Login userLogin={userLogin} userRole={userRole}/>}/>
        <Route element={<ProtectedRoutes/>}>
          <Route path='/teachers' element={<Teachers token={token} role={role}/>}/>
          <Route path='/students' element={<Students token={token}/>}/>
          <Route path='/principal' element={<Principal token={token}/>}/>
        </Route>
        
      </Routes>
    </div>
  );
}

export default App;
