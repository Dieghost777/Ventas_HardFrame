function validartarjeta() {
    const cardNumberInput = document.getElementById("card-number");
    const cardExpiryInput = document.getElementById("card-expiry");
    const cardCvcInput = document.getElementById("card-cvc");

    const cardNumberRegex = /^\d{16}$/;
    if (!cardNumberRegex.test(cardNumberInput.value)) {
      alert("Por favor, introduzca un número de tarjeta válido (16 dígitos)");
      return false;
    }

    const cardExpiryRegex = /^(0[1-9]|1[0-2])\/(\d{2})$/;
    if (!cardExpiryRegex.test(cardExpiryInput.value)) {
      alert("Por favor, introduzca una fecha de expiración válida (MM/AA)");
      return false;
    }

    const cardCvcRegex = /^\d{3}$/;
    if (!cardCvcRegex.test(cardCvcInput.value)) {
      alert("Por favor, introduzca un código de seguridad válido (3 dígitos)");
      return false;
    }
    alert("Resera Agendada!!");
    return true;
    
  }