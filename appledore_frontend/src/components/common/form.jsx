import React, { Component } from "react";
import Input from "./input";

class Form extends Component {
  state = {
    data: {},
  };

  handleChange = ({ currentTarget: input }) => {
    const data = { ...this.state.data };
    data[input.name] = input.value;
    this.setState({ data });
  };

  renderButton(label, classname) {
    return <button className={classname}>{label}</button>;
  }

  renderInput(name, label, type = "text") {
    const { data } = this.state;
    return (
      <Input
        type={type}
        name={name}
        label={label}
        value={data[name]}
        onChange={this.handleChange}
      />
    );
  }
}

export default Form;
