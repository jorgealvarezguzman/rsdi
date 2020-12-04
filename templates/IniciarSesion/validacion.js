function validarDatos(){
    var usuario = document.getElementById("usuario");
    var contraseña = document.getElementById("contrasena");
    var mensajeIngresarUsuario = document.getElementById("mensajeIngresarUsuario");
    var mensajeIngresarContraseña = document.getElementById("mensajeIngresarContraseña");

    if(usuario.value == ""){
        mensajeIngresarUsuario.style.display = "block";
        usuario.style.borderColor = "red";
        return false;
    }else if(contraseña.value == ""){
        mensajeIngresarContraseña.style.display = "block";
        contraseña.style.borderColor = "red";
        return false;
    }
}

function limpiarAlertasUsuario(){
    var mensajeDatosIncorrectos = document.getElementById("mensajeDatosIncorrectos");
    var mensajeIngresarUsuario = document.getElementById("mensajeIngresarUsuario");
    var usuario = document.getElementById("usuario");
    mensajeDatosIncorrectos.style.display = "none";
    mensajeIngresarUsuario.style.display = "none";
    usuario.style.borderColor = "lightgrey";
}

function limpiarAlertasContraseña(){
    var mensajeDatosIncorrectos = document.getElementById("mensajeDatosIncorrectos");
    var mensajeIngresarContraseña = document.getElementById("mensajeIngresarContraseña");
    var contraseña = document.getElementById("contrasena");
    mensajeDatosIncorrectos.style.display = "none";
    mensajeIngresarContraseña.style.display = "none";
    contraseña.style.borderColor = "lightgrey";
}
