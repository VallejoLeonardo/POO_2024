from conexionBD import *

class Usuario:
    def __init__(self, email, nombre, contrasena, id=None):
        self.id = id
        self.email = email
        self.nombre = nombre
        self.contrasena = contrasena

    def registrarse(self):
        try:
            cursor.execute(
                "INSERT INTO usuarios (email, nombre, contrasena) VALUES (%s, %s, %s)",
                (self.email, self.nombre, self.contrasena)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            cursor.execute(
                "SELECT * FROM usuarios WHERE email=%s AND contrasena=%s",
                (email, contrasena)
            )
            return cursor.fetchone()
        except:
            return None
