class perro:
    def __init__(self, nombre, edad, raza):
        # Dentro del código del constructor vamos a definir el estado
        # inicial de cualquier perro que sea creado
        self.name = nombre
        self.age = edad
        self.race = raza

# Metodos para realizar una accion como aumentar la edad mas 1
    def cumple(self):
        self.age += 1

# Metodo para devolver el nombre
    def getName(self):
        return self.name

miperro = perro("Boby", 5, "Poodle")
print(miperro.name)
print("\nEl nombre de mi perro es",miperro.getName())