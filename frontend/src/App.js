import logo from './logo.svg';
import './App.css';
import Login from './Components/login';
import Header from './Components/header';
import { Route, Routes } from 'react-router';
import Home from './Components/home';
import Register from './Components/register';
function App() {
  return (
    <div className="App">
      <Header/>
      <Routes>
        <Route path='' element={<Home/>} />
        <Route path='login' element={<Login/>}/>
        <Route path='register' element={<Register/>} />
      </Routes>
    </div>
  );
}

export default App;
