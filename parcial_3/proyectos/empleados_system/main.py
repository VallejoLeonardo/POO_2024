import mysql.connector
from mysql.connector import Error
import os
os.system("cls")

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def __str__(self):
        return f"Nombre: {self.nombre}, Puesto: {self.puesto}, Salario: {self.salario}"

class EmpleadoSystem:
    def __init__(self):
        self.conexion = self.crear_conexion()

    def crear_conexion(self):
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                database='mi_empresa',
                user='root',
                password=''
            )
            if conexion.is_connected():
                print("Conexión exitosa a la base de datos")
                return conexion
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def cerrar_conexion(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")

    def crear_empleado(self, nombre, puesto, salario):
        cursor = self.conexion.cursor()
        query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
        valores = (nombre, puesto, salario)
        cursor.execute(query, valores)
        self.conexion.commit()
        print("Empleado creado exitosamente")

    def leer_empleados(self):
        cursor = self.conexion.cursor()
        query = "SELECT * FROM empleados"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            empleado = Empleado(fila[1], fila[2], fila[3])
            print(empleado)

    def actualizar_empleado(self, id, nombre, puesto, salario):
        cursor = self.conexion.cursor()
        query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id = %s"
        valores = (nombre, puesto, salario, id)
        cursor.execute(query, valores)
        self.conexion.commit()
        print("Empleado actualizado exitosamente")

    def eliminar_empleado(self, id):
        cursor = self.conexion.cursor()
        query = "DELETE FROM empleados WHERE id = %s"
        valor = (id,)
        cursor.execute(query, valor)
        self.conexion.commit()
        print("Empleado eliminado exitosamente")

    def menu(self):
        if self.conexion:
            while True:
                print("\n--- Menú de Opciones ---")
                print("1. Crear empleado")
                print("2. Leer empleados")
                print("3. Actualizar empleado")
                print("4. Eliminar empleado")
                print("5. Salir")
                opcion = input("Elige una opción: ")

                if opcion == '1':
                    nombre = input("Nombre: ")
                    puesto = input("Puesto: ")
                    salario = input("Salario: ")
                    self.crear_empleado(nombre, puesto, salario)
                elif opcion == '2':
                    self.leer_empleados()
                elif opcion == '3':
                    id = input("ID del empleado a actualizar: ")
                    nombre = input("Nuevo nombre: ")
                    puesto = input("Nuevo puesto: ")
                    salario = input("Nuevo salario: ")
                    self.actualizar_empleado(id, nombre, puesto, salario)
                elif opcion == '4':
                    id = input("ID del empleado a eliminar: ")
                    self.eliminar_empleado(id)
                elif opcion == '5':
                    self.cerrar_conexion()
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")

if __name__== "__main__":
    sistema_empleados = EmpleadoSystem()
    sistema_empleados.menu()