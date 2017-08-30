import React from 'react'
import SignupCredentialPanel from '../components/panel/signup/SignupCredentialPanel'
import SignupProfilePanel from '../components/panel/signup/SignupProfilePanel'
import FormConfirmPanel from '../components/panel/common/FormConfirmPanel'
import AlertPanel from '../components/panel/common/AlertPanel'
import $ from 'jquery'
import Cookies from 'js.cookie'
import UTILS from '../utils/utils'

var CONSTANTS = require('../utils/constants');
class SignupPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      credential: {
      },
      profile: {
      },
      password_match: true,
      error_msg: " "
    }
  }

  onCredentialChange = (event) => {
    var credential = this.state.credential;
    credential[event.target.name] = event.target.value;
    this.setState({
      credential: credential,
      password_match: credential.password == credential.re_password,
      error_msg: credential.password == credential.re_password ? "" : "Password not match"
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
    if (this.state.password_match) {
      $.ajax(CONSTANTS.AUTH_SIGNUP_URL, {
        data: {
          'credential': JSON.stringify(this.state.credential),
          'profile': JSON.stringify(this.state.profile)
        },
        method: 'POST',
        success: function(res) {
          if (res.success == 0) {
            alert(res.msg);
            return;
          }
          var ret = res.ret;
        },
        error: function(res) {
        }
      });
    }
    else {
      alert('password not match');
    }
  }
  cancelForm = () => {
    window.location.replace('/');
  }
  render() {
    return (
      <div>
        <AlertPanel msg={ this.state.error_msg } />
        <SignupCredentialPanel onChange={ this.onCredentialChange }/>
        <SignupProfilePanel onChange={ this.onProfileChange }/>
        <FormConfirmPanel submit={ this.submitForm } cancel={ this.cancelForm }/>
      </div>
    )
  }
}
export default SignupPage;