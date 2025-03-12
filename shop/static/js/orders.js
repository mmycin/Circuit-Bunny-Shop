items = JSON.parse(document.getElementById("items").textContent)

itemArray = Object.entries(items).map(([name, quantity]) => ({ name, quantity }));

var mystr = ``
itemArray.forEach(item => {
    mystr += `
    <li class="list-group-item d-flex justify-content-between align-items-start">
            <div class="ms-2 me-auto">${item.name}</div>
            <span class="badge bg-primary ">${item.quantity}</span>
          </li> 
    `
});

var pricing = Number(document.getElementById("total").textContent)

finalstr = `
        <div>
          <ol class="list-group list-group-numbered d-md-block" id="items">
            ${mystr}
          </ol>
        </div>
        <span class=" ">Total Price: ৳${pricing}</span>
`


document.getElementById("showItems").onclick = () => {
    Swal.fire({
        title: "Items:",
        html: finalstr,
        icon: "info",
      });
}
