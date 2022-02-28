function agregarFormsProducto() {
  var totalForms = document.querySelector('#id_form-TOTAL_FORMS')

  //nuevo input para provedores
  var nuevoInputProvedores = document.querySelector('#id_form-0-prov_id').cloneNode(true)
  console.log(nuevoInputProvedores);

  nuevoInputProvedores.name = 'form-' + totalForms.value + '-prov_id'
  nuevoInputProvedores.id = 'id_form-' + totalForms.value + '-prov_id'
  nuevoInputProvedores.class='select2'
  //nuevo input para producto
  var nuevoInputProducto = document
    .querySelector('#id_form-0-nombre')
    .cloneNode(true)
  nuevoInputProducto.name = 'form-' + totalForms.value + '-nombre'
  nuevoInputProducto.id = 'id_form-' + totalForms.value + '-nombre'

  console.log(document.querySelector('#id_form-0-nombre'))
  //nuevo input para unidad
  var nuevoInputUnidad = document
    .querySelector('#id_form-0-unidad')
    .cloneNode(true)
  nuevoInputUnidad.name = 'form-' + totalForms.value + '-unidad'
  nuevoInputUnidad.id = 'id_form-' + totalForms.value + '-unidad'
  //nuevo input para precio unitario
  var nuevoInputPrecio = document
    .querySelector('#id_form-0-pro_precio')
    .cloneNode(true)
  nuevoInputPrecio.name = 'form-' + totalForms.value + '-pro_precio'
  nuevoInputPrecio.id = 'id_form-' + totalForms.value + '-pro_precio'
  nuevoInputPrecio.value = ''
  //nuevo input para cantidad
  var nuevoInputCantidad = document
    .querySelector('#id_form-0-pro_cantidad')
    .cloneNode(true)
  nuevoInputCantidad.name = 'form-' + totalForms.value + '-pro_cantidad'
  nuevoInputCantidad.id = 'id_form-' + totalForms.value + '-pro_cantidad'
  nuevoInputCantidad.value = ''
  nuevoInputCantidad.addEventListener('keyup', CalcularSubtotal, false)
  //nuevo input para subtotal
  var nuevoInputSubtotal = document
    .querySelector('#id_form-0-pro_total')
    .cloneNode(true)
  nuevoInputSubtotal.name = 'form-' + totalForms.value + '-pro_total'
  nuevoInputSubtotal.id = 'id_form-' + totalForms.value + '-pro_total'
  nuevoInputSubtotal.value = '0'
  totalForms.value = parseInt(totalForms.value) + 1

  var tbody = document.querySelector('#tbody')
  var tr = document.createElement('tr') //nueva fila

  var tdProvedores = document.createElement('td') //se crea la columna
  tdProvedores.appendChild(nuevoInputProvedores)
  tr.appendChild(tdProvedores)

  var tdProductos = document.createElement('td')
  tdProductos.appendChild(nuevoInputProducto)
  tr.appendChild(tdProductos)

  var tdUnidad = document.createElement('td')
  tdUnidad.appendChild(nuevoInputUnidad)
  tr.appendChild(tdUnidad)

  var tdPrecio = document.createElement('td')
  tdPrecio.appendChild(nuevoInputPrecio)
  tr.appendChild(tdPrecio)

  var tdCantidad = document.createElement('td')
  tdCantidad.appendChild(nuevoInputCantidad)
  tr.appendChild(tdCantidad)

  var tdsubTotal = document.createElement('td')
  tdsubTotal.appendChild(nuevoInputSubtotal)
  tr.appendChild(tdsubTotal)

  tbody.appendChild(tr)
}

function eliminarFormsProducto() {
  var forms = document.querySelector('#id_form-TOTAL_FORMS')
  if (forms.value > 1) {
    forms.value = parseInt(forms.value) - 1
    var tbody = document.querySelector('#tbody')
    var lastTr = tbody.lastChild
    tbody.removeChild(lastTr)
    CalcularTotal()
  } else {
    alert('No se pueden eliminar todos')
  }
}

function eliminar(input) {
  document.querySelector(input).remove()
}

var Cantidad = document.querySelector('#id_form-0-pro_cantidad')
Cantidad.addEventListener('keyup', CalcularSubtotal, false)

function CalcularSubtotal() {
  var idCantidad = event.path[0].id // se trae el input que acciona el evento
  var idPrecio = idCantidad.substr(0, 9) + '-pro_precio'
  console.log('cantidad :' + idCantidad)
  console.log('precio: ' + idPrecio)
  var idSubTotal = idCantidad.substr(0, 9) + '-pro_total' //se añade para traer el id del pro_total

  var Cantidad2 = document.querySelector('#' + idCantidad)
  var precio = document.querySelector('#' + idPrecio)
  var subtotal = document.querySelector('#' + idSubTotal)

  if (Cantidad2.value && precio.value) {
    subtotal.value = parseInt(Cantidad2.value) * parseInt(precio.value)
    CalcularTotal()
    /*var total=document.querySelector("#id_co_Total");
      total.value = parseInt(total.value)+parseInt(subtotal.value);*/
  }
}

function CalcularTotal() {
  var forms = document.querySelector('#id_form-TOTAL_FORMS')
  var total = document.querySelector('#id_co_Total')
  total.value = 0
  var subTotal
  for (var i = 0; i < forms.value; i++) {
    subTotal = document.querySelector('#id_form-' + i + '-pro_total')
    total.value = parseInt(total.value) + parseInt(subTotal.value)
  }
}
