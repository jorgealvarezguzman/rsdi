from db import *
from datetime import datetime


def loginUsuario(username):
    arreglo = (username,)
    query = "SELECT * FROM usuario WHERE username=?"
    usuario = sql_read(query, arreglo)
    return usuario

def getUsuario(id):
    arreglo = (id,)
    query = "select * from usuario where id = ?"
    usuario = sql_read(query, arreglo)
    return usuario


def getUsuarioByEmail(email):
    arreglo = (email,)
    query = "select * from usuario where email = ?"
    usuario = sql_read(query, arreglo)
    return usuario


def getImagen(id):
    arreglo = (id,)
    query = """select * from Imagen 
                where id = ?"""
    imagen = sql_read(query, arreglo)
    return imagen

def getImagenByUser(id_usuario):
    arreglo = (id_usuario,)
    query = """select * from Imagen 
                where id_usuario = ?"""
    imagen = sql_read(query, arreglo)
    return imagen


def getImagenes(acceso, limite, offset):
    arreglo = (acceso, limite, offset)
    query = """select * from Imagen 
                where publica = ? limit ? offset ?"""
    imagen = sql_read(query, arreglo)
    return imagen


def crearUsuario(username, password, email):
    try:
        arreglo = (username, password, email)
        query = """insert into Usuario (username, password, email) 
                    values(?, ?, ?)"""
        sql_create(query, arreglo)
        return "Usuario creado exitosamente"
    except(Exception) as e:
        error=None
        if(str(e)=="UNIQUE constraint failed: Usuario.username"):
            error = 'El usuario ya existe, intente nuevamente con un usuario diferente'
        elif(str(e)=="UNIQUE constraint failed: Usuario.email"):
            error = u'Esta dirección de correo ya está registrada'
        else:
            error = e
        return error


def crearImagen(nombre, descripcion, publica, url, id_usuario):
    try:
        date = datetime.now()
        arreglo = (nombre, descripcion, publica, url, id_usuario, date)
        query = """insert into Imagen (nombre, descripcion, publica, url, id_usuario, fecha) 
                    values(?, ?, ?, ?, ?, ?)"""
        sql_create(query, arreglo)
        return "Imagen creada exitosamente"
    except(Exception) as e:
        error=None
        if(str(e)=="UNIQUE constraint failed: Imagen.url"):
            error = 'la ruta url ya existe'
        else:
            error = e
        return error


def actualizarUsuario(password, id):
    try:
        respuesta = None
        arreglo = (password, id)
        query = """update Usuario set password = ?
                    where id = ?"""
        respuesta = sql_update(query, arreglo)
        if respuesta is not None:
            return "Contraseña actualizada correctamente"
        
        return "Error al actualizar la contraseña"
    except:
        return "Error al actualizar la contraseña"


def actualizarImg(nombre, descripcion, publica, id):
    try:
        respuesta = None
        date = datetime.now()
        arreglo = (nombre, descripcion, publica, date, id)
        query = """update Imagen set nombre = ?, descripcion = ?, 
                    publica = ?, fecha = ?
                    where id = ?"""
        respuesta = sql_update(query, arreglo)
        if respuesta is not None:
            return "Imagen actualizada correctamente"

        return "Error al actualizar la imagen"
    except:
        return "Error al actualizar la imagen"


def borrarImagen(id):
    respuesta = None
    arreglo = (id,)
    query = "delete from Imagen where id = ?"
    respuesta = sql_delete(query, arreglo)
    if respuesta is not None:
        return True
    return False


def activarUsuario(id):
    try:
        respuesta = None
        arreglo = (id,)
        query = """update Usuario set activo = 1
                    where id = ?"""
        respuesta = sql_update(query, arreglo)
        if respuesta is not None:
            return "Usuario activado correctamente"

        return "Error al activar usuario"
    except:
        return "Error al activar usuario"


def getImagenesBusqueda(keyword, id_usuario):
    arreglo = (f'%{keyword}%', f'%{keyword}%', id_usuario)
    query = """SELECT * FROM Imagen 
                WHERE ((descripcion LIKE ? OR nombre LIKE ?) AND (publica = 1 or (publica = 0 AND id_usuario = ?)))"""
    imagenes = sql_read(query, arreglo)
    return imagenes