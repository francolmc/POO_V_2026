# Esto es necesario para poder definir una clase abstracta
from abc import ABC, abstractmethod

class Personaje(ABC): # La clase hereda de ABC para ser abstracta
    # Constructor
    def __init__(self, nombre: str, nivel: int, vida: int, tipo: str):
        self.id = None
        self.nombre = nombre
        self.__nivel = nivel # Privado
        self.__vida = vida # Privado
        self.__tipo = tipo

    @property # Esta es la parte de lectura de la propiedad
    def vida(self) -> int:
        return self.__vida

    @vida.setter # Esta seria la parte de asignacion de la propiedad.
    def vida(self, valor: int):
        if not 0 <= valor <= 100:
            # con el comando raise lanzamos una excepcion (error)
            raise ValueError("La vida debe estar entre 0 y 100")
        self.__vida = valor

    @property
    def esta_vivo(self) -> bool:
        return self.__vida > 0

    @property
    def nivel(self) -> int:
        return self.__nivel

    @property
    def tipo(self) -> int:
        return self.__tipo

    # Metodo abstracto, el cual tendra que ser implementado por cada clase hija
    @abstractmethod
    def calcular_danio(self) -> int:
        pass

    @property
    @abstractmethod
    def poder(self) -> int:
        pass

    def recibir_danio(self, cantidad: int) -> None:
        self.__vida = max(0, self.__vida - cantidad)

    def atacar(self, objetivo: "Personaje") -> str: # Aqui es donde va la dependencia con el otro personaje
        if not isinstance(objetivo, Personaje):
            raise TypeError("Solo se puede atacatar a un Personaje")
        danio = self.calcular_danio()
        objetivo.recibir_danio(danio)
        if not objetivo.esta_vivo:
            return f"{objetivo.nombre} ya fue derrotado por {self.nombre}"
        return f"{self.nombre} ataca a {objetivo.nombre} (-{danio}) -> vida {objetivo.vida}"
