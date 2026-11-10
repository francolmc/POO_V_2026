from models.personaje import Personaje

# La clase guerrero debe heredar de Personaje
class Guerrero(Personaje):
    def __init__(self, nombre: str, nivel: int, vida: int, fuerza: int, tipo: str):
        # Con esto llamamos al constructor de la clase padre y de ese modo
        # al instaciar un objeto se realizar la instancia completa.
        super().__init__(nombre, nivel, vida, tipo)
        self.__fuerza = fuerza

    @property
    def poder(self):
        return self.__fuerza

    def calcular_danio(self) -> int:
        # Retornamos la parte entera de la division
        return self.__fuerza // 2