import React from 'react';
import Cookies from 'js.cookie';
import $ from 'jquery';
import ProfilePanel from 'components/panel/editablePanel/ProfilePanel';
import SummaryPanel from 'components/panel/editablePanel/SummaryPanel';
import EducationList from 'components/list/EducationList';
var CONSTANTS = require('utils/constants');

class DashboardPage extends React.Component {
  constructor(props) {
    super(props);
  };

  render() {
    return (
      <div>
        <ProfilePanel />
        <SummaryPanel />
        <EducationList />
      </div>
    )
  };
}

export default DashboardPage;