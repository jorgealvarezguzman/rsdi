function validarDatos(){
    var email = document.getElementById("email");
    var mensajeCorreo = document.getElementById("mensajeCorreo");

    if(email.value == ""){
        mensajeCorreo.style.display = "block";
        email.style.borderColor = "red";
        return false;
    }
}
function limpiarAlertasEmail(){
    var mensajeCorreo = document.getElementById("mensajeCorreo");
    var email = document.getElementById("email");
    mensajeCorreo.style.display = "none";
    email.style.borderColor = "lightgrey";
}
