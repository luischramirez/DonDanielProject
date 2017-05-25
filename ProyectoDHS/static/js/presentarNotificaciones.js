    var dia = new Date(),
    hora = dia.getHours(),
    minuto = dia.getMinutes();
    //se valida la hora en que debería mostrar las dietas (entre las 10 am - 12 pm y entre las 4 y 6 pm)
	if ((hora<10) || (hora>12 && hora<16) || (hora>18)){
		$("#tdieta").hide();	
	}
	// EPOCAS DE CELO
	var parrafoEpoca = document.getElementById("epocacelo").innerHTML;
	//Mes
	var split = parrafoEpoca.split(";");
	//nombre
	var nombreSplit = [];
	//fecha 
	var fechaSplit = [];
	//año
	var anio = [];
	//dia
	var diaCamada = [];

	for(var i = 0; i < split.length - 1; i++){
		arreglo = split[i].split(" ");
		nombreSplit[i] = arreglo[6];
		var mes = 0;
		switch(arreglo[2]){
			case "Enero": 
				mes = 01; break;
			case "Febrero": 
				mes = 02; break;
			case "Marzo": 
				mes = 03; break;
			case "Abril": 
				mes = 04; break;
			case "Mayo": 
				mes = 05; break;
			case "Junio": 
				mes = 06; break;
			case "Julio": 
				mes = 07; break;
			case "Agosto": 
				mes = 08; break;
			case "Septiembre": 
				mes = 09; break;
			case "Octubre": 
				mes = 10; break;
			case "Noviembre": 
				mes = 11; break;
			case "Diciembre": 
				mes = 12; break;
		}
		fechaSplit[i] = split[i];
		split[i] = mes;
		diaCamada[i] = arreglo[0];
		anio[i] = arreglo[4];
				
	}

	var tabla = document.getElementById("tepocacelo");
    //mes actual
	mes = dia.getMonth() + 1;
	for(var i = 0; i < split.length - 1; i++){
		//un mes antes o el mismo mes, envío la notificación
		if((split[i]) == (mes + 1) || (split[i]) == mes ){
			var tr = document.createElement("tr");
			var td = document.createElement("td");
			tr.setAttribute("class","ec"+i);
			td.style.border = "dashed";
			td.style.borderColor= "#4d94ff";
			//fecha aproximada de nacimiento de la camada
			var fechaCamada;
			var mesCamada = parseInt(split[i]) + 6;
			if(mesCamada>12){
					var diferencia = mesCamada - 12;
					mesCamada = "0" + diferencia;
					anio[i] = parseInt(anio[i])+1;
			}
			fechaCamada = diaCamada[i] + "/"+ mesCamada + "/" + anio[i];
			//tr.setAttribute("style","border-style:dashed");
            var fecha = fechaSplit[i].split("-");
			td.innerHTML= "Recuerde que " + nombreSplit[i] + " entra a epoca de celo el " + fecha[0] +
			 ", estar atento a los suplementos necesarios, siendo así, se pronostica nacimiento de la camada para el : " + fechaCamada;
			tr.appendChild(td);
			tabla.appendChild(tr);
		}
	}

	
	//-----------------------------------------------------------------------------------------------------------------------------------------------------
	//FECHAS DE RESERVA

	var parrafoFechaReserva = document.getElementById("fechareserva").innerHTML;
	//Mes
	var datos = parrafoFechaReserva.split(";");
	//fecha 
	var fecha_reserva = [];
	//nombre
	var nombrePerro = [];
	//dia
	var servicio = [];


	for(var i = 0; i < datos.length - 1; i++){
		arreglo = datos[i].split(" ");
		nombrePerro[i] = arreglo[5];
		var month = 0;
		switch(arreglo[2]){
			case "Enero": 
				month = 01; break;
			case "Febrero": 
				month = 02; break;
			case "Marzo": 
				month = 03; break;
			case "Abril": 
				month = 04; break;
			case "Mayo": 
				month = 05; break;
			case "Junio": 
				month = 06; break;
			case "Julio": 
				month = 07; break;
			case "Agosto": 
				month = 08; break;
			case "Septiembre": 
				month = 09; break;
			case "Octubre": 
				month = 10; break;
			case "Noviembre": 
				month = 11; break;
			case "Diciembre": 
				month = 12; break;
		}
		fecha_reserva[i] = datos[i];
		//meses
		datos[i] = month;		
	}

	var tabla_reserva= document.getElementById("tfechareserva");
    //mes actual
	var mes_actual = dia.getMonth() + 1;
	for(var i = 0; i < datos.length - 1; i++){
		//un mes antes o el mismo mes, envío la notificación
		if((datos[i]) == (mes_actual + 1) || (datos[i]) == mes_actual ){
			var fila = document.createElement("tr");
			var col = document.createElement("td");
			fila.setAttribute("class","ec"+i);
			col.style.border = "dashed";
			col.style.borderColor= "#4d94ff";
			//tr.setAttribute("style","border-style:dashed");
            var fecha_final = fecha_reserva[i].split(" ");
			//alert(fecha_reserva[i]);
			col.innerHTML="Recuerde que a " + nombrePerro[i] + " se le termina la reserva para " + fecha_final[6] +
			 " el "+ fecha_final[0]+ " de " + fecha_final[2]+" de "+ fecha_final[4]+".";
			fila.appendChild(col);
			tabla_reserva.appendChild(fila);
		}
	}