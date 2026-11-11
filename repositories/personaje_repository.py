import sqlite3
from models.personaje import Personaje
from models.guerrero import Guerrero

# El repositorio es una representacion de la tabla en la aplicacion.
class PersonajeRepository:
    def __init__(self, conexion: sqlite3.Connection):
        self.__conexion = conexion

    def crear(self, personaje: Personaje) -> int:
        try:
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
        except sqlite3.IntegrityError:
            print("Error al crear el personaje en la base de datos.")
            return -1


    def obtener_por_id(self, id: int):
        fila = self.__conexion.execute("""
            SELECT id, nombre, tipo, nivel, vida, poder
            FROM personajes
            WHERE id = ?
            """, (id,)).fetchone()
        tipo = fila[2]
        if tipo == "Guerrero":
            return Guerrero(fila[1], fila[3], fila[4], fila[5], "Guerrero")
        return None

    def editar():
        pass
