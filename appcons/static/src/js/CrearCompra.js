var compra = {
    items:{
        co_fechaIngreso:'',
        co_Total:0.00,
        productos:[]
    },

  
}

$(document).ready(function(){

    $('#buscador').select2({
        minimumInputLength:2,
        language: "es",
        placeholder:"Seleccione un material",
        ajax:{
            url:window.location.pathname,
            type: 'POST',
            data:function (params){
                var queryParams={
                    term:params.term,// el termino 
                    action:'search',//accion que debe estar en la vista
                    
                }
                console.log(queryParams);
                return queryParams;

            },
            dataType: 'json',
            processResults: function (data) {
                // Transforms the top-level key of the response object from 'items' to 'results'
                console.log(data)
                return {
                  results: data
                  
                };
              }
            
        }
        
    })

    $('#buscador').on('select2:select', function (e) {
        var data = e.params.data;
        alert(data['ma_nombre']);
    });

  
   
// $("#search").autocomplete({
//     source: function ( request,response ) {
//         $.ajax({
//             url:window.location.pathname,
//             type:'POST',
//             data:{
//                 'action':'search',//accion que debe estar en la vista
//                 'term':request.term// el termino 
//             },
//             dataType:'json',
//         }).done(function (data){
//             response(data)
//         }).fail(function(jqXHR, textStatus, errorThrom){
//             alert(textStatus+ ':' + errorThrom)
//         }).always(function(data){

//         });
//     },
//     delay:500,
//     select:function(event,ui){
//         console.log(ui.item);
//     }
// })


})

