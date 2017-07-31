import React from 'react'

class SignupProfilePanel extends React.Component {
  constructor(props) {
    super(props);
    this.onChange = props.onChange;
  }

  render() {
    return (
      <div>
        <div>
          <span>name:</span><input name="name" onChange={ this.onChange }/>
        </div>
        <div>
          <span>title:</span><input name="title" onChange={ this.onChange }/>
        </div>
        <div>
          <span>company:</span><input name="company" onChange={ this.onChange }/>
        </div>
        <div>
          <span>address:</span><input name="address" onChange={ this.onChange }/>
        </div>
        <div>
          <span>birth:</span><input name="birth" onChange={ this.onChange }/>
        </div>
        <div>
          <span>email:</span><input name="email" onChange={ this.onChange }/>
        </div>
        <div>
          <span>phone:</span><input name="phone" onChange={ this.onChange }/>
        </div>
      </div>
    )
  }
}

export default SignupProfilePanel;