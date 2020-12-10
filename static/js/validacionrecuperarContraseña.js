function validarDatos(){
    var contraseña = document.getElementById("contrasena");
    var confirmarContrasena = document.getElementById("confirmarContrasena");
    var mensajeIngresarContraseña = document.getElementById("mensajeIngresarContraseña");
    var mensajeConfirmarContraseña = document.getElementById("mensajeConfirmarContraseña");
    var mensajeContraseñaNoCoincide = document.getElementById("mensajeContraseñaNoCoincide");

    if(contraseña.value == ""){
        mensajeIngresarContraseña.style.display = "block";
        contraseña.style.borderColor = "red";
        return false;
    }else if(confirmarContrasena.value == ""){
        mensajeConfirmarContraseña.style.display = "block";
        confirmarContrasena.style.borderColor = "red";
        return false;
    }else if(contraseña.value != confirmarContrasena.value){
        mensajeContraseñaNoCoincide.style.display = "block";
        contraseña.style.borderColor = "red";
        confirmarContrasena.style.borderColor = "red";
        return false;
    }
}

function limpiarAlertasContraseña(){
    var mensajeIngresarContraseña = document.getElementById("mensajeIngresarContraseña");
    var contraseña = document.getElementById("contrasena");
    var confirmarContrasena = document.getElementById("confirmarContrasena");
    var mensajeContraseñaNoCoincide = document.getElementById("mensajeContraseñaNoCoincide");
    mensajeContraseñaNoCoincide.style.display = "none";
    mensajeIngresarContraseña.style.display = "none";
    contraseña.style.borderColor = "lightgrey";
    confirmarContrasena.style.borderColor = "lightgrey";
}

function limpiarAlertasConfirmarContraseña(){
    var mensajeConfirmarContraseña = document.getElementById("mensajeConfirmarContraseña");
    var confirmarContrasena = document.getElementById("confirmarContrasena");
    var mensajeContraseñaNoCoincide = document.getElementById("mensajeContraseñaNoCoincide");
    var contraseña = document.getElementById("contrasena");
    mensajeContraseñaNoCoincide.style.display = "none";
    mensajeConfirmarContraseña.style.display = "none";
    confirmarContrasena.style.borderColor = "lightgrey";
    contraseña.style.borderColor = "lightgrey";
}