import React from 'react'

class SignupCredentialPanel extends React.Component {
  render() {
    return (
      <div>
        <div>
          <span>Username:</span><input />
        </div>
        <div>
          <span>Password:</span><input />
        </div>
        <div>
          <span>Repeat Password:</span><input />
        </div>
        <hr />
      </div>
    )
  }
}
export default SignupCredentialPanel;