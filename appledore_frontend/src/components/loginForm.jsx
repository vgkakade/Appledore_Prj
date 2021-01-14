import React, { Component } from "react";
import { Redirect } from "react-router-dom";
import auth from "../services/authService";
import Joi from "joi-browser";
import Form from "./common/form";

class Login extends Form {
  state = {
    data: { username: "", password: "" },
    errors: {},
  };

  schema = {
    username: Joi.string().required().label("Username"),
    password: Joi.string().required().label("Password"),
  };

  handleSubmit = (e) => {
    e.preventDefault();
    this.doSubmit();
  };

  doSubmit = async () => {
    try {
      const { username, password } = this.state.data;
      await auth.login(username, password);

      const { state } = this.props.location;

      window.location = state ? state.from.pathname : "/";
    } catch (ex) {
      if (ex.response && ex.status === 400) {
        const errors = { ...this.state.errors };
        errors.username = ex.response.data;

        this.setState({ errors });
      }
    }
  };

  render() {
    if (auth.getCurrentUser()) return <Redirect to="/" />;
    return (
      <form onSubmit={this.handleSubmit}>
        <h1 className="h3 mb-3 fw-normal">Please sign in</h1>
        {this.renderInput("username", "Username")}
        {this.renderInput("password", "Password", "password")}

        <div className="checkbox mb-3">
          {/* <label>
        <input type="checkbox" value="remember-me" /> Remember me
      </label> */}
        </div>
        {this.renderButton("Sign In", "w-100 btn btn-lg btn-primary")}
        {/* <p className="mt-5 mb-3 text-muted">&copy; 2017-2020</p> */}
      </form>
    );
  }
}

export default Login;
