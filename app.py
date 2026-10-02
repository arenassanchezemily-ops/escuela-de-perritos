# app.py 
 
@app.router ("mascotas", methods=["GET"])

def listar_mascotas():
    list = obtener_mascotas("conexion")

    return render_template("index.html", mascotas=list)