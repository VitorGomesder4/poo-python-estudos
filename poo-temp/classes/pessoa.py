class Pessoa():
    def __init__(self, nome: str, idade: int, altura: float, peso: float, sexo: str):
        self.nome = nome
        self._idade = idade
        self.altura = altura
        self.peso = peso
        self.sexo = sexo

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}, Peso: {self.peso}, Sexo: {self.sexo}"

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, value):
        if not isinstance(value, int):
            raise TypeError("Essa idade não é um numero inteiro")
        else:
            self._idade = value