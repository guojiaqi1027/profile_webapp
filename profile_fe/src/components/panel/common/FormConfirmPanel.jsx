import React from 'react';

class FormConfirmPanel extends React.Component {
  constructor(props) {
    super(props);
    this.submit = props.submit;
    this.cancel = props.cancel;
  }
  render () {
    return (
      <div>
        <a onClick= {this.submit} >Submit</a>
        <a onClick={this.cancel}>Cancel</a>
      </div>
    )
  };
}
export default FormConfirmPanel;