    /**
     * Función para llenar automáticamente el campo de descripción de la dieta
     */
    $("#dia").change(function(){

        if($("#alimentacion").val()!=""){
            var texto = $("#alimentacion option:selected").text() + " - " + $("#dia option:selected").text();
            $("#descripcion_d").val(texto);
        }
        else{
            alert("Porfavor ingrese primero la alimentación de la dieta");
            $("#dia").val("");
        }
        
    });