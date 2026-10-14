import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",          # Modifica según tus credenciales de MySQL
        password="",          # Modifica según tu contraseña
        database="escuela_mascotas"
    )
    return connection