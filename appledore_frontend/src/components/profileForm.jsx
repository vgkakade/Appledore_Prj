import React, { Component } from "react";
import { Link } from "react-router-dom";

class ProfileForm extends Component {
  state = {};
  render() {
    return (
      <div className="row">
        <div className="col-2">
          <h1>Profile Form</h1>
        </div>
        <div className="col">
          <Link to={`/address`}>Address</Link>
        </div>
      </div>
    );
  }
}

export default ProfileForm;
