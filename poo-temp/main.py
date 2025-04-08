from agregadormodulo.agregador import Pessoa, Atendente, Farmaceutico
pessoa = Pessoa("Nome", 20, 1.75, 55.5, "Masculino")
print(pessoa)
print()
atendente = Atendente(pessoa.nome, pessoa.idade, pessoa.peso, pessoa.peso, pessoa.sexo, 543)
print(atendente)