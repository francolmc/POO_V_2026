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

try:
    conexion = obtener_conexion()

    crear_tablas(conexion)

    p_repositorio = PersonajeRepository(conexion)
    personaje1 = p_repositorio.obtener_por_id(1)

    print(personaje1.nombre)

    """
    nombre = input("Ingrese el nombre del personaje: ")
    while True:
        try:
            nivel = int(input("Ingrese el nivel del personaje: "))
            break
        except ValueError:
            print("Solo puede ingresar numeros para el nivel.")

    thor = Guerrero(nombre, nivel, 100, 60, "Guerrero")

    print(f"Soy: {thor.nombre}")

    p_repositorio = PersonajeRepository(conexion)
    id_personaje = p_repositorio.crear(thor)

    if id_personaje == -1:
        print("Error al crear el personaje.")
    else:
        print(f"{thor.nombre} fue creado con el id: {id_personaje}")
    """
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()