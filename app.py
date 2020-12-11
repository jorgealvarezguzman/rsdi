# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, flash
import yagmail
import utils
import os
#from flask import jsonify

app = Flask(__name__)
app.secret_key = os.urandom(12)
sesion = True

@app.route('/')
def index():
    sesion = request.args.get('sesion')
    if sesion == "1":
        return render_template("Dashboard/inicio.html")
    else:
        return render_template("Principal/inicio.html")

@app.route('/imagen_descargar')
@app.route('/imagen_descargar/<string:idImagen>')
def descargar(idImagen=None):
    imagen = request.args.get('imagen')
    return render_template("Dashboard/descargar.html", imagen=imagen)

@app.route('/imagen_guardar', methods=["POST"])
def imagen_guardar():
    if request.method == 'POST':
        nombre = request.form['titulo']
        desc = request.form['form-description']
        acceso = request.form['form-privacy']
        #imagen_file = request.form['imagen']
        if nombre != "" and desc != "" and acceso != "":
            print(request.form)
            #algoritmo para almacenar la imagen en carpeta destino
            #algoritmo para almacenar los datos de la imagen en DB
            #return jsonify(mensaje='Imagen guardada con exito', tipo="ok")
            return redirect("/imagen_crear?msg=guardados")
        else:
            return redirect("/imagen_crear?msg=datos")
    else:
        return redirect("/imagen_crear")
        #return jsonify(mensaje='Lo sentimos, no se puede acceder al recurso', tipo="bad")

@app.route('/recuperacion', methods=['GET','POST'])
@app.route('/recuperacion/<string:codigoRecuperacion>')
def recuperacion(codigoRecuperacion=None):
    try:
        if (request.method== 'POST'):
            error=None
            email = request.form['email']
            if not utils.isEmailValid(email):
                error = 'Direccion de correo no valida'
                flash(error)
                return render_template('recuperar1.html')
            yag = yagmail.SMTP('misiontic2022grupo11@gmail.com','2022Grupo11')
            yag.send(to=email,subject='Recuperacion de contraseña',contents='Entra al siguiente link para reestablecer tu cuenta: http://127.0.0.1:5000/recuperacion/1234')
            return redirect(url_for('login'))
        else:
            if (codigoRecuperacion == '1234'):
                return render_template('recuperar2.html')
            else:
                return render_template('recuperar1.html')
    except:
        return render_template('recuperar1.html')

@app.route('/imagen_borrar')
def borrar(idimagen):
    #funcion para borrar la imagen de la base de datos
    return redirect('/')
    
@app.route('/registro/', methods = ["GET", "POST"])
def registro():
    try:
        if request.method == 'POST':
            username = request.form['name']
            password = request.form['password']
            email = request.form['correo']
            error = None
            
            if not utils.isUsernameValid(username):
                error = "El usuario debe ser alfanumerico o incluir solo '.','_','-'"
                flash(error)
                return render_template('registro.html')

            if not utils.isPasswordValid(password):
                error = u'La contraseña debe contenir al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash(error)
                return render_template('registro.html')

            if not utils.isEmailValid(email):
                error = 'Correo invalido'
                flash(error)
                return render_template("registro.html")

            yag = yagmail.SMTP('misiontic2022grupo11@gmail.com', '2022Grupo11')
            yag.send(to=email, subject='Activa tu cuenta',
                     contents='Bienvenido, usa este link para activar tu cuenta: http://127.0.0.1:5000/activacion/enhorabuena ')
            flash('Revisa tu correo para activar tu cuenta')
            return redirect(url_for('login'))
        
        return render_template('registro.html')
    except:
        return render_template('registro.html')


@app.route('/logout')
def logout():
    return redirect("/")
    
@app.route('/imagen_actualizar/')
@app.route('/imagen_actualizar/<int:idImagen>')
def actualizarImagen(idImagen=None):
    if idImagen:
        return render_template('actualizarImagen.html', nombre="test", describcion="test", es_publica=True) 
    return render_template('actualizarImagen.html')

@app.route("/login/", methods=('GET', 'POST'))
def login():
    try:
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['contrasena']
            recordarme = False

            if request.form.get('recordarme'):
                recordarme = True

            if username == "test" and password == "test1234":
                return redirect('/?sesion=1')
            else:
                error = u"El usuario o la contraseña no son validos"
                return render_template("IniciarSesion.html", error1 = error, usuario = username, password=password)

        return render_template("IniciarSesion.html")
    except:
        return render_template("IniciarSesion.html")

@app.route('/imagen_crear')
def crearimagen():
    if request.method == "GET":
        msg = request.args.get('msg')        
        if msg == "datos":
            return render_template("crear3.html", msg='Los datos enviados son incorrectos. Intentelo nuevamente!')
        elif msg == "guardados":
            return render_template("crear3.html", msg='La imagen ha sido guardada exitosamente!')
        else:
            return render_template("crear3.html")
    else:
        return render_template("crear3.html")

@app.route('/activacion/<string:codigoActivacion>')
def activacion(codigoActivacion):
    if codigoActivacion == 'enhorabuena':
        return render_template("activacion.html")
    return render_template("IniciarSesion.html")

@app.route('/imagen_ver/<string:idImagen>')
def obtenerImagen(idImagen=None):
    #funcion para obtener la imagen de la base de datos
    return redirect('/')