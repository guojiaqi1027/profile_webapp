import React from 'react'
import SignupCredentialPanel from '../components/panel/signup/SignupCredentialPanel'
import SignupProfilePanel from '../components/panel/signup/SignupProfilePanel'
import FormConfirmPanel from '../components/panel/common/FormConfirmPanel'
class SignupPage extends React.Component {
  render() {
    return (
      <div>
        <SignupCredentialPanel />
        <SignupProfilePanel />
        <FormConfirmPanel />
      </div>
    )
  }
}
export default SignupPage;