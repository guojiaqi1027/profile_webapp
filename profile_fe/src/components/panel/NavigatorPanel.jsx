import React from 'react'
import Cookies from 'js.cookie'
class NavigatorPanel extends React.Component {
  onLogoutClick = (event) => {
    Cookies.remove('user');
    window.open('/');
    return;
  }
  renderUserControl = () => {
    if (Cookies.get('user')) {
      var user = Cookies.get('user');
      return (
        <div>
          <p> { user.username }</p>
          <p> { user.profile.name}</p>
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