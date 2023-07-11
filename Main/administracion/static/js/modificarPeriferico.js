// modificar.js
document.addEventListener("DOMContentLoaded", function() {
    const btnModificarList = document.querySelectorAll(".btn-modificar-2");
  
    btnModificarList.forEach((btnModificar) => {
      btnModificar.addEventListener("click", (event) => {
        const pk = event.target.dataset.pk;
        const url = "/modificarPeriferico/" + pk + "/";
        window.location.href = url;
      });
    });
  });
  