# Polimorfismo

class Playlist:
    def __init__(self, nombre, multimedia):
        self._nombre = nombre
        self._multimedia = multimedia
        
    @property
    def lista(self):
        return self._multimedia

    @property
    def tamaño(self):
        return len(self._multimedia)


class Multimedia:
    def __init__(self, nombre, año):
        self._nombre = nombre
        self.año = año
        self._me_gusta = 0

    def gusta(self):
        self._me_gusta += 1

    @property
    def nombre(self):
        return self._nombre

    @property
    def me_gusta(self):
        return self._me_gusta

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre.title()

    def __str__(self):
        print(" ")
        print(f'Nombre de película: {self.nombre.title()}')
        print(f'Año: {self.año}')
        print(f'Cantidad de likes: {self._me_gusta}')
        print(" ")


class Pelicula(Multimedia):
    def __init__(self, nombre, año, duracion):
        super().__init__(nombre, año)
        self.duracion = duracion
        self._me_gusta = 0

    def __str__(self):
        print(" ")
        print(f'Nombre de película: {self.nombre.title()}')
        print(f'Año: {self.año}')
        print(f'Duración: {self.duracion} min')
        print(f'Cantidad de likes: {self.me_gusta}')
        print(" ")


class Serie(Multimedia):
    def __init__(self, nombre, año, temporadas):
        super().__init__(nombre, año)
        self.temporadas = temporadas
        self._me_gusta = 0

    def __str__(self):
        print(" ")
        print(f'Nombre de serie: {self.nombre.title()}')
        print(f'Año: {self.año}')
        print(f'Temporada: {self.temporadas}')
        print(f'Cantidad de likes: {self.me_gusta}')


multimedia = Multimedia('Dragón: La historia de Bruce Lee', '1993')
spr = Pelicula('salvando al soldado ryan', '1998', '170')
hl = Serie('hartland', 2007, 16)
kb = Pelicula('kill bill', '2002', '120')
dark = Serie('dark', 2016, 3)


multimedia.__str__()
spr.__str__()
hl.__str__()
print(" ")

print("-----------------")
multimedia.gusta()
multimedia.gusta()
multimedia.gusta()
multimedia.gusta()

multimedia.nombre = 'pequeño dragon: La historia de Bruce Lee'
multimedia.__str__()
print(" ")


print("-----------------")
spr.gusta()
spr.gusta()
spr.gusta()
spr.gusta()

spr.nombre = 'rescatando al soldado ryan'
spr.__str__()
print(" ")


print("-----------------")


hl.gusta()
hl.gusta()
hl.gusta()
hl.gusta()
hl.gusta()
hl.gusta()

hl.nombre = 'new hartland'
hl.__str__()
print(" ")

# print("-----------------")


kb.gusta()
kb.gusta()
kb.gusta()
kb.gusta()
kb.gusta()
kb.gusta()


# print("-----------------")


dark.gusta()
dark.gusta()
dark.gusta()
dark.gusta()
dark.gusta()
dark.gusta()

series_peliculas = [spr, hl, kb, dark]

for i in series_peliculas:
    i.__str__()
    print("")

playlist_fds = Playlist('Playlist de fin de semana', series_peliculas)

for contenido in playlist_fds.lista:
    print(" ")
    print("Para ver el fin de semana ")
    print(" ")
    contenido.__str__()
    print(" ")
print(f'Tamaño de la playlist: {playlist_fds.tamaño}')
print(" ")

# Lo que aprendimos en esta aula:

# Algunos beneficios sobre el uso de la herencia;
# Polimorfismo;
# Relaciones entre clases;
# Representación textual de un objeto.

# Lo que aprendimos en esta aula:

# Herencia de una clase incorporada (nativa);
# Ventajas de la herencia de un iterable;
# Desventajas en el uso de la herencia.
