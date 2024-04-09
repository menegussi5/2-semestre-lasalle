class Empregado:
  def __init__(self, nome, idade, cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf

class Funcionario(Empregado):
  def __init__(self, nome, idade, cpf, salario):
    super().__init__(nome, idade, cpf)
    self.salario = salario

  def calculaSalario(self):
    return self.salario

class Faxineiro(Empregado):
  def __init__(self, nome, idade, cpf, horaTrabalhada, valorHora):
    super().__init__(nome, idade, cpf)
    self.horaTrabalhada = horaTrabalhada
    self.valorHora = valorHora

  def calculaSalario(self):
    return self.horaTrabalhada * self.valorHora

funcionarios = []
faxineiros = []
usuarios = []

while True:
    print('\nEscolha uma opção:')
    print('1 - Opções Funcionário')
    print('2 - Opções Faxineiro')
    print('x - Opções Usuário')
    print('x - Opções Livro')
    print('x - Sair do sistema')
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        print('\nEscolha uma opção:')
        print('1 - Cadastrar funcionário:')
        print('2 - Consultar funcionário:')
        print('0 - Voltar:')
        opcaoFuncionario = int(input('Digite uma opção: '))
        
        if opcaoFuncionario == 1:
            nome = input('Insira o nome do funcionário: ')
            idade = input('Insira a idade do funcionário: ')
            salario = int(input('Insira o salário do funcionário: '))
            cpf = int(input('Insira o CPF do funcionário: '))
            funcionario = Funcionario(nome, idade, cpf, salario)
            funcionarios.append(funcionario)
        
        if opcaoFuncionario == 2:
            cont = 0
            print('\nFuncionários cadastrados no sistema:')
            for funcionario in funcionarios:
                cont = cont + 1
                print(f'{cont} - {funcionario.nome}')
            print()
            
            opcaoConsultaFuncionario = int(input('Digite o funcionário desejado: ')) -1
            if opcaoConsultaFuncionario >= 0 and opcaoConsultaFuncionario < len(funcionarios):
                funcionario1 = funcionarios[opcaoConsultaFuncionario].nome
                
                encontrou = False
                for funcionario in funcionarios:
                    if funcionario.nome == funcionario1:
                        encontrou = True
                        print('\n', 5*'-=', f'Dados do funcionário "{funcionario.nome}":', 5*'-=')
                        print(f'Nome do funcionário: {funcionario.nome}')
                        print(f'Idade do funcionário: {funcionario.idade}')
                        print(f'Salário do funcionário: R${funcionario.salario:.2f}')
                        print(f'CPF do funcionário: {funcionario.cpf}')
                        print(28*'-=')
                if not encontrou:
                    print('Funcionário não encontrado')
            else:
                print('Opção inválida')
                
        if opcaoFuncionario == 0:
            break
        
    if opcao == 2:
        print('\nEscolha uma opção:')
        print('1 - Cadastrar faxineiro:')
        print('2 - Consultar faxineiro:')
        print('0 - Voltar:')
        opcaoFaxineiro = int(input('Digite uma opção: '))
        
        if opcaoFaxineiro == 1:
            nome = input('Insira o nome do faxineiro: ')
            idade = input('Insira a idade do faxineiro: ')
            cpf = int(input('Insira o CPF do faxineiro: '))
            horaTrabalhada = int(input('Insira a hora trabalhada do faxineiro: '))
            valorHora = int(input('Insira o valor da hora do faxineiro: '))
            faxineiro = Faxineiro(nome, idade, cpf, horaTrabalhada, valorHora)
            faxineiros.append(faxineiro)
        
        if opcaoFaxineiro == 2:
            cont = 0
            print('\nFaxineiros cadastrados no sistema:')
            for faxineiro in faxineiros:
                cont = cont + 1
                print(f'{cont} - {faxineiro.nome}')
            print()
            
            opcaoConsultaFaxineiro = int(input('Digite o faxineiro desejado: ')) -1
            if opcaoConsultaFaxineiro >= 0 and opcaoConsultaFaxineiro < len(faxineiros):
                faxineiro1 = faxineiros[opcaoConsultaFaxineiro].nome
                
                encontrou = False
                for faxineiro in faxineiros:
                    if faxineiro.nome == faxineiro1:
                        encontrou = True
                        print('\n', 5*'-=', f'Dados do faxineiro "{faxineiro.nome}":', 5*'-=')
                        print(f'Nome do faxineiro: {faxineiro.nome}')
                        print(f'Idade do faxineiro: {faxineiro.idade}')
                        print(f'CPF do faxineiro: {faxineiro.cpf}')
                        print(f'Salário do faxineiro: R${faxineiro.calculaSalario():.2f}')
                        print(28*'-=')
                if not encontrou:
                    print('Faxineiro não encontrado')
            else:
                print('Opção inválida')
                
        if opcaoFaxineiro == 0:
            break