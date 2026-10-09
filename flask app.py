import mysql.connector
from mysql.connector import Error

class usuariomodel:
    def __init__(self):
        self.config ={
          'host': 'localhost'
           'user': 'root'
           'paswoed': '',
           'database' : 'crud_db'
        }
def _conectar(self):
    """metedo auxiliar para abrir conexion con MySQL."""
    try: 
        return mysql.connector.connect(**self.config)
    except Error as e:
        print(f"error de conexion a MyQSL: {e}")
        return None

    def crear(self, nombre , email):
        conexion = self._conectar
        if not conexion:
            return False

        try:
            curso = conexion.curso()
            sql = "INSERT INTO usuarios (nombre, email) VALUES (%s,%s)"
            curso.execute(sql,(nombre.email))
            conexion.commit()
            return True
        except Error as e:
            print(f"error al insertar usuario: {e}") 
            return False
        finally:
            cursor.close()
            conexion = self._conectar()

            def obtener_todos(self):
                conexion = self._conectar()
                if not conexion:
                    return []


                try:
                    cursor = conexion.curso(dictionary=True)
                    sql = "insert into mascotas (nombre, raza) values (%s, %s)"
                    cursor.execute(sql,(mascotas, raza))
                    conexion.commit()
                    return True 
                except Error as e:
                    print(f"error al insertar usuario:{e}")
                    cursor.close()
                    conexion.close()

                    def obtener_todos(self):
                        conexion = self._conectar()
                        if not conexion:
                            return

                        try:
                            cursor = conexion.cursor(dictiononary=True)
                            sql = "select id, nombre, mascotas, razas order by id desc"
                            cursor.execute(sql)
                            return cursor.fetchall()
                        except error as e:
                            print(f"error al consular ala escuela: {e}")
                            return []
                        finally:
                            cursor.close()
                            conexion.close()

                            def obtener_por_id(self, mascotas)
                                conexion = self._conectar()
                                if not conexion:
                                    return None

                                try:
                                    cursor = conexion.cursor(dictionary=True)
                                    sql = "select id, nombre, razas from mascota where id = %s"
                                    cursor.execute(sql,(mascota_id))
                                    return cursor.fetchone()
                                except Error as e:
                                    print(f"error l consultar mascota por id: {e}")
                                    return None
                                finally:r
                                cursor.close()
                            conexion.close()

                    f actualizar(self, mascotas_id, nombre , razas):
                    conexion = self._conectar()
                    if not conexion:
                                            
                     return False

                    try: 
                        cursor = conexion.cursor()
                        sql = "update mascotas set nombre = %s, raza = %s where id = %s"
                        cursor.execute(sql,(nombre, raza,mascota))
                        conexion.commit()
                        return True