import React from 'react'

class SignupProfilePanel extends React.Component {
  render() {
    return (
      <div>
        <div>
          <span>name:</span><input />
        </div>
        <div>
          <span>title:</span><input />
        </div>
        <div>
          <span>company:</span><input />
        </div>
        <div>
          <span>address:</span><input />
        </div>
        <div>
          <span>birth:</span><input />
        </div>
        <div>
          <span>email:</span><input />
        </div>
        <div>
          <span>phone:</span><input />
        </div>
      </div>
    )
  }
}

export default SignupProfilePanel;