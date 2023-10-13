# 1.Repaso
# 2.Métodos y atributos

class Pelicula:
    def __init__(self, nombre, año, duracion):
        self.__nombre = nombre
        self.año = año
        self.duracion = duracion
        self.__me_gusta = 0

    def gusta(self):
        self.__me_gusta += 1

    @property
    def nombre(self):
        return self.__nombre

    @property
    def me_gusta(self):
        return self.__me_gusta

    def __str__(self):
        print(" ")
        print(f'Nombre de película: {self.nombre.title()}')
        print(f'Año: {self.año}')
        print(f'Duración: {self.duracion}')
        print(f'Cantidad de likes: {self.me_gusta}')
        print(" ")


class Serie:
    def __init__(self, nombre, año, temporadas):
        self.__nombre = nombre
        self.año = año
        self.temporadas = temporadas
        self.__me_gusta = 0

    def gusta(self):
        self.__me_gusta += 1

    @property
    def nombre(self):
        return self.__nombre

    @property
    def me_gusta(self):
        return self.__me_gusta

    def __str__(self):
        print(" ")
        print(f'Nombre de serie: {self.nombre.title()}')
        print(f'Año: {self.año}')
        print(f'Temporada: {self.temporadas}')
        print(f'Cantidad de likes: {self.me_gusta}')
        print(" ")


spr = Pelicula('salvando al soldado ryan', '1998', '170')
hl = Serie('hartland', 2007, 16)

spr.__str__()
hl.__str__()
print(" ")

print("-----------------")
spr.gusta()
spr.gusta()
spr.gusta()
spr.gusta()

spr.__str__()
print(" ")


print("-----------------")


hl.gusta()
hl.gusta()
hl.gusta()
hl.gusta()
hl.gusta()
hl.gusta()

hl.__str__()
print(" ")


