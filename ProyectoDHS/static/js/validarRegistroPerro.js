 $( function() {
    $("#sexo").change(function(){
        var sexo = $("#sexo").val();
        if(sexo=='M'){
            var label1 = document.getElementsByTagName("label")[7];
            var label2 = document.getElementsByTagName("label")[8];
            label1.setAttribute("class","hidden");
            label2.setAttribute("class","hidden");
            $("#epoca_celo_real").hide();
            $("#epoca_celo_aprox").hide();
        }else if(sexo=='H'){
            var label1 = document.getElementsByTagName("label")[7];
            var label2 = document.getElementsByTagName("label")[8];
            label1.setAttribute("class","");
            label2.setAttribute("class","");
            $("#epoca_celo_real").show();
            $("#epoca_celo_aprox").show();
        }
        else{
            alert("Porfavor ingrese M o H en el campo sexo");
            $( "#sexo" ).val("");
        }

    });
    //configuracion español datepicker
    $.datepicker.regional['es'] = {
        closeText: 'Cerrar',
        prevText: '< Ant',
        nextText: 'Sig >',
        currentText: 'Hoy',
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthNamesShort: ['Ene','Feb','Mar','Abr', 'May','Jun','Jul','Ago','Sep', 'Oct','Nov','Dic'],
        dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        dayNamesShort: ['Dom','Lun','Mar','Mié','Juv','Vie','Sáb'],
        dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sá'],
        weekHeader: 'Sm',
        dateFormat: 'dd/mm/yy',
        firstDay: 1,
        isRTL: false,
        showMonthAfterYear: false,
        yearSuffix: ''
    };
        $.datepicker.setDefaults($.datepicker.regional['es']);
        $(function () {
            //se pinta el calendario para cada campo
            $( "#fecha_nacimiento" ).datepicker({
                dateFormat: 'dd/mm/yy',
                changeYear: true,
                yearRange: "-100:+0",
            });
            $( "#fecha_desparasitacion" ).datepicker({
                dateFormat: 'dd/mm/yy',
                changeYear: true,
                yearRange: "-100:+0",
            });
            $( "#epoca_celo_real" ).datepicker({
                dateFormat: 'dd/mm/yy',
                changeYear: true,
                yearRange: "-100:+0",
            });
        });
           
    $("#fecha_nacimiento").change(function(){
        //cálculo de la edad
        var values = $( "#fecha_nacimiento" ).val().split("/");
        var dia = values[2];
        var mes = values[1];
        var ano = values[0];
        var fecha1 = dia + "-" + mes + "-" + ano;
        var fechaNacimiento = new Date(fecha1).getTime();
        var fechaActual     = new Date().getTime();
        var diff = fechaActual - fechaNacimiento;
        var edad = (diff/(1000*60*60*24)) / 365 ;

        if (diff>=0){
            $("#edad").val(Math.floor(edad));
        }
        else{
            alert ("La fecha de nacimiento no puede ser mayor a la fecha actual");
            $("#fecha_nacimiento").val("");
            $("#edad").val("");
        }
    });

    $("#epoca_celo_real").change(function(){
        // calcular la nueva epoca de celo
        var suma = 6;
        var fechaReal = $("#epoca_celo_real").val();
        var fecha = fechaReal.split('/');
        var total = parseInt(fecha[1])+suma;
        if(total>12){
            var diferencia = total - 12;
            fecha[1] = 0 + diferencia;
            fecha[1] = "0"+ fecha[1];
            fecha[2] = parseInt(fecha[2])+1;
            total = fecha[1];
        }
        var fechaNueva = fecha[0]+"/"+total+"/"+fecha[2];
        $("#epoca_celo_aprox").val(fechaNueva);
    }); 

});