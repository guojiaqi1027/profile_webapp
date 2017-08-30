import React from 'react';
import ReactDOM from 'react-dom';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import StartupPage from './pages/StartupPage';
import NavigatorPanel from './components/panel/NavigatorPanel';
import registerServiceWorker from './registerServiceWorker';
import DashboardPage from './pages/DashboardPage';
import { Route, Link, BrowserRouter, Switch } from 'react-router-dom'
import Cookies from 'js.cookie';

var startup = Cookies.get('token') ? DashboardPage : StartupPage;
ReactDOM.render(
  (
    <div>
      <NavigatorPanel />
      <BrowserRouter >
        <Switch>
          <Route exact path="/" component={startup} />
          <Route path="/login" component={LoginPage} />
          <Route path="/signup" component={SignupPage} />
          <Route path="/dashboard" component={DashboardPage} />
        </Switch>
      </BrowserRouter>
    </div>
  ), 
  document.getElementById('root')); 
  registerServiceWorker();