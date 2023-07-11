document.addEventListener("DOMContentLoaded", function() {
    const btnEliminarList = document.querySelectorAll(".btn-eliminar");
  
    btnEliminarList.forEach((btnEliminar) => {
      btnEliminar.addEventListener("click", (event) => {
        const pk = event.target.dataset.pk;
        const url = "/eliminarComponente/" + pk + "/";
        window.location.href = url;
      });
    });
  });
  