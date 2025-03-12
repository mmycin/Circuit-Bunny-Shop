window.onload = function() {
  // Simulate a button click when the page is loaded
  document.getElementById('show').click();
  $("#showprice").append(totalPrice);
  $("#priceField").val(totalPrice);

};

if (localStorage.getItem("cart") == null || localStorage.getItem("price") == null) {
  var cart = {};
  var price = {}
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
  price = JSON.parse(localStorage.getItem("price"));
}

cartArray = Object.entries(cart).map(([name, quantity]) => ({ name, quantity }));


cartArray.forEach(item => {
  if (item.quantity === 0) {
    // Delete the item from the cart object
    delete cart[item.name];
  }
});

var totalPrice = 0;

cartArray.forEach(item => {
    const { name, quantity } = item;

    // Check if the item exists in the price object
    if (price.hasOwnProperty(name)) {
        totalPrice += quantity * price[name];
    }
});


function updateCartArrayAndHTML() {
  cartArray = Object.entries(cart).map(([name, quantity]) => ({ name, quantity }));

  const listItems = cartArray.map(({ name, quantity }) => `
    <li class="list-group-item d-flex justify-content-between align-items-start">
      <div class="ms-2 me-auto">${name}</div>
      <span class="badge bg-primary rounded-pill">${quantity}</span>
    </li>
  `);

  addstring = listItems.join(''); // Join the list items into a single string

  
  finalstr = `
    <div>
      <ol class="list-group list-group-numbered d-md-block" id="items">
        ${addstring}
      </ol>
    </div>
    <li class="list-group-item d-flex justify-content-between align-items-start">
      <div class="mt-2 me-auto">Total Price: </div>
      <span class=" ">৳${totalPrice}</span>
    </li>
    <hr>
  `;
}

document.getElementById("show").addEventListener("click", function () {
updateCartArrayAndHTML(); // Update cartArray and addstring


  Swal.fire({
    title: "Your Cart:",
    html: finalstr,
    icon: "info",
    showDenyButton: true,
    confirmButtonText: "Ok",
    denyButtonText: "Delete All"
  }).then((result) => {
    if (result.isDenied) {
      Swal.fire({
        title: "Confirm Deletion",
        text: "Are you sure you want to remove all items from your cart?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Yes, delete it!",
        cancelButtonText: "No, cancel",
      }).then((result) => {
        if (result.isConfirmed) {
          // User confirmed, proceed with deletion
          cart = {};
          localStorage.setItem("cart", JSON.stringify(cart));

          // Show a success message
          Swal.fire({
            title: "Items Deleted",
            text: "Your cart is empty now",
            icon: "success",
          });

          // Close the modal after deletion
          Swal.close();

          updateCartArrayAndHTML();
          document.getElementById('show').click(); // Update cartArray and addstring after deletion
        }
      });
    }
  });
});

	
$("#itemJson").val(JSON.stringify(cart));