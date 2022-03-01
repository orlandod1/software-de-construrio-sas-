function confirmarEliminacionCompra(id) {
  Swal.fire({
    title: 'Estas seguro que deseas eliminar esta compra?',
    text: 'No podrás deshacer esta acción!',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si,Eliminar!',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = '/eliminar-compra/' + id + '/'
      //redirigir al usuario a la ruta de eliminar
    }
  })
}

function confirmarEliminacionmaterial(id) {
  Swal.fire({
    title: 'Estas seguro que deseas eliminar este material?',
    text: 'No podrás deshacer esta acción!',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si,Eliminar!',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.isConfirmed) {
      //redirigir al usuario a la ruta de eliminar
      window.location.href = 'eliminar-material/' + id + '/'
    }
  })
}

function confirmarEliminacionProovedor(id) {
  Swal.fire({
    title: 'Estas seguro que deseas eliminar este proveedor?',
    text: 'No podrás deshacer esta acción!',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si,Eliminar!',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.isConfirmed) {
      //redirigir al usuario a la ruta de eliminar
      window.location.href = 'eliminar/' + id + '/'
    }
  })
}

function confirmarEliminacionUnidad(id) {
  Swal.fire({
    title: 'Estas seguro que deseas eliminar esta unidad?',
    text: 'No podrás deshacer esta acción!',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si,Eliminar!',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.isConfirmed) {
      //redirigir al usuario a la ruta de eliminar
      window.location.href = 'eliminar/' + id + '/'
    }
  })
}
//corregir esta alerta
function salirSeccion(id) {
  Swal.fire({
    title: 'Estas seguro que deseas salir de la seccion?',

    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.isConfirmed) {
      //redirigir al usuario a la ruta de eliminar
      window.location.href = 'login/'
    }
  })
}
