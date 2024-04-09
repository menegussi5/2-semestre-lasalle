class Empregado():
    def __init__(self, nome):
        self.nome = nome
    def retornaPagamento(self):
        pass

class Assalariado(Empregado):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario
    def retornaPagamento(self):
        return self.salario
    
class Horista(Empregado):
    def __init__(self, nome, valorHora, qtdHora):
        super().__init__(nome)
        self.valorHora = valorHora
        self.qtdHora = qtdHora
    def retornaPagamento(self):
        return self.valorHora * self.qtdHora * 4.5
    
empregados = []
assalariados = []
horistas = []

while True:
    print('\nEscolha uma opção:')
    print('1 - Cadastrar assalariado')
    print('2 - Cadastrar horista')
    print('3 - Folha salarial')
    print('4 - Sair do sistema')
    opcao = int(input('Digite uma opção: '))    
        
    if opcao == 1:
        nomeAssalariado = input('Insira o nome do assalariado: ')
        salarioAssalariado = int(input('Insira o salário do assalariado: '))
        assalariado = Assalariado(nomeAssalariado, salarioAssalariado)
        empregados.append(assalariado)
        
    if opcao == 2:
        nomeHorista = input('Insira o nome do horista: ')
        valorHoraHorista = float(input('Insira o valor da hora do horista: '))
        qtdHoraHorista = int(input('Insira a quantidade de horas do horista: '))
        horista = Horista(nomeHorista, valorHoraHorista, qtdHoraHorista)
        empregados.append(horista)
        
    def folhaSalarial(empregados):
        total = 0
        for i in empregados:
            total += i.retornaPagamento()
        return total
        
    if opcao == 3:
        print(folhaSalarial(empregados))
        
              
    if opcao == 4:
        break