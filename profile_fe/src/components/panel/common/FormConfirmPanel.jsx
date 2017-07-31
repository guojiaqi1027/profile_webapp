import React from 'react';

class FormConfirmPanel extends React.Component {
  constructor(props) {
    super(props);
    this.submit = props.submit;
  }
  render () {
    return (
      <div>
        <a onClick= {this.submit} >Submit</a>
        <a href='/'>Cancel</a>
      </div>
    )
  };
}
export default FormConfirmPanel;