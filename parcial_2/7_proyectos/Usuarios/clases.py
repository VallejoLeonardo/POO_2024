import os
os.system('cls')

class Usuarios:
    def __init__(self,nombre,direccion,tel):
        self.nombre=nombre
        self.direccion=direccion
        self.tel=tel

    def Info_usuario(self,info_usuario):
        self.info_usuario=info_usuario
        return self.info_usuario
        
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre 

    def getDireccion(self):
        return self.direccion
    def setDireccion(self,direccion):
        self.direccion=direccion

    def getTel(self):
        return self.tel
    def setTel(self,tel):
        self.tel=tel
    
    def getInfo(self):
        print(self.getNombre(), self.getDireccion(), {self.getTel()})    

class Clientes(Usuarios):
    def __init__(self,nombre,direccion,tel,num_cliente):
        super().__init__(nombre,direccion,tel)
        self.num_cliente=num_cliente

    def Info_usuario(self,info_usuario):
        self.info_usuario=info_usuario
        return self.info_usuario

    def getNumcliente(self):
        return self.Numcliente
    def setNumcliente(self,Numcliente):
        self.Numcliente=Numcliente

    def getInfo1(self):
        (f"Su nombre es: {self.getNombre()}, Su direccion registrada es: {self.getDireccion()} \nSu numero de telefono: {self.getTel()}") 

class Empleados(Usuarios):
    def __init__(self,nombre,direccion,tel,salario,num_empleado,tipo):
        super().__init__(nombre,direccion,tel)
        self.salario=salario
        self.num_empleado=num_empleado
        self.tipo=tipo

    def Info_usuario(self,info_usuario):
        self.info_usuario=info_usuario
        return self.info_usuario

    def getSalario(self):
        return self.salario
    def setSalario(self,salario):
        self.salario=salario

    def getNumempleado(self):
        return self.num_empleado
    def setNumempleado(self,num_empleado):
        self.num_empleado=num_empleado

    def getTipo(self):
        return self.tipo
    def setTipo(self,tipo):
        self.tipo=tipo

    def getInfo2(self):
        print(f"Su nombre es: {self.getNombre()}, Su direccion registrada es: {self.getDireccion()} \nSu numero de telefono: {self.getTel()}, Su salario es:{self.getSalario()}, Su numero de empleado es:{self.getNumempleado()}, Su tipo de empleado es:{self.getTipo()}")  