from flask import Flask
from flask import render_template
from flask import request
#from flask import jsonify

app = Flask(__name__)
sesion = True
@app.route('/')
def index():
    #sesion = True
    if sesion == True:
        return render_template("Dashboard/inicio.html")
    else:
        return render_template("Principal/inicio.html")

@app.route('/imagen_descargar')
def descargar():
    imagen = request.args.get('imagen')
    return render_template("Dashboard/descargar.html", imagen=imagen)

@app.route('/imagen_guardar', methods=["POST"])
def imagen_guardar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        desc = request.form['descripcion']
        acceso = request.form['acceso']
        #algoritmo para almacenar la imagen en carpeta destino
        #algoritmo para almacenar los datos de la imagen en DB
        #return jsonify(mensaje='Imagen guardada con exito', tipo="ok")
        redirect("/imagen_crear")
    else:
        redirect("/imagen_crear")
        #return jsonify(mensaje='Lo sentimos, no se puede acceder al recurso', tipo="bad")



@app.route('/logout')
def logout():
    sesion = False
    