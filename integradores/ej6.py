# falta hacerlo
class Persona():
    def __init__(self, nombre='Sofi', edad=0, dni=0) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if int(edad) > 0 and int(edad) < 150:
            self.__edad = int(edad)
        else:
            self.__edad = 0

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni
 
    def mostrar(self):
        return "Nombre:"+self.__nombre+" - Edad:"+str(self.__edad)+" - DNI:"+str(self.__dni)

    def es_mayor_de_edad(self):
        return self.__edad >= 18

P = Persona('Sofi', 15, 40494199)
print(P.mostrar())

print(P.es_mayor_de_edad())



p1 = Persona()
p1.set_nombre('So')
p1.set_edad(15)
p1.set_dni(40)
print(p1.mostrar())
