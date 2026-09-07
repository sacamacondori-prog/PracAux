class Computadora:
    def __init__(self, marca, procesador, ram, almacenamiento):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
pc1 = Computadora("HP", "Intel i5", 8, 512)
pc2 = Computadora(marca="Dell", procesador="Ryzen 5", ram=16, almacenamiento=1000)
X = 8
if pc1.ram == X:
    print(f"La RAM de {pc1.marca} es igual a {X} GB")
else:
    print(f"La RAM de {pc1.marca} no es igual a {X} GB")
if pc1.almacenamiento > pc2.almacenamiento:
    mayor = pc1
else:
    mayor = pc2
print(f"La computadora con mayor almacenamiento es {mayor.marca}")
print(f"Marca: {mayor.marca}")
print(f"Procesador: {mayor.procesador}")
print(f"RAM: {mayor.ram} GB")
print(f"Almacenamiento: {mayor.almacenamiento} GB")