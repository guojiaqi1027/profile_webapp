import React from 'react';
import $ from 'jquery';
import Cookies from 'js.cookie';
import FormConfirmPanel from 'components/panel/common/FormConfirmPanel';
import AlertPanel from 'components/panel/common/AlertPanel';
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

  skipField = new Set(['username', 'uid']);

  init = () => {
    var self = this;
    $.ajax(CONSTANTS.GET_PROFILE_URL, {
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
  };

  onPropertyChange = (event) => {
    var profile = this.state.profile;
    profile[event.target.name] = event.target.value;
    var state = this.state;
    this.setState({
      profile: profile,
      panelState: state.panelState
    });
  };

  onEditClick = () => {
    this.old_profile = Object.assign({}, this.state.profile);
    this.setState({
      panelState: 2
    });
  };

  onSubmitUpdate = () => {
    var self = this;
    $.ajax(CONSTANTS.UPDATE_PROFILE_URL, {
      data: {
        profile: JSON.stringify(self.state.profile)
      },
      xhrFields: { withCredentials: true },
      method: 'POST',
      success: function (res) {
        if (res.success == 0 ){
          alert(res.msg);
          return;
        }
        window.location.reload();
      }
    });
  };

  onCancelUpdate = () => {
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
      if (self.skipField.has(key)) {
        return;
      }
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

  renderAlertPanel = () => {
    if (this.state.err_msg) {
      return (<AlertPanel msg={ this.state.error_msg } />);
    }
    else return null;
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
        { this.renderAlertPanel() }
        { this.renderPanelHead() }
        { this.renderUserProfile() }
        { this.renderConfirmControl() }
      </div>
    );
  }
}

export default ProfilePanel;