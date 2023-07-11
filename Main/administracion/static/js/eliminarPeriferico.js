document.addEventListener("DOMContentLoaded", function() {
    const btnEliminarList = document.querySelectorAll(".btn-eliminar-2");
  
    btnEliminarList.forEach((btnEliminar) => {
      btnEliminar.addEventListener("click", (event) => {
        const pk = event.target.dataset.pk;
        const url = "/eliminarPeriferico/" + pk + "/";
        window.location.href = url;
      });
    });
  });
  