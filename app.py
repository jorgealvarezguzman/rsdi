from flask import Flask, render_template,request
app=Flask(__name__)

@app.route('/imagen_crear', methods=["POST", "GET"])
def crearimagen():
    if request.method == "GET":
        return render_template("crear3.html")
    else:
        return render_template("crear3.html")

@app.route('/imagensubida/', methods=["POST","GET"])
def imagen():
    return render_template("imagensubida.html")