
    $("#tipo_dieta").change(function(){
        //validacion de Si y No
        var texto = $( "#tipo_dieta" ).val();
        if (texto.toLowerCase() != 'si' && texto.toLowerCase() != 'no'){
            alert("Recuerde que solo puede escribir si y no en este campo");
            $( "#tipo_dieta" ).val(" ");
        }
    });