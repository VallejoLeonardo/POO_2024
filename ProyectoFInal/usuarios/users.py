from conexionBD import *
from partidos.part import Partido
import os

def borrarPantalla():
    os.system("cls")

def esperaTecla():
    input("\nPresiona una tecla para continuar...")

class Usuario:
    def __init__(self, nombre_usuario, contraseña, nombre, apellidos, fecha_nac, salario,tipo_usuario):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nac = fecha_nac
        self.salario = salario


class Jugador(Usuario):
    def __init__(self, nombre_usuario, contraseña, nombre, apellidos, fecha_nac, salario, tipo_usuario, numero_camiseta, nacionalidad):
        super().__init__(nombre_usuario, contraseña, nombre, apellidos, fecha_nac, salario, tipo_usuario)
        self.numero_camiseta = numero_camiseta
        self.nacionalidad = nacionalidad

    def registrarJugador(self):
        try:
            cursor.execute("INSERT INTO usuarios (nombre_usuario, contraseña, nombre, apellido, fecha_nac, salario, tipo, numeroCamiseta, nacionalidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (self.nombre_usuario, self.contraseña, self.nombre, self.apellidos, self.fecha_nac, self.salario, self.tipo_usuario, self.numero_camiseta, self.nacionalidad))
            conexion.commit()
            print("\nJugador registrado correctamente")
        except Exception as e:
            print(f"\nError al registrar jugador: {e}")

    @staticmethod
    def mostrar_estadisticas(id_partido,id_jugador):
        try:
            print("\n...:: Estadísticas del partido ::...")
            cursor.execute("SELECT minuto FROM goles WHERE id_partido = %s AND id_jugador = %s ", (id_partido,id_jugador))
            goles = cursor.fetchall()
            if goles:
                borrarPantalla()
                print("\n Tus goles: ")
                for gol in goles:
                    print(f"Minuto: {gol[0]}")
                    print("-----------------------------------------")
            else:
                print("\nNo hay estadísticas para este partido.")
        except Exception as e:
            print(f"\nError al mostrar estadísticas: {e}")

    @staticmethod
    def ver_partidos(tipo,id_equipo,id):
        if tipo == "1":
            try:
                print("\n...:: Partidos Pendientes ::...")
                cursor.execute("SELECT * FROM partido WHERE (idEq1 = %s OR idEq2 = %s) and estado = 'Pendiente'", (id_equipo, id_equipo))
                partidos = cursor.fetchall()
                if partidos:
                    borrarPantalla()
                    print("\nLista de partidos: ")
                    for partido in partidos:
                        print(f"Fecha: {partido[3]}")
                        print(f"Estado: {partido[4]}")
                        print(f"Estadio: {partido[5]}")
                        print("\n-----------------------------------------")
                        esperaTecla()
                else:
                    print("\nNo hay partidos para tu equipo.")
                    esperaTecla()
            except Exception as e:
                print(f"\nError al mostrar partidos: {e}")
                esperaTecla()
        elif tipo == "2":
            try:
                print("\n...:: Partidos Completados ::...")
                cursor.execute("SELECT * FROM partido WHERE (idEq1 = %s OR idEq2 = %s) and estado = 'Completado'", (id_equipo, id_equipo))
                partidos = cursor.fetchall()
                if partidos:
                    borrarPantalla()
                    print("\nLista de partidos: ")
                    for partido in partidos:
                        print(f"Fecha: {partido[3]}")
                        print(f"Estado: {partido[4]}")
                        print(f"Estadio: {partido[5]}")
                        print("\n-----------------------------------------")
                else:
                    print("\nNo hay partidos jugados.")
                    esperaTecla()
            except Exception as e:
                print(f"\nError al mostrar partidos: {e}")
                esperaTecla()

    @staticmethod
    def iniciar_sesion(nombre_usuario, contraseña):
        try:
            cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = %s AND contraseña = %s AND tipo = 'Jugador'", (nombre_usuario, contraseña))
            user = cursor.fetchone()
            if user:
                return user
            else:
                return []
        except Exception as e:
            print(f"\nError al iniciar sesión: {e}")
            return []

    @staticmethod
    def verGoles(id_jugador):
        try:
            cursor.execute("SELECT id_partido, minuto FROM goles WHERE id_jugador = %s", (id_jugador,))
            goles = cursor.fetchall()
            if goles:
                print("\n...:: Historial de Goles ::...")
                for gol in goles:
                    print(f"\nID Partido: {gol[0]}")
                    print(f"Minuto: {gol[1]}")
                    print("\n-----------------------------------------")
            else:
                print("\nNo hay goles registrados.")
        except Exception as e:
            print(f"\nError al mostrar goles: {e}")


class Presidente(Usuario):
    def __init__(self, nombre_usuario, contraseña, nombre, apellidos, fecha_nac, salario, tipo_usuario, antiguedad):
        super().__init__(nombre_usuario, contraseña, nombre, apellidos, fecha_nac, salario, tipo_usuario)
        self.antiguedad = antiguedad

    @staticmethod
    def contratoJugador(idJugador,idEquipo):
        try:
            cursor.execute("UPDATE usuarios SET equipo_jug = %s WHERE id = %s", (idEquipo, idJugador))
            conexion.commit()
            print("\n¡ Jugador contratado correctamente :D !")
        except Exception as e:
            print(f"\nError al contratar jugador: {e}")

    def registrarPresidente(self):
        try:
            cursor.execute("INSERT INTO usuarios (nombre_usuario, contraseña, nombre, apellido, fecha_nac, salario, tipo, antiguedad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (self.nombre_usuario, self.contraseña, self.nombre, self.apellidos, self.fecha_nac, self.salario, self.tipo_usuario, self.antiguedad))
            conexion.commit()
            print("\nPresidente registrado correctamente")
        except Exception as e:
            print(f"\nError al registrar presidente: {e}")

    @staticmethod
    def gestionar_equipo(id,idEquipo):
        print("...:: Gestión del equipo ::...")
        print("\n\n1. Ver Jugadores\n2. Contratar Jugador\n3. Despedir Jugador")
        op = input("Elige una opción: ")

        if op == "1":
            borrarPantalla()
            print("...:: Ver Jugadores ::...")
            try:
                cursor.execute("SELECT * FROM usuarios WHERE tipo = 'Jugador' and equipo_jug = %s", (idEquipo,))
                resultado = cursor.fetchall()
                if resultado:
                    print("\nLista de jugadores:")
                    for jugador in resultado:
                        print(f"\nID: {jugador[0]}")
                        print(f"Nombre: {jugador[3]} {jugador[4]}")
                        print(f"Salario: {jugador[6]}")
                        print(f"Número de camiseta: {jugador[8]}")
                        print("\n-----------------------------------------")
                    esperaTecla()
                else:
                    print("\nNo hay jugadores en el equipo.")
                    esperaTecla()
            except Exception as e:
                print(f"\nError al mostrar jugadores: {e}")
                esperaTecla()

        elif op == "2":
            borrarPantalla()
            print("...:: Contratar Jugador ::...")
            try:
                cursor.execute("SELECT * FROM usuarios WHERE tipo = 'Jugador' and equipo_jug = 0")
                resultado = cursor.fetchall()
                if resultado:
                    print("\nLista de jugadores disponibles:")
                    for jugador in resultado:
                        print(f"\nID: {jugador[0]}")
                        print(f"Nombre: {jugador[3]} {jugador[4]}")
                        print(f"Salario: {jugador[6]}")
                        print(f"Número de camiseta: {jugador[8]}")
                        print("\n-----------------------------------------")
                    contrato = int(input("Ingrese el ID del jugador a contratar: "))
                    eleccion = input("¿Desea contratar a este jugador? (s/n): ")
                    if eleccion == "s":
                        Presidente.contratoJugador(contrato,idEquipo)
                    else:
                        print("\nNo se contrató al jugador.")
                    esperaTecla()
                else:
                    print("\nNo hay jugadores disponibles.")
                    esperaTecla()
            except Exception as e:
                print(f"\nError al mostrar jugadores: {e}")
                esperaTecla()

        elif op == "3":
            borrarPantalla()
            print("...:: Despedir Jugador ::...")
            try:
                cursor.execute("SELECT * FROM usuarios WHERE tipo = 'Jugador' and equipo_jug = %s", (idEquipo,))
                resultado = cursor.fetchall()
                if resultado:
                    print("\nLista de jugadores del equipo:")
                    for jugador in resultado:
                        print(f"\nID: {jugador[0]}")
                        print(f"Nombre: {jugador[3]} {jugador[4]}")
                        print(f"Salario: {jugador[6]}")
                        print(f"Número de camiseta: {jugador[8]}")
                        print("\n-----------------------------------------")
                    despido = int(input("Ingrese el ID del jugador a despedir: "))
                    eleccion = input("¿Desea despedir a este jugador? (s/n): ")
                    if eleccion == "s":
                        cursor.execute("UPDATE usuarios SET equipo_jug = 0 WHERE id = %s", (despido,))
                        conexion.commit()
                        print("\n¡ Jugador despedido correctamente :D !")
                        esperaTecla()
                    else:
                        print("\nNo se despidió al jugador.")
                        esperaTecla()
                else:
                    print("\nNo hay jugadores en el equipo.")
                esperaTecla()
            except Exception as e:
                print(f"\nError al mostrar jugadores: {e}")
                esperaTecla()
        else:
            print("\nOpción inválida.")
            esperaTecla()

    @staticmethod
    def fijar_presupuesto(id_presidente, presupuesto):
        try:
            cursor.execute("UPDATE equipo SET presupuesto = %s WHERE presidente = %s", (presupuesto, id_presidente))
            conexion.commit()
            print("\n¡ Nuevo presupuesto fijado correctamente :D !")
        except Exception as e:
            print(f"\nError al fijar presupuesto: {e}")

    @staticmethod
    def iniciar_sesion(nombre_usuario, contraseña):
        try:
            cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = %s AND contraseña = %s AND tipo = 'Presidente'", (nombre_usuario, contraseña))
            user = cursor.fetchone()
            if user:
                return user
            else:
                return[]
        except Exception as e:
            print(f"\nError al iniciar sesión: {e}")
            return[]

    @staticmethod
    def registrarPartido(partido: Partido):
        try:
            cursor.execute("INSERT INTO partido (idEq1, idEq2, fecha, estado, estadio) VALUES (%s, %s, %s, %s, %s)", (partido.id_equipo1, partido.id_equipo2, partido.fecha, partido.estado, partido.estadio))
            conexion.commit()
            print("\nPartido registrado correctamente")
        except Exception as e:
            print(f"\nError al registrar partido: {e}")

    @staticmethod
    def estadisticasEquipo(partido,idEquipo,idPres):
        try:
            cursor.execute("SELECT golesT FROM goles WHERE id_partido = %s", (partido,))
            golesT = cursor.fetchone()
            cursor.execute("SELECT id_jugador, minuto FROM goles WHERE id_equipo = %s", (idEquipo,))
            goles = cursor.fetchall()
            print(f"\nGoles totales del partido: {golesT[0]}")
            print("\nGoles por jugador:")
            for gol in goles:
                print(f"ID Jugador: {gol[0]} - Minuto: {gol[1]}")
        except Exception as e:
            print(f"\nError al mostrar estadísticas: {e}")
            return []
    