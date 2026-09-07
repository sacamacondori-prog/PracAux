class Vehiculo:
    def __init__(self, marca, modelo, anio, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.color = "Sin definir"
    def mostrar_kilometraje(self):
        km = self.kilometraje
        m = km * 1000
        print(f"{self.marca} {self.modelo}: {km} km ({m} m)")
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print(f"El color del {self.marca} {self.modelo} ahora es {self.color}")
auto1 = Vehiculo("Toyota", "Corolla", 2020, 45000)
auto2 = Vehiculo("Nissan", "Sentra", 2019, 60000)
auto1.cambiar_color("Rojo")
auto2.cambiar_color("Azul")
auto1.mostrar_kilometraje()
auto2.mostrar_kilometraje()