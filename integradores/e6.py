class Persona():
     # Constructor
     def __intit__(self, nombre = 'Nombre', edad = 0, dni = 0):
            self._nombre = nombre
            self._edad = edad
            self._dni = dni

    # Getters
     def get_nombre(self):
          return self._nombre

     def get_edad(self):
          return self._edad

     def get_dni(self):
          return self._dni

    #  Setters
     def set_nombre(self, nombre):
           if nombre.isalpha():
                 self._nombre = nombre
           else:
                print("El nombre ingresado debe ser una cadena de texto.")

     def set_edad(self, edad):
           if type(edad) == int and edad > 0:
                 self._edad = edad
           else:
                print("La edad ingresada debe ser un numero natural (entero positivo).")

     def set_dni(self, dni):
            if type(dni) == int and dni > 0:
                 self._dni = dni
            else:
                print("El DNI ingresado no debe incluir puntos ni texto.")

    # Metodos
     def mostrar(self):
          print(f"Nombre: {self._nombre.capitalize()},\nEdad: {self._edad} años,\nD.N.I.: {self._dni}.")

     def es_mayor_de_edad(self):
          return self._edad >= 18

# --- PRUEBA 6
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
dni = int(input("Ingrese su DNI: "))

p1 = Persona()
p1.set_nombre(nombre)
p1.set_edad(edad)
p1.set_dni(dni)
print("---------------------6---------------------")
p1.mostrar()
print("¿Es mayor de edad?:", p1.es_mayor_de_edad())