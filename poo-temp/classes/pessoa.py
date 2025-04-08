class Pessoa():
    def __init__(self, nome, idade, altura, peso, sexo):
        self.nome = str(nome)
        self.idade = int(idade)
        self.altura = float(altura)
        self.peso = float(peso)
        self.sexo = str(sexo)
    
    def __str__(self):
        return "Nome: {}, Idade: {}, Altura: {}, Peso: {}, Sexo: {}".format(self.nome, self.idade, self.altura, self.peso, self.sexo)