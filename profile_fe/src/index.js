import React from 'react';
import ReactDOM from 'react-dom';
import LoginPage from './pages/LoginPage';
import NavigatorPanel from './components/panel/NavigatorPanel';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(
      (
      <div>
            <NavigatorPanel />
            <LoginPage />
      </div>
      ), 
      document.getElementById('root')); registerServiceWorker();