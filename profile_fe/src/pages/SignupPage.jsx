import React from 'react'
import SignupCredentialPanel from '../components/panel/signup/SignupCredentialPanel'
import SignupProfilePanel from '../components/panel/signup/SignupProfilePanel'
import FormConfirmPanel from '../components/panel/common/FormConfirmPanel'
import $ from 'jquery'

var CONSTANTS = require('../utils/constants');

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
    $.ajax(CONSTANTS.AUTH_SIGNUP_URL, {
      data: {
        'credential': JSON.stringify(this.state.credential),
        'profile': JSON.stringify(this.state.profile)
      },
      method: 'POST',
      success: function(res) {
        alert(res);
      },
      error: function(res) {
        alert(res);
      }
    });
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