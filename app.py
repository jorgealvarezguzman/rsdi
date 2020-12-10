from flask import Flask, render_template, request, redirect
import yagmail
import utils
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

@app.route('/recuperacion', methods=['GET','POST'])
def recuperacion():
    if (request.method== 'POST'):
        email = request.form['email']
        if not utils.isEmailValid(email):
            return render_template('recuperarContraseña1/index.html')
        yag = yagmail.SMTP('misiontic2022grupo11@gmail.com','2022Grupo11')
        yag.send(to=email,subject='Recuperacion de contraseña',contents='Entra al siguiente link para reestablecer tu cuenta')
        return render_template('recuperarContraseña2/index.html')
    else:
        return render_template('recuperarContraseña1/index.html')

@app.route('/imagen_borrar')
def borrar():
    #funcion para borrar la imagen de la base de datos
    return redirect('/')

@app.route('/logout')
def logout():
    sesion = False
    
