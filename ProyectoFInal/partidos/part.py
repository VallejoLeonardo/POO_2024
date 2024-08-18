from conexionBD import *

class Partido:
    def __init__(self, idEq1, idEq2, fecha, estado,estadio):
        self.id_equipo1 = idEq1
        self.id_equipo2 = idEq2
        self.fecha = fecha
        self.estado = estado
        self.estadio = estadio

    @staticmethod
    def obtener_resultados(partido_id):
        cursor.execute("SELECT golesE1, golesE2 FROM Partido WHERE id = %s", (partido_id,))
        resultado = cursor.fetchone()
        return resultado