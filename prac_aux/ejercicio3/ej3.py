class CuentaBancaria:
    def __init__(self, titular, nroCuenta, saldo):
        self.titular = titular
        self.nroCuenta = nroCuenta
        self.saldo = saldo
    def depositar(self, monto):
        if monto <= 0:
            print("Error: no se puede depositar un monto negativo o igual a 0.")
        else:
            self.saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: bs. {self.saldo}")
    def retirar(self, monto):
        if monto > self.saldo:
            print("Error: no se puede retirar más dinero del que hay en la cuenta.")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: bs. {self.saldo}")
    def mostrar_datos(self):
        print(f"Titular: {self.titular}")
        print(f"Nro. Cuenta: {self.nroCuenta}")
        print(f"Saldo: bs. {self.saldo}")
cuenta1 = CuentaBancaria("Angel Perez", "1234567", 500)
cuenta1.mostrar_datos()
cuenta1.depositar(200)
cuenta1.retirar(1000)
cuenta1.depositar(-50)
cuenta1.retirar(100)
cuenta1.mostrar_datos()