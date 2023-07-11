// modificar.js
document.addEventListener("DOMContentLoaded", function() {
    const btnModificarList = document.querySelectorAll(".btn-modificar-1");
  
    btnModificarList.forEach((btnModificar) => {
      btnModificar.addEventListener("click", (event) => {
        const pk = event.target.dataset.pk;
        const url = "/modificarSoftware/" + pk + "/";
        window.location.href = url;
      });
    });
  });
  