from flask import Blueprint, render_template, request, redirect, url_for
from models.mascota_model import MascotaModel

# Crear el Blueprint de mascotas
mascota_bp = Blueprint('mascota', __name__, url_prefix='/mascotas')

@mascota_bp.route('/')
def index():
    mascotas = MascotaModel.get_all()
    return render_template('mascota/index.html', mascotas=mascotas)

@mascota_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        nombre = request.form['nombre']
        especie = request.form['especie']
        raza = request.form['raza']
        fecha_nacimiento = request.form['fecha_nacimiento']

        MascotaModel.create(id_cliente, nombre, especie, raza, fecha_nacimiento)
        return redirect(url_for('mascota.index'))

    clientes = MascotaModel.get_clientes()
    return render_template('mascota/crear.html', clientes=clientes)

@mascota_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        nombre = request.form['nombre']
        especie = request.form['especie']
        raza = request.form['raza']
        fecha_nacimiento = request.form['fecha_nacimiento']

        MascotaModel.update(id, id_cliente, nombre, especie, raza, fecha_nacimiento)
        return redirect(url_for('mascota.index'))

    mascota = MascotaModel.get_by_id(id)
    clientes = MascotaModel.get_clientes()
    return render_template('mascota/editar.html', mascota=mascota, clientes=clientes)

@mascota_bp.route('/eliminar/<int:id>')
def eliminar(id):
    MascotaModel.delete(id)
    return redirect(url_for('mascota.index'))