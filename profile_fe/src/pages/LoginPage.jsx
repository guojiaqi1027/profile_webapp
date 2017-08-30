import React from 'react'
import NavigatorPanel from '../components/panel/NavigatorPanel'
import LoginPanel from '../components/panel/LoginPanel'
import $ from 'jquery'
import Cookies from 'js.cookie'
import UTILS from '../utils/utils'
var CONSTANTS = require('../utils/constants');


class LoginPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: ''
    }
  }

  onUsernameChange = (event) => {
    var username = event.target.value;
    this.setState({
      username: username
    });
  }

  onPasswordChange = (event) => {
    var password = event.target.value;
    this.setState({
      password: password
    });
  }

  submit = () => {
    var username = this.state.username;
    var password = this.state.password;
    $.ajax(CONSTANTS.LOGIN_URL, {
      data: {
        'username': this.state.username,
        'password': this.state.password
      },
      xhrFields: { withCredentials: true },
      method: 'POST',
      success: function (res) {
        if (res.success == 0) {
          alert(res.msg);
          return;
        }
        window.location.replace("/");
      },
      error: function(res) {
      }
    });
  }

  render() {
    return (
      <LoginPanel onUsernameChange={ this.onUsernameChange }
                  onPasswordChange={ this.onPasswordChange }
                  submit={ this.submit }
      />
    )
  }
}

export default LoginPage;