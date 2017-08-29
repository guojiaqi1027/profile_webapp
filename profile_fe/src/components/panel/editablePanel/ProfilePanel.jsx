import React from 'react';
import $ from 'jquery';
import Cookies from 'js.cookie';
import FormConfirmPanel from 'components/panel/common/FormConfirmPanel';
var CONSTANTS = require('utils/constants');
class ProfilePanel extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      profile: {},
      panelState: 0
    };
    this.init();
  };
  old_profile = {};
  panelStates = {
    0: 'Initialing',
    1: 'View',
    2: 'Edit'
  };

  init = () => {
    var self = this;
    var uid = Cookies.get('uid');
    if (uid) {
      $.ajax(CONSTANTS.GET_PROFILE_URL, {
        data: {
          uid: uid
        },
        xhrFields: { withCredentials: true },
        method: 'POST',
        success: function (res) {
          if (res.success == 0) {
            alert(res.msg);
            return;
          }
          else {
            self.setState({
              profile: res.profile,
              panelState: 1
            });
          }
        }
      });
    }
  };

  onPropertyChange = (event) => {
    var profile = this.state.profile;
    profile[event.target.name] = event.target.value;
    var state = this.state;
    this.setState({
      uid: state.uid,
      profile: profile,
      panelState: state.panelState
    });
  };

  onEditClick = () => {
    this.old_profile = Object.assign({}, this.state.profile);
    console.log(this.old_profile);
    this.setState({
      panelState: 2
    });
  };

  onSubmitUpdate = () => {

  };

  onCancelUpdate = () => {
    console.log(this.old_profile);
    this.setState({
      profile: this.old_profile,
      panelState: 1
    });
  };

  renderInitializing = () => {
    return (
      <div>
        <h2>Loading...</h2>
      </div>
    );
  };

  renderUserProfile = () => {
    var self = this;
    var view = [];
    $.each(self.state.profile, function (key, value) {
      var field;
      if (self.state.panelState == 1) {
        field = <span>{ value }</span>;
      }
      else {
        field = <input name={ key } value={ value } onChange={ self.onPropertyChange }></input>;
      }
      var item = <div>{ key }:{ field }</div>;
      view.push(item);
    });
    return (
      <div>
        { view }
      </div>
    );
  };

  renderPanelHead = () => {
    var button = this.state.panelState == 1 ? (<button onClick={ this.onEditClick }>Edit</button>) : null;
    return (
      <div>
        <h4>Profile</h4>
        { button }
      </div>
    );
  };

  renderConfirmControl = () => {
    if (this.state.panelState != 2) {
      return null;
    }
    else return (
      <FormConfirmPanel submit={this.onSubmitUpdate} cancel={this.onCancelUpdate} />
    );
  };

  render() {
    if (this.state.panelState == 0) {
      return (
        <div>
          { this.renderInitializing() }
        </div>
      );
    }
    return (
      <div>
        { this.renderPanelHead() }
        { this.renderUserProfile() }
        { this.renderConfirmControl() }
      </div>
    );
  }
}

export default ProfilePanel;