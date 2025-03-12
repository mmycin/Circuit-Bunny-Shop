$("#trackerForm").submit((event) => {
  event.preventDefault(); // Prevent the default form submission

  $("#items").empty();

  var formData = {
    orderID: $("input[name=orderID]").val(),
    email: $("input[name=email]").val(),
    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
  };

  $.ajax({
    type: "POST",
    url: "/tracker/",
    data: formData,
    encode: true,
  }).done((data) => {
    updates = JSON.parse(data);
    if ((updates.length > 0) & (updates != {})) {
      let mystr = ""; 
      for (let i = 0; i < updates.length; i++) {
        let text = updates[i]["text"];
        let time = updates[i]["time"];

        mystr += `
          <li class="list-group-item d-flex justify-content-between align-items-start">
            <div class="ms-2 me-auto">${text}</div>
            <span class="badge bg-primary ">${time}</span>
          </li> 
        `;
      }

      let final = `
        <div>
          <ol class="list-group list-group-numbered d-md-block" id="items">
            ${mystr}
          </ol>
        </div>
      `;

      Swal.fire({
        title: "Tracking Status:",
        html: final,
        icon: "info",
      });
    } else {
      updates = "error";
      mystr = `
        <li class="list-group-item d-flex justify-content-between align-items-start mb-2">
          <div class="ms-2 me-auto">Sorry, we don't have any information of <span class="text-info">Tracking ID: ${$(
            "input[name=orderID]"
          ).val()}</span> and <span class="text-info">Email: ${$(
        "input[name=email]"
      ).val()}</span> make sure you have entered the correct informations and try again.</div>
        </li> 
      `;

      Swal.fire({
        title: "Tracking Status",
        html: mystr,
        icon: "info",
      });
    }
  });
});
