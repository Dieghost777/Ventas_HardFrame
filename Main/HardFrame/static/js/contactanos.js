function validarFormulario() {
    var nombre = document.getElementById('nombre').value;
    var email = document.getElementById('email').value;
    var mensaje = document.getElementById('mensaje').value;
  
    var errorNombre = document.getElementById('error-nombre');
    var errorEmail = document.getElementById('error-email');
    var errorMensaje = document.getElementById('error-mensaje');
  
    errorNombre.textContent = '';
    errorEmail.textContent = '';
    errorMensaje.textContent = '';
  
    var isValid = true;
  
    if (nombre.trim() === '') {
      errorNombre.textContent = 'Por favor, ingresa tu nombre.';
      isValid = false;
    }
  
    if (email.trim() === '') {
      errorEmail.textContent = 'Por favor, ingresa tu correo electrónico.';
      isValid = false;
    } else if (!validarEmail(email)) {
      errorEmail.textContent = 'Por favor, ingresa un correo electrónico válido.';
      isValid = false;
    }
  
    if (mensaje.trim() === '') {
      errorMensaje.textContent = 'Por favor, ingresa tu mensaje.';
      isValid = false;
    }
  
    return isValid;
  }
  
  function validarEmail(email) {
    var regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regexEmail.test(email);
  }