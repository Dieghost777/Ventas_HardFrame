document.addEventListener("DOMContentLoaded", function() {
    const btnEliminarList = document.querySelectorAll(".btn-eliminar-1");
  
    btnEliminarList.forEach((btnEliminar) => {
      btnEliminar.addEventListener("click", (event) => {
        const pk = event.target.dataset.pk;
        const url = "/eliminarSoftware/" + pk + "/";
        window.location.href = url;
      });
    });
  });
  