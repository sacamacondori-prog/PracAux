class Bus:
    def __init__(self, capacidad_total):
        self.capacidad_total = capacidad_total
        self.pasajeros = 0
    def subir_pasajeros(self, cantidad):
        if self.pasajeros + cantidad > self.capacidad_total:
            print("Error: no hay suficientes asientos disponibles.")
        else:
            self.pasajeros += cantidad
            print(f"Subieron {cantidad} pasajeros.")
    def cobrar_pasaje(self):
        costo_pasaje = 1.50
        total = self.pasajeros * costo_pasaje
        print(f"Total cobrado a {self.pasajeros} pasajeros: bs. {total}")
    def asientos_disponibles(self):
        disponibles = self.capacidad_total - self.pasajeros
        print(f"Asientos disponibles: {disponibles}")
bus1 = Bus(40)
bus1.subir_pasajeros(15)
bus1.cobrar_pasaje()
bus1.asientos_disponibles()