import React from 'react'
import { Router, Route, Link } from 'react-router'
class StartupPanel extends React.Component {
  render() {
    return (
      <div>
        <a href='/login'>Login</a>
        <a href='/signup'>Signup</a>
      </div>
    )
  }
}
export default StartupPanel;