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