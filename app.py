# encoding: utf-8
# -*- coding: ascii -*-
from flask import Flask, render_template, request, redirect, url_for, flash, session, g, make_response, abort, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
import yagmail
import utils
import os
from modelo import *
#from flask import jsonify

app = Flask(__name__)
app.secret_key = os.urandom( 24 )
app.config['DATABASE'] = 'rsdi.db'
app.secret_key = os.urandom(12)
app.config['UPLOAD_FOLDER'] = "./uploads"
sesion = True


@app.route('/')
def index():
pag = request.args.get('page')
    print(pag)
    if pag != "" and pag != None:
        offset = int(pag)*10
    else:
        offset = 0
    loteImgs = getImagenes(True, 10, offset)
    # [id,username,password,email]
    if g.usuario:
        id_usuario = g.usuario[0]
        #print('id_usuario: '+ str(id_usuario))
        return render_template("Dashboard/inicio.html", images = loteImgs)
    else:
        return render_template("Principal/inicio.html", images = loteImgs)



@app.route('/imagen_descargar')
@app.route('/imagen_descargar/<int:idImagen>')
def descargar(idImagen=None):
    dataImagen = getImagen(idImagen)
    print('/static/uploads/'+str(dataImagen[0][4]))
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename=dataImagen[0][4], as_attachment=True)
    #return render_template("Dashboard/descargar.html", imagen=imagen)


@app.route('/imagen_guardar', methods=["POST"])
def imagen_guardar():
    if request.method == 'POST':
        if g.usuario:
            id_usuario = g.usuario[0]
            # print('id_usuario: '+ str(id_usuario))
        nombre = request.form['titulo']
        desc = request.form['form-description']
        acceso = request.form['form-privacy']
        imagen_file = request.files['imagen']
        if nombre != "" and desc != "" and acceso != "" and imagen_file != "":
            # Definimos la ruta base
            #BASE_DIR = dirname(dirname(abspath(__file__)))
            BASE_DIR_PUB = "publics"
            BASE_DIR_PRV = "privates"

            #algoritmo para almacenar la imagen en carpeta destino
            if imagen_file.filename:
                if acceso == "public":
                    destino = BASE_DIR_PUB+"/"+str(imagen_file.filename)
                    publica = 1
                elif acceso == "private":
                    destino = BASE_DIR_PRV + "/" + str(imagen_file.filename)
                    publica = 0

                #Move file to UPLAOD_FOLDER
                imagen_file.save(os.path.join(app.config['UPLOAD_FOLDER'], destino))

                #algoritmo para almacenar los datos de la imagen en DB
                img_data_to_db = crearImagen(nombre, desc, publica, destino, id_usuario)
                if img_data_to_db == "Imagen creada exitosamente":
                    return redirect("/imagen_crear?msg=guardados")


            #return jsonify(mensaje='Imagen guardada con exito', tipo="ok")
        else:
            return redirect("/imagen_crear?msg=datos")
    else:
        return redirect("/imagen_crear")
        #return jsonify(mensaje='Lo sentimos, no se puede acceder al recurso', tipo="bad")


@app.route('/recuperacion', methods=['GET','POST'])
@app.route('/recuperacion/<string:codigoRecuperacion>', methods=['GET','POST'])
def recuperacion(codigoRecuperacion=None):
    try:
        if(not codigoRecuperacion):
            if (request.method== 'POST'):
                error=None
                email = request.form['email']
                usuario =getUsuarioByEmail(email)

                if not utils.isEmailValid(email):
                    error = 'Direccion de correo no valida'
                    flash(error)
                    return render_template('recuperar1.html')
                if usuario==[]:
                    error= 'Email no valido'
                    flash(error)
                    return render_template('recuperar1.html')
                
                yag = yagmail.SMTP('misiontic2022grupo11@gmail.com','2022Grupo11')
                yag.send(to=email,subject='Recuperacion de contraseña',
                                  contents=f"""Entra al siguiente link para reestablecer tu cuenta: 
                                               http://127.0.0.1:5000/recuperacion/{generate_password_hash('recover')}?email={email}""")
                return redirect(url_for('login'))
            else:
                error = 'revise su correo'
                flash(error)
                return render_template('recuperar1.html')
        else:
            
            if(check_password_hash(codigoRecuperacion, 'recover')):
                if (request.method== 'POST'):
                    pass1=request.form['contrasena']
                    pass2=request.form['confirmarContrasena']            
                    if(pass1!="" and pass2!="" and pass1==pass2):
                        actualizarUsuario(generate_password_hash(pass1), request.cookies.get('idUsuario'))
                        return redirect('/login')
                    error= 'campos vacios o no coinciden'
                    flash(error)
                    return redirect('/recuperacion/'+codigoRecuperacion)
                else:
                    usuario = getUsuarioByEmail(request.args.get('email'))
                    response = make_response(render_template('recuperar2.html', codigoRecuperacion = codigoRecuperacion))
                    response.set_cookie('idUsuario', f'{usuario[0][0]}')
                    return response
            else:
                return redirect('/')
    except:
        return render_template('recuperar1.html')


@app.route('/imagen_borrar')
@app.route('/imagen_borrar/<string:idImagen>')
def borrar(idImagen):
    borrarImagen(idImagen)
    flash('La imagen ha sido borrada exitosamente')
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

            if getUsuarioByEmail(email) != []:
                error="Usuario ya existente"
                flash(error)
                return redirect(url_for('registro'))
            else:
                crearUsuario(username, generate_password_hash(password), email)

            yag = yagmail.SMTP('misiontic2022grupo11@gmail.com', '2022Grupo11')
            yag.send(to=email, subject='Activa tu cuenta',
                     contents=f"""Bienvenido, usa este link para activar tu cuenta: 
                                  http://127.0.0.1:5000/activacion/{generate_password_hash('enhorabuena')}?email={email}""")
            flash('Revisa tu correo para activar tu cuenta')
            return redirect(url_for('login'))
        
        return render_template('registro.html')
    except:
        return render_template('registro.html')


@app.route('/logout')
def logout():
    session.clear()
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

            usuario = loginUsuario(username)
            if usuario != []:
                if check_password_hash(usuario[0][2], password):
                    if not usuario[0][4]:
                        error2 = "Esta cuenta no ha sido activada."
                        error3= "Revisa tu correo para activar tu cuenta."
                        return render_template("IniciarSesion.html", usuario = username, password=password, 
                                                error2 = error2, error3 = error3)
                    session.clear()
                    session['id_usuario'] = usuario[0][0]
                    return redirect('/')
                error = u"El usuario o la contraseña no son validos"
                return render_template("IniciarSesion.html", error1 = error, usuario = username, password=password)
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
    if (check_password_hash(codigoActivacion, 'enhorabuena')):
        usuario = getUsuarioByEmail(request.args.get('email'))
        activarUsuario(usuario[0][0])
        return render_template("activacion.html")
    return render_template("IniciarSesion.html")


@app.route('/imagen_ver/<string:idImagen>')
def obtenerImagen(idImagen=None):

    return redirect('/')


@app.before_request
def load_logged_in_user():
    id_usuario = session.get('id_usuario')
    
    if id_usuario is None:
        g.usuario = None
    else:
        g.usuario = getUsuario(id_usuario)[0]  # se almacenan los datos de usuario. [id,username,password,email]

    
