import React from 'react'
import SignupCredentialPanel from '../components/panel/SignupCredentialPanel'
import SignupProfilePanel from '../components/panel/SignupProfilePanel'
class SignupPage extends React.Component {
  render() {
    return (
      <div>
        <SignupCredentialPanel />
        <SignupProfilePanel />
      </div>
    )
  }
}
export default SignupPage;