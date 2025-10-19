import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Leaderboard from './Leaderboard';
import './App.css'

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={<Leaderboard/>}/>
          <Route path='/leaderboard' element={<Leaderboard/>}/>
        </Routes>
      </Router>
    </>
  )
}

export default App
