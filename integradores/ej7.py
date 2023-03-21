from ej6 import Persona as P

class Cuenta:
    def __init__(self, titular = P, cantidad = 0.0) -> None:
        self.__titular = titular
        self.__cantidad = cantidad

