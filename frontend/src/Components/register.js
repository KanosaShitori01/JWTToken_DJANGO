import React from 'react'

function Register() {
  return (
    <main className="form-signup">
        <form>
            <h1 className="h3 mb-3 fw-normal">Register</h1>
            <div className="form-floating">
                <input type="text" className="form-control" id="floatingInput" placeholder="Name" />
                <label htmlFor="floatingInput">Name</label>
            </div>
            <div className="form-floating">
                <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com" />
                <label htmlFor="floatingInput">Email address</label>
            </div>
            <div className="form-floating">
                <input type="password" className="form-control" id="floatingPassword" placeholder="Password" />
                <label htmlFor="floatingPassword">Password</label>
            </div>
            <button className="w-100 btn btn-lg btn-primary" type="submit">Register</button>
        </form>
    </main>
  )
}

export default Register