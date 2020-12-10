# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, flash
import yagmail
import utils
#from flask import jsonify

app = Flask(__name__, static_folder='templates')
sesion = True

@app.route('/')
def index():
    sesion = request.args.get('sesion')
    if sesion == 1:
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
                return render_template('Registro/index.html')

            if not utils.isPasswordValid(password):
                error = 'La contraseña debe contenir al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash(error)
                return render_template('Registro/index.html')

            if not utils.isEmailValid(email):
                error = 'Correo invalido'
                flash(error)
                return render_template("Registro/index.html")

            yag = yagmail.SMTP('misiontic2022grupo11@gmail.com', '2022Grupo11')
            yag.send(to=email, subject='Activa tu cuenta',
                     contents='Bienvenido, usa este link para activar tu cuenta ')
            flash('Revisa tu correo para activar tu cuenta')
            return render_template('IniciarSesion/index.html')
        
        return render_template('Registro/index.html')
    except:
        return render_template('Registro/index.html')


@app.route('/logout')
def logout():
    sesion = False
    

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
                error = u"El correo electrónico o la contraseña no son validos"
                return render_template("IniciarSesion.html", error1 = error)

        return render_template("IniciarSesion.html")
    except:
<<<<<<< HEAD
        return render_template("IniciarSesion.html")
=======
        return render_template("IniciarSesion/index.html")

    
@app.route('/imagen_crear', methods=["POST", "GET"])
def crearimagen():
    if request.method == "GET":
        return render_template("crear3.html")
    else:
        return render_template("crear3.html")

@app.route('/imagensubida/', methods=["POST","GET"])
def imagen():
    return render_template("imagensubida.html")
>>>>>>> 506140d667a9cf559a05911553d3d13a430ed459
