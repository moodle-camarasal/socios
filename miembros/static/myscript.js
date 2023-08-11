const ventanaRN = document.getElementById('cfe-rn-windon')
const ventanaRS = document.getElementById('cfe-rs-windon')
const ventanaIC = document.getElementById('cfe-ic-windon')
const avisos = document.getElementById('cfe-avisos')
const registroSocio = document.getElementById('cfe-form-rs')

closeRN.addEventListener("click", cfemostrarRN, false)
closeRS.addEventListener("click", cfemostrarRS, false)
closeIC.addEventListener("click", cfemostrarIC, false)

let codigo = "00004303";

document.body.onclick = function() {
    avisos.classList.add("cfe-toogle")
	//avisos.style.display = "none";
  }

registroSocio.addEventListener("submit", function(event) {
    // Evita que se envíe el formulario
    event.preventDefault();

    /* Realiza la acción deseada aquí
	const empresa = document.getElementById("cfe-ne-rs").value;
	const responsable = document.getElementById("cfe-nr-rs").value;
	const cargo = document.getElementById("cfe-cd-rs").value;
	const correo = document.getElementById("cfe-ce-rs").value;
	const telefono = document.getElementById("cfe-te-rs").value;
	const codigoValue = document.getElementById("cfe-cs-rs").value;
  
	//const codigoInput = registroSocio.elements.cfe-codigo;
	//const codigoValue = codigoInput.value;
	const patron = /^[0-9]{8}$/;
	if(patron.test(codigoValue)){
		LeerCodigo(codigo);
	}
	else{
		avisos.classList.remove("cfe-toogle");
		avisos.innerText = `El código ${codigoValue} no cumple con el formato requerido, \n Ingrese solo 8 digitos con valor del 0 al 9`;		
	}*/
	alert('Esto funciona!!!!!')
  });
 /* 
function cfemostrarRN(){
	if (ventanaRN.classList.contains("cfe-toogle")) {
		ventanaRN.classList.remove("cfe-toogle")
		//otroMetodo()
	} else {
		ventanaRN.classList.add("cfe-toogle")
	}
}
function cfemostrarRS(){
	if (ventanaRS.classList.contains("cfe-toogle")) {
		ventanaRS.classList.remove("cfe-toogle")
		//otroMetodo()
	} else {
		ventanaRS.classList.add("cfe-toogle")
	}
}
function cfemostrarIC(){
	if (ventanaIC.classList.contains("cfe-toogle")) {
		ventanaIC.classList.remove("cfe-toogle")
		//otroMetodo()
	} else {
		ventanaIC.classList.add("cfe-toogle")
	}
}

function LeerCodigo(kodigo){
	fetch('socios.csv')
	//fetch('https://cfevirtual.camarasal.com/imgmoodle/socios.csv')
  .then(response => response.text())
  .then(data => {
    // Aquí puedes procesar los datos del archivo CSV
	const rows = data.split('\n');
	let codigoEncontrado = false;
	
	for(let i = 1; i < rows.length; i++){
		const row = rows[i];
		const columns = row.split(';');
		
		if(columns[1] == kodigo){
			codigoEncontrado = true;
			const filial = columns[0];
            const razonSocial = columns[2];
			avisos.classList.remove("cfe-toogle");
			avisos.innerText = `El código existe. Los datos son: \n Filial: ${filial}, Código: ${codigo}, Razón Social: ${razonSocial}`;
			break;
		}
	}
	if (!codigoEncontrado) {
		avisos.classList.remove("cfe-toogle");
        avisos.innerText = "El código que ingresó no existe";
	}
  })
  .catch(error => {
    console.error('Error al obtener el archivo CSV:', error);
  });

}
*/