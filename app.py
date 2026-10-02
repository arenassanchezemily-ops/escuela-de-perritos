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