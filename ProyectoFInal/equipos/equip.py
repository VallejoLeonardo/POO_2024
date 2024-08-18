from conexionBD import *

class Equipo:
    def __init__(self, nombre, pais, estadio, presidente,presupuesto):
        self.nombre = nombre
        self.pais = pais
        self.estadio = estadio
        self.presidente = presidente
        self.presupuesto = presupuesto

    def registrar_equipo(self):
        try:
            cursor.execute("INSERT INTO equipo (nombre, pais, estadio, presidente, presupuesto ) VALUES (%s, %s, %s, %s, %s)", (self.nombre, self.pais, self.estadio, self.presidente, self.presupuesto))
            conexion.commit()
            print("\nEquipo registrado correctamente")
        except Exception as e:
            print(f"\nError al registrar equipo: {e}")

    @staticmethod
    def cambiar_presidente(id_presidente, equipo_id,idEX):
        try:
            cursor.execute("UPDATE equipo SET presidente = %s WHERE id = %s", (id_presidente, equipo_id))
            conexion.commit()
            cursor.execute("UPDATE usuarios SET equipo = %s WHERE id = %s", (equipo_id, id_presidente))
            conexion.commit()
            cursor.execute("UPDATE usuarios SET equipo = NULL WHERE id = %s", (idEX,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al cambiar presidente: {e}")