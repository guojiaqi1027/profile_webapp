import React from 'react'
import Cookies from 'js.cookie'
import $ from 'jquery'

var CONSTANTS = require('../../utils/constants');

class NavigatorPanel extends React.Component {
  constructor(props) {
    super(props);
    this.init();
  }

  init = () => {
    this.state = {
      profile: null
    };
    if (Cookies.get('token')) {
      this.getProfile();
    }
  }

  getProfile = () => {
    var self = this;
    $.ajax(CONSTANTS.GET_PROFILE_URL, {
      method: 'POST',
      xhrFields: { withCredentials: true },
      success: function (res) {
        if (res.success == 0) {
          alert(res.msg);
          return;
        }
        var profile = res.profile;
        self.setState({
          profile: profile
        });
      },
      error: false
    });
  }

  onLogoutClick = (event) => {
     this.setState({
      profile: null
    });
    Cookies.remove('token');
    window.location.replace('/');
    return;
  }

  renderUserControl = () => {
    if (this.state.profile) {
      return (
        <div>
          <span> { this.state.profile.name }</span>
          <button onClick={ this.onLogoutClick }> Log out </button>
        </div>
      );
    }
    return null;
  }

  render() {
    return (
    <div>
      { this.renderUserControl() }
      <h3>Online Profile System</h3>
      <hr />
    </div>
    )
  }
}

export default NavigatorPanel;