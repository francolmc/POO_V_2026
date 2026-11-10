import sqlite3
from models.personaje import Personaje

# El repositorio es una representacion de la tabla en la aplicacion.
class PersonajeRepository:
    def __init__(self, conexion: sqlite3.Connection):
        self.__conexion = conexion

    def crear(self, personaje: Personaje) -> int:
        cursor = self.__conexion.execute("""
            INSERT INTO personajes 
            (nombre, tipo, nivel, vida, poder) 
            VALUES (?, ?, ?, ?, ?)
        """, (
            personaje.nombre, personaje.tipo, personaje.nivel, 
            personaje.vida, personaje.poder
        ))
        # Esto es necesario para materializar el insert
        self.__conexion.commit()
        personaje.id = cursor.lastrowid # nos trae el id del registro creado
        return personaje.id



