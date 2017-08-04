import React from 'react'

class SignupCredentialPanel extends React.Component {
  constructor(props) {
    super(props);
    this.onChange = props.onChange;
  }
  render() {
    return (
      <div>
        <div>
          <span>Username:</span><input name='username' onChange={ this.onChange }/>
        </div>
        <div>
          <span>Password:</span><input type='password' name='password' onChange={ this.onChange }/>
        </div>
        <div>
          <span>Repeat Password:</span><input type='password' name='re_password' onChange={ this.onChange }/>
        </div>
        <hr />
      </div>
    )
  }
}
export default SignupCredentialPanel;