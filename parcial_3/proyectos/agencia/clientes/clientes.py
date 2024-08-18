from conexionBD import *

class Cliente:
    def __init__(self, nif, nombre, direccion, ciudad, tel):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel

    def insertar(self):
        try:
            cursor.execute(
                "INSERT INTO clientes (nif, nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s, %s)",
                (self.nif, self.nombre, self.direccion, self.ciudad, self.tel)
            )
            conexion.commit()
            return True
        except:
            return False   

    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "SELECT * FROM clientes",
            )
            return cursor.fetchall()
        except:
            return None    

    @staticmethod
    def actualizar(nif, nombre, direccion, ciudad, tel):
        try:
            cursor.execute(
                "UPDATE clientes SET nombre=%s, direccion=%s, ciudad=%s, tel=%s WHERE nif=%s",
                (nombre, direccion, ciudad, tel, nif)
            )
            conexion.commit()
            return True
        except:
            return False  

    @staticmethod
    def eliminar(nif):
        try:
            cursor.execute(
                "DELETE FROM clientes WHERE nif=%s",
                (nif,)
            )
            conexion.commit()
            return True
        except:
            return False
