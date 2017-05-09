    var dia = new Date(),
    hora = dia.getHours(),
    minuto = dia.getMinutes();
    //se valida la hora en que debería mostrar las dietas (entre las 10 am - 12 pm y entre las 4 y 6 pm)
	if ((hora<10) || (hora>12 && hora<16) || (hora>18)){
		$("#tdieta").hide();	
	}
			
	var parrafoEpoca = document.getElementById("epocacelo").innerHTML;
	//Mes
	var split = parrafoEpoca.split(";");
	//nombre
	var nombreSplit = [];
	//fecha 
	var fechaSplit = [];

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
				
	}
	var tabla = document.getElementById("tepocacelo");
    //mes actual
	mes = dia.getMonth() + 1;
	for(var i = 0; i < split.length - 1; i++){
		if((split[i]) == (mes + 1) || (split[i]) == mes ){
			var tr = document.createElement("tr");
			var td = document.createElement("td");
			var trBtn = document.createElement("tr");
			var tdBtn = document.createElement("td");
			var btn = document.createElement("button");
			btn.setAttribute("class","btn btn-primary " + "ec"+i);
			btn.setAttribute("onClick","atender('" + "ec"+i + "')");
			btn.innerHTML = "Atender";
			tr.setAttribute("class","ec"+i);
			td.style.border = "dashed";
			//tr.setAttribute("style","border-style:dashed");
            var fecha = fechaSplit[i].split("-");
			td.innerHTML="Recuerde que " + nombreSplit[i] + " entra a epoca de celo el " + fecha[0] + ", estar atento a los suplementos necesarios";
			trBtn.appendChild(tdBtn);
			tdBtn.appendChild(btn);
			tr.appendChild(td);
			tabla.appendChild(tr);
			tabla.appendChild(trBtn);					
		}
	}

	

	//función encargada de atender las notificaciones 
    function atender(id){
		$('.'+id+'').remove();	
	}