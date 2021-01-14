import { Link } from "react-router-dom";
import React, { Component } from "react";

class NavBar extends Component {
  state = {};

  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          <Link to="/" className="navbar-brand">
            BambooTantra
          </Link>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <a className="nav-link" href="#">
                  Features
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div className="nav navbar-nav navbar-right">
          <div className="form-inline my-2 my-lg-0">
            <input
              className="form-control mr-sm-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            {!this.user && (
              <React.Fragment>
                <i className="fa fa-shopping-cart"></i>
                <Link to={`/login/`}>Login</Link>
              </React.Fragment>
            )}
            {this.user && (
              <React.Fragment>
                <i className="fa fa-shopping-cart"></i>
                <Link to={`/profile`}>{this.user.firstname}</Link>
                <Link to={`/logout`}>Logout</Link>
              </React.Fragment>
            )}
          </div>
        </div>
      </nav>
    );
  }
}

export default NavBar;
