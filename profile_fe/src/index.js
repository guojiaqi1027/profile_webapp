import React from 'react';
import ReactDOM from 'react-dom';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import StartupPage from './pages/StartupPage';
import NavigatorPanel from './components/panel/NavigatorPanel';
import registerServiceWorker from './registerServiceWorker';
import { Route, Link, BrowserRouter, Switch } from 'react-router-dom'

ReactDOM.render(
  (
    <div>
      <NavigatorPanel />
      <BrowserRouter >
        <Switch>
          <Route exact path="/" component={StartupPage} />
          <Route path="/login" component={LoginPage} />
          <Route path="/signup" component={SignupPage} />
        </Switch>
      </BrowserRouter>
    </div>
  ), 
  document.getElementById('root')); 
  registerServiceWorker();