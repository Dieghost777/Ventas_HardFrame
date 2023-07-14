window.addEventListener("DOMContentLoaded", () => {
    const email = document.getElementById("email");
    const name1 = document.getElementById("name");
    const form = document.getElementById("form");
    const nameWarning = document.getElementById("name-warning");
    const emailWarning = document.getElementById("email-warning");
    const rutWarning = document.getElementById("rut-warning");
    const residenciaWarning = document.getElementById("residencia-warning");
    const comentarioWarning = document.getElementById("comentario-warning");
  
    form.addEventListener("submit", e => {
      e.preventDefault();
      nameWarning.textContent = "";
      emailWarning.textContent = "";
      rutWarning.textContent = "";
      residenciaWarning.textContent = "";
      comentarioWarning.textContent = "";
  
      let entrar = false;
      let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
      let regexNumber = /^[0-9]+$/;
  
      if (name1.value.length < 8) {
        nameWarning.textContent = "Falta nombre";
        entrar = true;
      }
  
      if (!regexEmail.test(email.value)) {
        emailWarning.textContent = "El email no es válido";
        entrar = true;
      }
  
      if (rut.value.length < 8 || !regexNumber.test(rut.value)) {
        rutWarning.textContent = "Rut incompleto o no es un número válido";
        entrar = true;
      }
  
      if (Residencia.value.length < 8) {
        residenciaWarning.textContent = "Falta residencia";
        entrar = true;
      }
  
      if (!entrar) {
        // Aquí puedes realizar las acciones necesarias cuando el formulario se envía correctamente
        comentarioWarning.textContent = "todo correcto";
        window.location.href = "{% url '/targeta/' %}";
      }
    });
  });

  $(document).ready(function() {
    $("#ocultar-btn").click(function() {
      $(".col-6").hide();
    });
  });