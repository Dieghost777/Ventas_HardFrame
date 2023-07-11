// modificar.js
document.addEventListener("DOMContentLoaded", function() {
    const btnModificarList = document.querySelectorAll(".btn-modificar");
  
    btnModificarList.forEach((btnModificar) => {
      btnModificar.addEventListener("click", (event) => {
        const pk = event.target.dataset.pk;
        const url = "/modificarComponente/" + pk + "/";
        window.location.href = url;
      });
    });
  });
  