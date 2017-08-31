import React from 'react';
import $ from 'jquery';
import EducationCard from 'components/card/EducationCard';
import NewEducationCard from 'components/card/NewEducationCard';
var CONSTANTS = require('utils/constants');

class EducationList extends React.Component {
  constructor (props) {
    super(props);
    this.state = {
      educationList: [],
      listState: 0
    };
    this.init();
  };

  listState = {
    0: 'view',
    1: 'Add'
  };

  init = () => {
    var self = this;
    $.ajax(CONSTANTS.GET_EDUCATIONS_URL, {
      xhrFields: { withCredentials: true },
      method: 'POST',
      success: function (res) {
        if (res.success == 0) {
          alert(res.msg);
          return;
        }
        self.setState({
          educationList: res.educations
        });
      }
    });
  };

  onAddClick = () => {
    this.setState({
      listState: 1
    });
  };

  onCancelNewClick = () => {
    this.setState({
      listState: 0
    });
  };

  renderControls = () => {
    if (this.state.listState == 0) {
      return (
        <div>
          <button onClick={ this.onAddClick }>Add</button>
        </div>
      );
    }
    else {
      return null;
    }
  };

  renderList = () => {
    var self = this;
    var list = [];
    $.each(this.state.educationList, function (index, value) {
      var card = <EducationCard education={ value } />;
      list.push(card);
    })
    return (
      <div>
        { list }
      </div>
    );
  };

  renderNewEducation = () => {
    if (this.state.listState == 1) {
      return (
        <div>
          <NewEducationCard onCancelClick={ this.onCancelNewClick } />
        </div>
      )
    }
    else {
      return null;
    }
  };

  render() {
    return (
      <div>
        <h3>Education</h3>
        { this.renderControls() }
        { this.renderNewEducation() }
        { this.renderList() }
      </div>
    );
  };
};

export default EducationList;