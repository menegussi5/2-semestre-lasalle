class Pessoa:
    def __init__(self, nome, idade, endereco, sexo):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.sexo = sexo
        
    def setNome(self, nome):
        self.nome = nome
    def setIdade(self, idade):
        self.idade = idade
    def setEndereco(self, endereco):
        self.endereco = endereco
    def setSexo(self, sexo):
        self.sexo = sexo
        
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getEndereco(self):
        return self.endereco
    def getSexo(self):
        return self.sexo
    
p1 = Pessoa('Maria', 41, 'Av. Farroupilha 1200, Marechal Rondon, Canoas', 'Feminino')
p2 = Pessoa('João', 52, 'Rua Florianópolis 756, São Paulo, São Paulo', 'Masculino')
p3 = Pessoa('Pedro', 30, 'Rua Alexandre de Gusmão 737, Cidade Baixa, Porto Alegre', 'Masculino')

print('endereco da p1 = ', p1.getEndereco())
print('sexo da p1 = ', p1.getSexo())
print('nome da p1 = ', p1.getNome())

print()

print('idade da p2 = ', p2.getIdade())
print('sexo da p2 = ', p2.getSexo())

print()

print('nome da p3 = ', p3.getNome())
print('sexo da p3 = ', p3.getSexo())
print('endereco da p3 = ', p3.getEndereco())