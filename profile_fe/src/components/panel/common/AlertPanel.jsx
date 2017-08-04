import React from 'react'
class AlertPanel extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <span> { this.props.msg } </span>
      </div>
    )
  }
}
export default AlertPanel;