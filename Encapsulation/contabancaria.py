class Contabancaria():
    id = 1

    def __init__(self, titular, saldo):
        self.id = Contabancaria.id
        self.__titular = titular
        self._saldo = saldo

        Contabancaria.id += 1

    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            raise ValueError("valor não pode ser negativo")

    def __str__(self):
        return f"Conta {self.id}: {self.titular}, Saldo: R$ {self.saldo:.2f}"