from db import *
from datetime import datetime


def loginUsuario(username, password):
    arreglo = (username, password)
    query = f"SELECT * FROM usuario WHERE username=? AND password=?"
    usuario = sql_read(query, arreglo)
    return usuario

def getUsuario(id):
    arreglo = (id)
    query = f"""select * from Usuario 
                where id = ?"""
    usuario = sql_read(query, arreglo)
    return usuario


def getUsuarioByEmail(email):
    arreglo = (email)
    query = f"""select * from Usuario 
                where email = ?"""
    usuario = sql_read(query, arreglo)
    return usuario


def getImagen(id):
    arreglo = (id)
    query = f"""select * from Imagen 
                where id = ?"""
    imagen = sql_read(query, arreglo)
    return imagen


def crearUsuario(username, password, email):
    try:
        arreglo = (username, password, email)
        query = f"""insert into Usuario (username, password, email) 
                    values(?, ?, ?)"""
        sql_create(query, arreglo)
        return "Usuario creado exitosamente"
    except(Exception) as e:
        error=None
        if(str(e)=="UNIQUE constraint failed: usuario.username"):
            error = 'el usuario ya existe, intente nuevamente con un usuario diferente'
        elif(str(e)=="UNIQUE constraint failed: usuario.email"):
            error = u'esta dirección de correo ya está registrada'
        return error


def crearImagen(nombre, descripcion, publica, url, id_usuario):
    try:
        date = 'date'
        arreglo = (nombre, descripcion, publica, url, id_usuario, date)
        query = f"""insert into Imagen (nombre, descripcion, publica, url, id_usuario, fecha) 
                    values(?, ?, ?, ?, ?, ?)"""
        sql_create(query, arreglo)
        return "Imagen creada exitosamente"
    except(Exception) as e:

        print(str(e))

        error=None
        if(str(e)=="UNIQUE constraint failed: Imagen.url"):
            error = 'la ruta url ya existe'
        else:
            error = e
        return error


def actualizarUsuario(id, password):
    try:
        arreglo = (id, password)
        query = f"""update Usuario set password = ?
                    where id = ?"""
        sql_update(query, arreglo)
        return "Contraseña actualizada correctamente"
    except:
        return "Error al actualizar la contraseña"


def actualizarImagen(id, nombre, descripcion, publica, url):
    try:
        query = f"""update Imagen set nombre = {nombre}, descripcion = {descripcion}, 
                    publica = {publica}, url = '{url}', fecha = datetime('now', 'localtime')
                    where id = {id};"""
        sql_update(query)
        return "Imagen actualizada correctamente"
    except:
        return "Error al actualizar la imagen"


def borrarImagen(id):
    query = f"delete from Usuario where id = {id};"
    sql_delete(query)