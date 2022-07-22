import { useState, useLayoutEffect } from 'react'
import axios from 'axios'
function Home() {
  const [name, setName] = useState('Guest')
  useLayoutEffect(()=>{
    (async()=>{
      try{
        const {data} = await axios.get('user')
        setName(data.name)
      }
      catch(e){
        return 
      }
    })()
  }, [])
  return (
    <div className='home'>
        <h1>Hi {name}!</h1>
    </div>
  )
}

export default Home