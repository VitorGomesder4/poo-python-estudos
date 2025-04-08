from agregadormodulo.agregador import Pessoa
class Farmaceutico(Pessoa):
    def __init__(self, nome, idade, altura, peso, sexo, salario, registro_profissional):
        super().__init__(nome, idade, altura, peso, sexo)
        self.salario = salario
        self.registro_profissional = registro_profissional

    def __str__(self):
        return super().__str__() + ", Salario: {}, Registro Profissional: {}".format(self.salario, self.registro_profissional)