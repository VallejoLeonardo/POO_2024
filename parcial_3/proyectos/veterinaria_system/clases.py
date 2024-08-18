from conexionBD import conexion, cursor

class Empleado:
    def __init__(self, idEmpleado, NombreC, AñoContratacion, Edad, Rol, Telefono, Direccion, Genero, Email):
        self.idEmpleado = idEmpleado
        self.NombreC = NombreC
        self.AñoContratacion = AñoContratacion
        self.Edad = Edad
        self.Rol = Rol
        self.Telefono = Telefono
        self.Direccion = Direccion
        self.Genero = Genero
        self.Email = Email

    @staticmethod
    def agregarEmpleado(empleado):
        cursor.execute("""
            INSERT INTO Empleado (NombreC, AñoContratacion, Edad, Rol, Telefono, Direccion, Genero, Email)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (empleado.NombreC, empleado.AñoContratacion, empleado.Edad, empleado.Rol, empleado.Telefono, empleado.Direccion, empleado.Genero, empleado.Email))
        conexion.commit()

    @staticmethod
    def eliminarEmpleado(idEmpleado):
        cursor.execute("DELETE FROM Empleado WHERE idEmpleado=%s", (idEmpleado,))
        conexion.commit()

    @staticmethod
    def modificarEmpleado(idEmpleado, datos):
        cursor.execute("""
            UPDATE Empleado SET NombreC=%s, AñoContratacion=%s, Edad=%s, Rol=%s, Telefono=%s, Direccion=%s, Genero=%s, Email=%s
            WHERE idEmpleado=%s
        """, (*datos, idEmpleado))
        conexion.commit()

class Veterinaria:
    def __init__(self, IdVeterinaria, Telefono, Direccion, Email):
        self.IdVeterinaria = IdVeterinaria
        self.Telefono = Telefono
        self.Direccion = Direccion
        self.Email = Email

    @staticmethod
    def agregarEmpleado(empleado):
        cursor.execute("""
            INSERT INTO Veterinaria (Telefono, Direccion, Email)
            VALUES (%s, %s, %s)
        """, (empleado.Telefono, empleado.Direccion, empleado.Email))
        conexion.commit()

    @staticmethod
    def eliminarEmpleado(idVeterinaria):
        cursor.execute("DELETE FROM Veterinaria WHERE IdVeterinaria=%s", (idVeterinaria,))
        conexion.commit()

    @staticmethod
    def modificarEmpleado(idVeterinaria, datos):
        cursor.execute("""
            UPDATE Veterinaria SET Telefono=%s, Direccion=%s, Email=%s
            WHERE IdVeterinaria=%s
        """, (*datos, idVeterinaria))
        conexion.commit()

class Servicio:
    def __init__(self, IdServicio, Precio, Empleado):
        self.IdServicio = IdServicio
        self.Precio = Precio
        self.Empleado = Empleado

    @staticmethod
    def agregarServicio(servicio):
        cursor.execute("""
            INSERT INTO Servicio (Precio, Empleado)
            VALUES (%s, %s)
        """, (servicio.Precio, servicio.Empleado))
        conexion.commit()

    @staticmethod
    def eliminarServicio(idServicio):
        cursor.execute("DELETE FROM Servicio WHERE IdServicio=%s", (idServicio,))
        conexion.commit()

    @staticmethod
    def modificarServicio(idServicio, datos):
        cursor.execute("""
            UPDATE Servicio SET Precio=%s, Empleado=%s
            WHERE IdServicio=%s
        """, (*datos, idServicio))
        conexion.commit()

class Cliente:
    def __init__(self, IdCliente, NombreC, Num_tel, Genero, Edad, Email):
        self.IdCliente = IdCliente
        self.NombreC = NombreC
        self.Num_tel = Num_tel
        self.Genero = Genero
        self.Edad = Edad
        self.Email = Email

    @staticmethod
    def registrarCliente(cliente):
        cursor.execute("""
            INSERT INTO Cliente (NombreC, Num_tel, Genero, Edad, Email)
            VALUES (%s, %s, %s, %s, %s)
        """, (cliente.NombreC, cliente.Num_tel, cliente.Genero, cliente.Edad, cliente.Email))
        conexion.commit()

    @staticmethod
    def eliminarCliente(idCliente):
        cursor.execute("DELETE FROM Cliente WHERE IdCliente=%s", (idCliente,))
        conexion.commit()

    @staticmethod
    def modificarCliente(idCliente, datos):
        cursor.execute("""
            UPDATE Cliente SET NombreC=%s, Num_tel=%s, Genero=%s, Edad=%s, Email=%s
            WHERE IdCliente=%s
        """, (*datos, idCliente))
        conexion.commit()

class Animales:
    def __init__(self, IdAnimal, Tipoanimal, Edad, Raza, Peso, Altura, Color, Sexo):
        self.IdAnimal = IdAnimal
        self.Tipoanimal = Tipoanimal
        self.Edad = Edad
        self.Raza = Raza
        self.Peso = Peso
        self.Altura = Altura
        self.Color = Color
        self.Sexo = Sexo

    @staticmethod
    def agregarAnimal(animal):
        cursor.execute("""
            INSERT INTO Animales (Tipoanimal, Edad, Raza, Peso, Altura, Color, Sexo)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (animal.Tipoanimal, animal.Edad, animal.Raza, animal.Peso, animal.Altura, animal.Color, animal.Sexo))
        conexion.commit()

    @staticmethod
    def eliminarAnimal(idAnimal):
        cursor.execute("DELETE FROM Animales WHERE IdAnimal=%s", (idAnimal,))
        conexion.commit()

    @staticmethod
    def modificarAnimal(idAnimal, datos):
        cursor.execute("""
            UPDATE Animales SET Tipoanimal=%s, Edad=%s, Raza=%s, Peso=%s, Altura=%s, Color=%s, Sexo=%s
            WHERE IdAnimal=%s
        """, (*datos, idAnimal))
        conexion.commit()

class Cita:
    def __init__(self, idCita, Ficha, Fecha, IdCliente, IdAnimal):
        self.idCita = idCita
        self.Ficha = Ficha
        self.Fecha = Fecha
        self.IdCliente = IdCliente
        self.IdAnimal = IdAnimal

    @staticmethod
    def agendarCita(cita):
        cursor.execute("""
            INSERT INTO Cita (Ficha, Fecha, IdCliente, IdAnimal)
            VALUES (%s, %s, %s, %s)
        """, (cita.Ficha, cita.Fecha, cita.IdCliente, cita.IdAnimal))
        conexion.commit()

    @staticmethod
    def eliminarCita(idCita):
        cursor.execute("DELETE FROM Cita WHERE idCita=%s", (idCita,))
        conexion.commit()

    @staticmethod
    def modificarCita(idCita, datos):
        cursor.execute("""
            UPDATE Cita SET Ficha=%s, Fecha=%s, IdCliente=%s, IdAnimal=%s
            WHERE idCita=%s
        """, (*datos, idCita))
        conexion.commit()
    
    
