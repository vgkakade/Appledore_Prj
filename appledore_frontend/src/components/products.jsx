import React, { Component } from "react";
import { Link } from "react-router-dom";

class Products extends Component {
  state = {
    products: [],
  };

  componentDidMount() {
    fetch("http://127.0.0.1:8000/")
      .then((response) => response.json())
      .then((data) => {
        this.setState({ products: data["results"] });
      });
    console.log(this.state.user);
  }

  render() {
    return (
      <div className="row mt-2">
        <div className="col-3">
          <div className="list-group">
            <a
              href="#"
              className="list-group-item list-group-item-action active"
            >
              Cras justo odio
            </a>
          </div>
        </div>
        <div className="col">
          <div className="row">
            {this.state.products.map((product) => (
              <div
                key={product.id}
                className="card col-2 mr-2"
                style={{ width: "10rem" }}
              >
                <Link to={`/product/${product.id}`}>
                  <img
                    className="card-img-top"
                    src={product.thumb}
                    alt="Card image cap"
                  />
                </Link>
                <div className="card-body">
                  <Link to={`/product/${product.id}`}>
                    {product.product_name}
                  </Link>
                  <p className="card-text">{product.product_desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    );
  }
}

export default Products;
