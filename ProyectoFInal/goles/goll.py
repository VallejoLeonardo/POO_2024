from conexionBD import *

class Goles:
    def __init__(self, id_jugador, id_equipo, id_partido, minuto, golesT):
        self.id_jugador = id_jugador
        self.id_equipo = id_equipo
        self.id_partido = id_partido
        self.minuto = minuto
        self.golesT = golesT

    def registrar_gol(self):
        try:
            cursor.execute("""
                INSERT INTO Goles (id_jugador, id_equipo, id_partido, minuto,golesT)
                VALUES (%s, %s, %s, %s, %s)
            """, (self.id_jugador, self.id_equipo, self.id_partido, self.minuto, self.golesT))
            conexion.commit()
            print("Gol registrado correctamente")
        except Exception as e:
            print(f"Error al registrar gol: {e}")

    @staticmethod
    def goles_totales(id_partido):
        try:
            cursor.execute(f"""
                SELECT golesT FROM Goles WHERE id_partido = {id_partido}
            """)
            goles = cursor.fetchone()
            print(f"Goles totales del partido: {goles[0]}")
        except Exception as e:
            print(f"Error al obtener goles totales: {e}")