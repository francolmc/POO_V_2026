"""
from models.guerrero import Guerrero
from models.gremio import Gremio

thor = Guerrero("Thor", 5, 100, 80)
puga = Guerrero("Mr. Puga", 20, 100, 90)
dragon = Guerrero("Dragón", 10, 100, 60)

# Dependencia
print(thor.atacar(dragon))

# Creamos al gremio
los_bakancitos = Gremio("Los Bakancitos")

los_bakancitos.reclutar(thor)
los_bakancitos.reclutar(puga)

print(los_bakancitos.atacar_todos(dragon))
"""
from database.conexion import obtener_conexion, crear_tablas
from models.guerrero import Guerrero
from repositories.personaje_repository import PersonajeRepository

conexion = obtener_conexion()

crear_tablas(conexion)

thor = Guerrero("Thor", 6, 100, 60, "Guerrero")

print(f"Soy: {thor.nombre}")

p_repositorio = PersonajeRepository(conexion)
id_personaje = p_repositorio.crear(thor)

print(f"Thor fue creado con el id: {id_personaje}")

conexion.close()