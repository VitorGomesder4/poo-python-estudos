from agregadormodulo.agregador import Pessoa

class Atendente(Pessoa):
    def __init__(self, nome, idade, altura, peso, sexo, salario):
        super().__init__(nome, idade, altura, peso, sexo)
        self.salario = float(salario)

    def __str__(self):
        return super().__str__() + ", Salario: {}".format(self.salario)