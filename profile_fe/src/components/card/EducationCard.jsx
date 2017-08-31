import React from 'react';
import $ from 'jquery';
import FormConfirmPanel from 'components/panel/common/FormConfirmPanel'
var CONSTANTS = require('utils/constants');

class EducationCard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      education: {
        "Start time": props.education.start_t,
        "End time": props.education.end_t,
        "School Name": props.education.school,
        "Major": props.education.major,
        "Degree": props.education.degree,
        education_id: props.education.education_id,
        uid: props.education.uid,
      },
      editState: 0
    };
  }
  editState = {
    0: 'view',
    1: 'edit'
  };

  skipField = new Set(['uid', 'education_id']);

  old_education = {};

  doDelete = () => {
    var self = this;
    $.ajax(CONSTANTS.DELETE_EDUCATION_URL, {
      xhrFields: { withCredentials: true },
      method: 'POST',
      data: {
        'education_id': this.state.education.education_id
      },
      success: function (res) {
        if (res.success == 0) {
          alert(res.msg);
          return;
        }
        window.location.reload();
      }
    });
  };

  doUpdate = () => {
    var self = this;
    var education = {
      start_t: this.state.education["Start time"],
      end_t: this.state.education['End time'],
      school: this.state.education["School Name"],
      major: this.state.education['Major'],
      degree: this.state.education['Degree'],
      education_id: this.state.education.education_id,
      uid: this.state.education.uid
    };

    $.ajax(CONSTANTS.UPDATE_EDUCATION_URL, {
      xhrFields: { withCredentials: true },
      method: 'POST',
      data: {
        'education_id': this.state.education.education_id,
        'education': JSON.stringify(education)
      },
      success: function (res) {
        if (res.success == 0) {
          alert(res.msg);
          return;
        }
        window.location.reload();
      }
    });
  };

  onPropertyChange = (event) => {
    var education = this.state.education;
    education[event.target.name] = event.target.value;
    this.setState({
      education: education
    });
  };

  onEditClick = () => {
    this.old_education = Object.assign({}, this.state.education);
    this.setState({
      editState: 1
    })
  };

  onSubmitUpdate = () => {
    this.doUpdate();
  };

  onDeleteClick = () => {
    this.doDelete();
  };

  onCancelUpdate = () => {
    this.setState({
      education: this.old_education,
      editState: 0
    });
  };

  renderEducationCard = () => {
    var self = this;
    var view = [];
    $.each(self.state.education, function (key, value) {
      if (self.skipField.has(key)) {
        return;
      }
      var field;
      if (self.state.editState == 0) {
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

  renderControls = () => {
    var buttons;
    if (this.state.editState == 0) {
      buttons = (
        <div>
          <button onClick={ this.onEditClick }>Edit</button>
          <button onClick={ this.onDeleteClick }>Delete</button>
        </div>
      );
    }
    else buttons = null;
    return buttons;
  };

  renderConfirmControl = () => {
    if (this.state.editState != 1) {
      return null;
    }
    else return (
      <FormConfirmPanel submit={this.onSubmitUpdate} cancel={this.onCancelUpdate} />
    );
  };

  render() {
    return (
      <div>
        { this.renderEducationCard() }
        { this.renderControls() }
        { this.renderConfirmControl() }
        {}
      </div>
    );
  };
};

export default EducationCard;