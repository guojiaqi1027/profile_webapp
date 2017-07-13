import React from 'react'

class LoginPanel extends React.Component {
    render() {
        return (
        <div>
            <div>
                <span>username:</span>
                <input />
            </div>
            <div>
                <span>password:</span>
                <input />
            </div>
            <button>Login</button>
            <button>Register</button>
        </div>
        )
    }
}

export default LoginPanel;