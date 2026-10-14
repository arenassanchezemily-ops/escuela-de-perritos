from config import get_db_connection

class MascotaModel:
    @staticmethod
    def get_all():
        """Obtiene todas las mascotas junto al nombre de su dueño (cliente)."""
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT m.id_mascota, m.nombre, m.especie, m.raza, m.fecha_nacimiento, 
                   c.nombre AS dueno, m.id_cliente
            FROM mascotas m
            INNER JOIN clientes c ON m.id_cliente = c.id_cliente
            ORDER BY m.id_mascota DESC
        """
        cursor.execute(query)
        mascotas = cursor.fetchall()
        cursor.close()
        connection.close()
        return mascotas

    @staticmethod
    def get_by_id(id_mascota):
        """Obtiene una mascota por su ID."""
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM mascotas WHERE id_mascota = %s"
        cursor.execute(query, (id_mascota,))
        mascota = cursor.fetchone()
        cursor.close()
        connection.close()
        return mascota

    @staticmethod
    def create(id_cliente, nombre, especie, raza, fecha_nacimiento):
        """Inserta una nueva mascota en la base de datos."""
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO mascotas (id_cliente, nombre, especie, raza, fecha_nacimiento)
            VALUES (%s, %s, %s, %s, %s)
        """
        # Convertir fecha vacía a None si aplica
        fecha = fecha_nacimiento if fecha_nacimiento else None
        cursor.execute(query, (id_cliente, nombre, especie, raza, fecha))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update(id_mascota, id_cliente, nombre, especie, raza, fecha_nacimiento):
        """Actualiza los datos de una mascota."""
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            UPDATE mascotas 
            SET id_cliente = %s, nombre = %s, especie = %s, raza = %s, fecha_nacimiento = %s
            WHERE id_mascota = %s
        """
        fecha = fecha_nacimiento if fecha_nacimiento else None
        cursor.execute(query, (id_cliente, nombre, especie, raza, fecha, id_mascota))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(id_mascota):
        """Elimina una mascota por su ID."""
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "DELETE FROM mascotas WHERE id_mascota = %s"
        cursor.execute(query, (id_mascota,))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_clientes():
        """Obtiene la lista de clientes para rellenar el menú desplegable."""
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id_cliente, nombre FROM clientes ORDER BY nombre ASC")
        clientes = cursor.fetchall()
        cursor.close()
        connection.close()
        return clientes