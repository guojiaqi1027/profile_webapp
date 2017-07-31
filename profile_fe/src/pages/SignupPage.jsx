import React from 'react'
import SignupCredentialPanel from '../components/panel/signup/SignupCredentialPanel'
import SignupProfilePanel from '../components/panel/signup/SignupProfilePanel'
import FormConfirmPanel from '../components/panel/common/FormConfirmPanel'
class SignupPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      credential: {
      },
      profile: {
      }
    }
  }
  onCredentialChange = (event) => {
    var credential = this.state.credential;
    credential[event.target.name] = event.target.value;
    this.setState({
      credential: credential
    });
  }

  onProfileChange = (event) => {
    var profile = this.state.profile;
    profile[event.target.name] = event.target.value;
    this.setState({
      profile: profile
    });
  }

  submitForm = () => {
    alert(this.state);
  }

  render() {
    return (
      <div>
        <SignupCredentialPanel onChange={ this.onCredentialChange }/>
        <SignupProfilePanel onChange={ this.onProfileChange }/>
        <FormConfirmPanel submit={ this.submitForm }/>
      </div>
    )
  }
}
export default SignupPage;