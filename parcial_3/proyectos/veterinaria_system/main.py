from clases import Empleado, Cliente, Cita, Animales, Veterinaria, Servicio
import os
os.system("cls")

def main():
    while True:
        print("\nMenú:")
        print("1. Registrar Empleado")
        print("2. Registrar Cliente")
        print("3. Agendar Cita")
        print("4. Registrar Animal")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            NombreC = input("Nombre Completo: ")
            AñoContratacion = int(input("Año de Contratación: "))
            Edad = int(input("Edad: "))
            Rol = input("Rol: ")
            Telefono = input("Teléfono: ")
            Direccion = input("Dirección: ")
            Genero = input("Género: ")
            Email = input("Email: ")
            empleado = Empleado(None, NombreC, AñoContratacion, Edad, Rol, Telefono, Direccion, Genero, Email)
            Empleado.agregarEmpleado(empleado)
            print("Empleado registrado exitosamente.")
            print("************************************")

        elif opcion == "2":
            NombreC = input("Nombre Completo: ")
            Num_tel = input("Número de Teléfono: ")
            Genero = input("Género: ")
            Edad = int(input("Edad: "))
            Email = input("Email: ")
            cliente = Cliente(None, NombreC, Num_tel, Genero, Edad, Email)
            Cliente.registrarCliente(cliente)
            print("Cliente registrado exitosamente.")
            print("************************************")

        elif opcion == "3":
            Ficha = input("Ficha: ")
            Fecha = input("Fecha: ")
            IdCliente = int(input("ID Cliente: "))
            IdAnimal = int(input("ID Animal: "))
            cita = Cita(None, Ficha, Fecha, IdCliente, IdAnimal)
            Cita.agendarCita(cita)
            print("Cita agendada exitosamente.")
            print("************************************")

        elif opcion == "4":
            Tipoanimal = input("Tipo de Animal: ")
            Edad = int(input("Edad: "))
            Raza = input("Raza: ")
            Peso = int(input("Peso: "))
            Altura = int(input("Altura: "))
            Color = input("Color: ")
            Sexo = input("Sexo: ")
            animal = Animales(None, Tipoanimal, Edad, Raza, Peso, Altura, Color, Sexo)
            Animales.agregarAnimal(animal)
            print("Animal registrado exitosamente.")

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
