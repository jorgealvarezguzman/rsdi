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
        if(str(e)=="UNIQUE constraint failed: usuario.username"):
            error = 'el usuario ya existe, intente nuevamente con un usuario diferente'
        elif(str(e)=="UNIQUE constraint failed: usuario.email"):
            error = u'esta dirección de correo ya está registrada'
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


def actualizarUsuario(id, password):
    try:
        arreglo = (id, password)
        query = """update Usuario set password = ?
                    where id = ?"""
        sql_update(query, arreglo)
        return "Contraseña actualizada correctamente"
    except:
        return "Error al actualizar la contraseña"


def actualizarImg(nombre, descripcion, publica, url, id):
    try:
        date = datetime.now()
        arreglo = (nombre, descripcion, publica, url, date, id)
        query = """update Imagen set nombre = ?, descripcion = ?, 
                    publica = ?, url = ?, fecha = ?
                    where id = ?"""
        sql_update(query, arreglo)
        return "Imagen actualizada correctamente"
    except:
        return "Error al actualizar la imagen"


def borrarImagen(id):
    arreglo = (id,)
    query = "delete from Usuario where id = ?"
    sql_delete(query, arreglo)


def activarUsuario(id):
    try:
        arreglo = (id,)
        query = """update Usuario set activo = 1
                    where id = ?"""
        sql_update(query, arreglo)
        return "Usuario activado correctamente"
    except:
        return "Error al activar usuario"