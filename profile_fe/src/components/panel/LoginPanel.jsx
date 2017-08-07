import React from 'react'

class LoginPanel extends React.Component {
  constructor(props) {
    super(props);
    this.onUsernameChange = props.onUsernameChange;
    this.onPasswordChange = props.onPasswordChange;
    this.submit = props.submit;
  }
  render() {
        return (
        <div>
            <div>
                <span>username:</span>
                <input name='username' onChange={ this.onUsernameChange }/>
            </div>
            <div>
                <span>password:</span>
                <input name='password' onChange={ this.onPasswordChange }/>
            </div>
            <a onClick={ this.submit }>Login</a>
            <a href='/signup'>Register</a>
        </div>
        )
  }
}

export default LoginPanel;