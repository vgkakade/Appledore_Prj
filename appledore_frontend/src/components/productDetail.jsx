import React, { Component } from "react";

class ProductDetail extends Component {
  state = {
    product: "",
    images: "",
    //contains: product_name,product_price,product_quantity, product_desc,company,category,thumb{thumb,left_view,right_view}
  };

  componentDidMount() {
    const { id } = this.props.match.params;

    fetch(`http://127.0.0.1:8000/${id}`)
      .then((response) => response.json())
      .then((data) => {
        this.setState({ product: data, images: data["thumb"] });
      });
  }

  render() {
    var result = Object.values(this.state.images);

    return (
      <React.Fragment>
        <h2>{this.state.product.product_name}</h2>
        <div className="row">
          <div className="col">
            {result.map((item) => {
              return (
                <img
                  key={item}
                  src={item}
                  width="200px"
                  className="mr-2"
                  alt="No Image"
                />
              );
            })}
          </div>
          <div className="col">
            <h5>{this.state.product.product_price}</h5>
            <h5>{this.state.product.product_quantity}</h5>
            <h5>{this.state.product.product_desc}</h5>
            <h5>{this.state.product.category}</h5>
            <label htmlFor="qty">Quantity:</label>
            <input type="number" id="qty" defaultValue="1" />
            <button className="btn btn-primary btn-sm">Add to Cart</button>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default ProductDetail;

// const ProductDetail = ({ match }) => {
//   const productId = match.params.id;

//   return <h1>Product Details{match.params.id}</h1>;
// };

// export default ProductDetail;
