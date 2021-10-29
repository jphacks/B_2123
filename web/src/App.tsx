import React from "react";
import "./App.css";
import { Route, BrowserRouter as Router } from "react-router-dom";
import { Home } from "./page/Home";
import { User } from "./page/User";

function App() {
  return (
    <div className="wrapper">
      <Router>
        <Route exact path="/group/:id" component={Home}></Route>
        <Route exact path="/user/:id" component={User}></Route>
      </Router>
    </div>
  );
}

export default App;
