from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return "Esta es la página principal."
