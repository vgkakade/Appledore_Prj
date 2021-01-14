import React, { Component } from "react";
import { Redirect, Route, Switch } from "react-router-dom";
import ProtectedRoute from "./components/common/protectedRoute";
import NavBar from "./components/navBar";
import Products from "./components/products";
import ProductDetail from "./components/productDetail";
import Address from "./components/address";
import LoginForm from "./components/loginForm";
import Logout from "./components/logout";
import "./App.css";
import auth from "./services/authService";
import ProfileForm from "./components/profileForm";
import Footer from "./components/footer";

class App extends Component {
  state = {};

  componentDidMount() {
    const user = auth.getCurrentUser();
    this.setState({ user });
  }

  render() {
    const { user } = this.state;
    return (
      <React.Fragment>
        <NavBar user={user} />
        <main className="container">
          <Switch>
            <Route path="/products" component={Products}></Route>
            <Route path="/product/:id" component={ProductDetail} />
            <Route path="/login" component={LoginForm}></Route>
            <Route path="/logout" component={Logout}></Route>
            <ProtectedRoute path="/profile" component={ProfileForm} />
            <ProtectedRoute path="/address" component={Address} />
            <Redirect exact from="/" to="/products" />
          </Switch>
        </main>
        <Footer />
      </React.Fragment>
    );
  }
}

export default App;
