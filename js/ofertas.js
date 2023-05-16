
function cargarproductos(){
$(document).ready(function() {
    $.getJSON("/json/productos.json", function(data) {
      $.each(data.productos, function(i, producto) {
        var html = "<div class='producto'>";
        html += "<img src='" + producto.imagen + "'>";
        html += "<h2>" + producto.nombre + "</h2>";
        html += "<p class='descripcion'>" + producto.descripcion + "</p>";
        html += "<p class='precio'>" + producto.precio + " CLP</p>";
        html += "</div>";
        $("#productos").append(html);
      });
    });
  });}