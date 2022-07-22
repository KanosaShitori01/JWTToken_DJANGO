import axios from 'axios'
import {useState, useLayoutEffect} from 'react'
import { useNavigate } from 'react-router'
// import {brow}
const Message = ({text}) => {
  return(<div className="alert alert-danger text-center" role="alert">
    {text}
  </div>)
}
function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState({text: "", visible: false})
  const navigate = useNavigate()
  const submitLogin = async e => {
    e.preventDefault()
    const status = await axios.post('login', {
      email, password
    }, {withCredentials: true})
    let getStatus = status.status
    if(getStatus !== undefined){
      window.history.go(history.length)
      navigate("/", {replace: true})
    }
    else setMessage({text: "Invalid Email Or Password", visible: true})
  }
  useLayoutEffect(()=>{
    (async()=>{
        const logged = await axios.get("user")
        if(logged.status === 200)
          navigate("/")
    })()  
  }, [])
  return (<>
    {message.visible ? <Message text={message.text}/> : ""} 
    <main className="form-signin">
      <form onSubmit={submitLogin}>
        <h1 className="h3 mb-3 fw-normal">Sign In</h1>
        <div className="form-floating">
          <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com" 
          onChange={e => setEmail(e.target.value)} />
          <label htmlFor="floatingInput">Email address</label>
        </div>
        <div className="form-floating">
          <input type="password" className="form-control" id="floatingPassword" placeholder="Password" 
          onChange={e => setPassword(e.target.value)} />
          <label htmlFor="floatingPassword">Password</label>
        </div>
        <button className="w-100 btn btn-lg btn-primary" 
        type="submit">Sign in</button>
      </form>
    </main>
  </>)
}

export default Login