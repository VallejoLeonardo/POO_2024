from conexionBD import *

class Auto:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif

    def insertar(self):
        try:
            cursor.execute(
                "INSERT INTO autos (matricula, marca, modelo, color, nif) VALUES (%s, %s, %s, %s, %s)",
                (self.matricula, self.marca, self.modelo, self.color, self.nif)
            )
            conexion.commit()
            return True
        except:
            return False   

    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "SELECT * FROM autos",
            )
            return cursor.fetchall()
        except:
            return None    

    @staticmethod
    def actualizar(matricula, marca, modelo, color, nif):
        try:
            cursor.execute(
                "UPDATE autos SET marca=%s, modelo=%s, color=%s, nif=%s WHERE matricula=%s",
                (marca, modelo, color, nif, matricula)
            )
            conexion.commit()
            return True
        except:
            return False  

    @staticmethod
    def eliminar(matricula):
        try:
            cursor.execute(
                "DELETE FROM autos WHERE matricula=%s",
                (matricula,)
            )
            conexion.commit()
            return True
        except:
            return False
