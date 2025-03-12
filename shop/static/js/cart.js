check = document.getElementById("notify");

cart = {};

// Check if Notify Div is there

// Get Item from Localstorage
if (localStorage.getItem("cart") == null) {
  var cart = {};
  var price = {}
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
  price = JSON.parse(localStorage.getItem("price"));
}

$(".cart").click(function () {
  var idstr = this.id.toString();

  
  price[idstr] = Number(document.getElementById(`price(${idstr})`).textContent)
  
  // Add to cart
  if (cart[idstr] != undefined) {
    cart[idstr] += 1;
  } else {
    cart[idstr] = 1;
  }

  addtext = `
    <div>${idstr} is successfully added to cart</div>
    <div>Quantity: ${cart[idstr]}</div>
    <div class="buttons-container">
      <input type="text" class="swal-input form-control mt-3" value="${cart[idstr]}" /> <br>
      <div class="mt-3">
        <button class="confirm-button swal2-confirm swal2-styled ">Confirm</button>
        <button class="delete-button swal2-cancel swal2-styled bg-danger text-white" data-item-id="${idstr}">Delete</button>
      </div>
      </div>
  `;

  Swal.fire({
    title: "Added to Cart",
    html: addtext,
    icon: "success",
    showConfirmButton: false, // Hide the default confirm button
  });

  // Add event listener for delete button
  document.querySelector(".delete-button").addEventListener("click", function () {
    // Get the item ID from the data attribute
    var itemId = this.getAttribute("data-item-id");

    // Ask for confirmation before deletion
    Swal.fire({
      title: "Confirm Deletion",
      text: `Are you sure you want to remove ${itemId} from your cart?`,
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Yes, delete it!",
      cancelButtonText: "No, cancel",
    }).then((result) => {
      if (result.isConfirmed) {
        // User confirmed, proceed with deletion
        delete cart[itemId];
        localStorage.setItem("cart", JSON.stringify(cart));

        // Show a success message
        Swal.fire({
          title: "Item Deleted",
          text: `${itemId} has been removed from your cart.`,
          icon: "success",
        });

        // Close the modal after deletion
        Swal.close();
      }
    });
  });

  // Add event listener for confirm button
  document.querySelector(".confirm-button").addEventListener("click", function () {
    // Get the quantity from the input field
    var quantity = document.querySelector(".swal-input").value;
    
    // You can add any additional actions for the confirm button here
    // ...

    Swal.fire({
      title: `Succesfully Added to cart`,
      html: `<a class="btn shadow-sm p-3 mb-5 bg-body-tertiary rounded " href="/checkout">
          <img src="https://cdn-icons-png.flaticon.com/128/102/102655.png" width="20" height="20"> Go to checkout
        </a>`,
      icon: "success",
      showConfirmButton: false,
    });

    // Save the updated quantity to the cart
    cart[idstr] = Number(quantity) || 0;
    localStorage.setItem("cart", JSON.stringify(cart));
    localStorage.setItem("price", JSON.stringify(price));



    // Close the modal
    // Swal.close();
  });

});


// var cartArray = Object.entries(cart).map(([name, quantity]) => ({ name, quantity }));
