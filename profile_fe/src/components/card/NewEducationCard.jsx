import React from 'react';
import $ from 'jquery';

var CONSTANTS = require('utils/constants');

class NewEducationCard extends React.Component {
  constructor (props) {
    super(props);
    this.state = {
      education: {
        "Start time": "",
        "End time": "",
        "School Name": "",
        "Major": "",
        "Degree": ""
      }
    };
  };

  doAdd = () => {
    var self = this;
    var education = {
      start_t: this.state.education['Start time'],
      end_t: this.state.education['End time'],
      school: this.state.education['School Name'],
      major: this.state.education['Major'],
      degree: this.state.education['Degree']
    };

    $.ajax(CONSTANTS.ADD_EDUCATION_URL, {
      xhrFields: { withCredentials: true },
      method: 'POST',
      data: {
        education: JSON.stringify(education)
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
    })
  };

  onSubmitClick = (event) => {
    this.doAdd();
  };

  renderEducation = () => {
    var self = this;
    var view = [];
    $.each(self.state.education, function (key, value) {
      var item = <div> {key} : <input name={ key } value={ value } onChange={ self.onPropertyChange }></input></div>;
      view.push(item);
    });
    return (
      <div>{ view }</div>
    );
  };

  renderControls = () => {
    return (
      <div>
        <button onClick={ this.onSubmitClick }>Submit</button>
        <button onClick={ this.props.onCancelClick }>Cancel</button>
      </div>
    );
  };

  render() {
    return (
      <div>
        { this.renderEducation() }
        { this.renderControls() }
      </div>
    );
  }
};

export default NewEducationCard;