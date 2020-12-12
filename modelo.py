from db import *


def getUsuario(id):
    query = f"""select * from Usuario 
                where id = {id};"""
    usuario = sql_read(query)
    return usuario


def getUsuarioByEmail(email):
    query = f"""select * from Usuario 
                where email = '{email}';"""
    usuario = sql_read(query)
    return usuario


def getImagen(id):
    query = f"""select * from Imagen 
                where id = {id};"""
    imagen = sql_read(query)
    return imagen


def crearUsuario(username, password, email):
    try:
        query = f"""insert into Usuario (username, password, email) 
                    values('{username}', '{password}', '{email}');"""
        sql_create(query)
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
        query = f"""insert into Imagen (nombre, descripcion, publica, url, id_usuario, fecha) 
                    values('{nombre}', '{descripcion}', '{publica}', '{url}', '{id_usuario}',
                    datetime('now', 'localtime')
                    );"""
        sql_create(query)
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
        query = f"""update Usuario set password = '{password}'
                    where id = {id};"""
        sql_update(query)
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