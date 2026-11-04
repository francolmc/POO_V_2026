from models.personaje import Personaje

# Gremio se encarga de agrupar Personajes (agregacion)
class Gremio:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__miembros = []

    @property
    def miembros(self) -> list:
        return self.__miembros

    def reclutar(self, personaje: Personaje) -> None:
        # Antes de agregar al personaje debemos validar:
        # 1- Que el personaje sea del tipo Personaje
        if not isinstance(personaje, Personaje):
            raise TypeError("Solo se pueden reclutar Personajes")
        # 2- Que el personaje no exista en el grupo
        if personaje in self.__miembros:
            raise ValueError(f"{personaje.nombre} ya esta en el gremio.")
        self.__miembros.append(personaje)

    def expulsar(self, personaje: Personaje) -> None:
        self.__miembros.remove(personaje)

    def atacar_todos(self, objetivo: Personaje) -> list[str]:
        return [p.atacar(objetivo) for p in self.__miembros if p.esta_vivo]

    def disolver(self) -> None:
        self.__miembros.clear()