import { useEffect, useState } from 'react'
import './App.css'
import axios from 'axios'



function App() {

  const getUser = async ()=>{
    try {

       const res = await axios.get("http://127.0.0.1:8000/api/hello/")
       console.log(res)

    } catch (error) {

      console.log(error)
      
    }

  }

  
  useEffect(()=>{getUser()},[])

  return (
    <>
      <div>

      </div>
    </>
  )
}

export default App
