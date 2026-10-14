import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mascotas", methods=["GET"])
def listar_mascotas():
    #list = obtener_mascotas("conexion")

    return render_template("index.html", mascotas=list)

    from flask import Flask, render_template, request, redirect, url_for
    from models.mascotas_model import mascotasmodel

    app = flask(__name__)
    modelo = mascotasmodel()

    @app.route('/')
    def index():
        usuarios = modelo.obtener_todos()
        return render_template('index.html', mascotas=mascotas)

    @app.route('/crear', methods=['POST'])
    def index():
        nombre = request.form['nombre']
        email = request.form['email']
        modelo.crear(nombre, email)
        return redirect(url_for('index'))
    @app.route('/eliminar/<int:id>')
    def eliminar(id):
        modelo.eliminar(id)
        return redirect(url_for('index'))
    
if __name__== '__main__':
    app.run(debug=True)
    