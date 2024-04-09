class Funcionário():
    def __init__(self, nome, cpf, salario, departamento):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.departamento = departamento
            
    def bonificarFuncionario(self):
        self.salario = self.salario * 1.10
            
class Gerente(Funcionário):
    def __init__(self, nome, cpf, salario, departamento, senha, numeroFuncionario):
        super().__init__(nome, cpf, salario, departamento)
        self.senha = senha
        self.numeroFuncionario = numeroFuncionario
        
    def autenticarSenha(self, senha):
        if senha == self.senha:
            return True
        else:
            return False
        
    def bonificarGerente(self):
        self.salario = self.salario * 1.15
            
class Vendedor(Funcionário):
    def __init__(self, nome, cpf, salario, departamento, qtdVendas, comissao):
        super().__init__(nome, cpf, salario, departamento)
        self.qtdVendas = qtdVendas
        self.comissao = comissao
        
    def atualizaQuantidadeVendas(self, qtdVendas):
        self.qtdVendas = self.qtdVendas + qtdVendas
        
    def calculaSalario(self):
        return self.salario + self.comissao

funcionarios = []
gerentes = []
vendedores = []

while True:
    print('\nEscolha uma opção:')
    print('1 - Cadastrar funcionário')
    print('2 - Cadastrar gerente')
    print('3 - Cadastrar vendedor')
    print('4 - Consultar')
    print('5 - Bonificar')
    print('6 - Autenticar senha do gerente')
    print('7 - Atualizar quantidade de vendas')
    print('8 - Calcular o salário')
    print('0 - Encerrar programa')
    opcao = int(input('Digite a opção: '))
    
    if opcao == 1: #CADASTRAR FUNCIONARIO
        nomeFuncionario = input('\nInsira o nome do funcionário: ')
        cpfFuncionario = input('Insira o CPF do funcionário: ')
        salarioFuncionario = float(input('Insira do salário do funcionário: '))
        departamentoFuncionario = input('Insira o departamento do funcionário: ')
        
        funcionario = Funcionário(nomeFuncionario, cpfFuncionario, salarioFuncionario, departamentoFuncionario)
        funcionarios.append(funcionario)
        print('Funcionário cadastrado com sucesso!')
        
    elif opcao == 2: #CADASTRAR GERENTE
        nomeGerente = input('\nInsira o nome do gerente: ')
        cpfGerente = input('Insira o CPF do gerente: ')
        salarioGerente = float(input('Insira o salário do gerente: '))
        departamentoGerente = input('Insira o departamento do gerente: ')
        senhaGerente = int(input('Insira a senha do gerente: '))
        numFuncionario = int(input('Insira o número do funcionário: '))
        
        gerente = Gerente(nomeGerente, cpfGerente, salarioGerente, departamentoGerente, senhaGerente, numFuncionario)
        gerentes.append(gerente)
        print('Gerente cadastrado com sucesso!')
    
    elif opcao == 3: #CADASTRAR VENDEDOR
        nomeVendedor = input('\nInsira o nome do vendedor: ')
        cpfVendedor = input('Insira o CPF do vendedor: ')
        salarioVendedor = float(input('Insira o salário do vendedor: '))
        departamentoVendedor = input('Insira o departamento do vendedor: ')
        qtdVendasVendedor = int(input('Insira a quantidade de vendas que esse vendedor possui: '))
        comissaoVendedor = float(input('Insira a comissão que esse vendedor ganha: '))

        vendedor = Vendedor(nomeVendedor, cpfVendedor, salarioVendedor, departamentoVendedor, qtdVendasVendedor, comissaoVendedor)
        vendedores.append(vendedor)
        print('Vendedor cadastrado com sucesso!')

    elif opcao == 4: #INICIO LAÇO CONSULTA DADOS
        while True:
            print('\nEscolha uma opção:')
            print('1 - Consultar funcionário')
            print('2 - Consultar gerente')
            print('3 - Consultar vendedor')
            print('0 - Voltar')
            opcao1 = int(input('Digite a opção: '))
            
            if opcao1 == 1: #CONSULTA FUNCIONARIO
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
                            print(f'CPF do funcionário: {funcionario.cpf}')
                            print(f'Salário do funcionário: R${funcionario.salario:.2f}')
                            print(f'Departamento do funcionário: {funcionario.departamento}')
                            print(28*'-=')
                    if not encontrou:
                        print('Funcionário não encontrado')
                else:
                    print('Opção inválida')
            
            
            elif opcao1 == 2: #CONSULTA GERENTE
                cont = 0
                print('\nGerentes cadastrados no sistema:')
                for gerente in gerentes:
                    cont = cont + 1
                    print(f'{cont} - {gerente.nome}')
                print()
                
                opcaoConsultaGerente = int(input('Digite o gerente desejado: ')) -1
                if opcaoConsultaGerente >= 0 and opcaoConsultaGerente < len(gerentes):
                    gerente1 = gerentes[opcaoConsultaGerente].nome
                    
                    encontrou = False
                    for gerente in gerentes:
                        if gerente.nome == gerente1:
                            encontrou = True
                            print('\n', 5*'-=', f'Dados do gerente "{gerente.nome}":', 5*'-=')
                            print(f'Nome do gerente: {gerente.nome}')
                            print(f'CPF do gerente: {gerente.cpf}')
                            print(f'Salário do gerente: R${gerente.salario:.2f}')
                            print(f'Departamento do gerente: {gerente.departamento}')
                            print(f'Senha do gerente: {gerente.senha}')
                            print(f'Número de funcionário do gerente: {gerente.numeroFuncionario}')
                            print(26*'-=')
                    if not encontrou:
                        print('Gerente não encontrado')
                else:
                    print('Opção inválida')
                    
            
            elif opcao1 == 3: #CONSULTA VENDEDOR
                cont = 0
                print('\nVendedores cadastrados no sistema:')
                for vendedor in vendedores:
                    cont = cont + 1
                    print(f'{cont} - {vendedor.nome}')
                print()
                
                opcaoConsultaVendedor= int(input('Digite o vendedor desejado: ')) -1
                if opcaoConsultaVendedor >= 0 and opcaoConsultaVendedor < len(vendedores):
                    vendedor1 = vendedores[opcaoConsultaVendedor].nome
                    
                    encontrou = False
                    for vendedor in vendedores:
                        if vendedor.nome == vendedor1:
                            encontrou = True
                            print('\n', 5*'-=', f'Dados do vendedor "{vendedor.nome}":', 5*'-=')
                            print(f'Nome do vendedor: {vendedor.nome}')
                            print(f'CPF do vendedor: {vendedor.cpf}')
                            print(f'Salário do vendedor: R${vendedor.salario:.2f}')
                            print(f'Departamento do vendedor: {vendedor.departamento}')
                            print(f'Quantidade de vendas do vendedor: {vendedor.qtdVendas}')
                            print(f'Comissão do vendedor: R${vendedor.comissao}')
                            print(27*'-=')
                    if not encontrou:
                        print('Gerente não encontrado')
                else:
                    print('Opção inválida')
            
            
            elif opcao1 == 0: #FIM LAÇO CONSULTA DADOS
                break
            
            else:
                print('Opção inválida')
            
    
    elif opcao == 5: #BONIFICAR
        while True:
            print('\nEscolha uma opção:')
            print('1 - Bonificar funcionário')
            print('2 - Bonificar gerente')
            print('0 - Voltar')
            opcao2 = int(input('Digite a opção: '))
            
            if opcao2 == 1: #FUNCIONARIO
                cont = 0
                print('\nFuncionários cadastrados no sistema:')
                for funcionario in funcionarios:
                    cont = cont + 1
                    print(f'{cont} - {funcionario.nome}')
                print()
                
                opcaoConsultaFuncionario1 = int(input('Digite o funcionário desejado: ')) -1
                if opcaoConsultaFuncionario1 >= 0 and opcaoConsultaFuncionario1 < len(funcionarios):
                    funcionario2 = funcionarios[opcaoConsultaFuncionario1].nome
                    
                    encontrou = False
                    for funcionario in funcionarios:
                        if funcionario.nome == funcionario2:
                            encontrou = True
                            print('\n', 5*'-=', f'Salário do funcionário "{funcionario.nome}":', 5*'-=')
                            print(f'Salário antigo: R${funcionario.salario:.2f}')
                            funcionario.bonificarFuncionario()
                            print(f'Salário novo (+10%): R${funcionario.salario:.2f}')
                            print(29*'-=')
                    if not encontrou:
                        print('Funcionário não encontrado')
                else:
                    print('Opção inválida')
                    
                    
            elif opcao2 == 2: #GERENTE
                cont = 0
                print('\nGerentes cadastrados no sistema:')
                for gerente in gerentes:
                    cont = cont + 1
                    print(f'{cont} - {gerente.nome}')
                print()
                
                opcaoConsultaGerente1 = int(input('Digite o gerente desejado: ')) -1
                if opcaoConsultaGerente1 >= 0 and opcaoConsultaGerente1 < len(gerentes):
                    gerente2 = gerentes[opcaoConsultaGerente1].nome
                    
                    encontrou = False
                    for gerente in gerentes:
                        if gerente.nome == gerente2:
                            encontrou = True
                            print('\n', 5*'-=', f'Salário do gerente "{gerente.nome}":', 5*'-=')
                            print(f'Salário antigo: R${gerente.salario:.2f}')
                            gerente.bonificarGerente()
                            print(f'Salário novo (+15%): R${gerente.salario:.2f}')
                            print(28*'-=')
                    if not encontrou:
                        print('Gerente não encontrado')
                else:
                    print('Opção inválida')
                    
                    
            elif opcao2 == 0: #FIM LAÇO BONIFICAR
                break
            
            else:
                print('Opção inválida')
                
                
    elif opcao == 6: #AUTENTICAR SENHA GERENTE
        cont = 0
        print('\nGerentes cadastrados no sistema:')
        for gerente in gerentes:
            cont = cont + 1
            print(f'{cont} - {gerente.nome}')
        print()
        
        opcaoConsultaGerente2 = int(input('Digite o gerente desejado: ')) -1
        if opcaoConsultaGerente2 >= 0 and opcaoConsultaGerente2 < len(gerentes):
            gerente3 = gerentes[opcaoConsultaGerente2].nome
            
            encontrou = False
            for gerente in gerentes:
                if gerente.nome == gerente3:
                    encontrou = True
                    senhaNum = int(input(f'\nDigite a senha do gerente "{gerente.nome}": '))
                    senhaVerificar = gerente.autenticarSenha(senhaNum)
                    if senhaVerificar == True:
                        print('Senha AUTORIZADA com SUCESSO!')
                    else:
                        print('Senha NEGADA')
            if not encontrou:
                print('Gerente não encontrado')
        else:
            print('Opção inválida')
            
            
    elif opcao == 7: #ATUALIZAR QTD DE VENDAS VENDEDOR
        cont = 0
        print('\nVendedores cadastrados no sistema:')
        for vendedor in vendedores:
            cont = cont + 1
            print(f'{cont} - {vendedor.nome}')
        print()
        
        opcaoConsultaVendedor1 = int(input('Digite o vendedor desejado: ')) -1
        if opcaoConsultaVendedor1 >= 0 and opcaoConsultaVendedor1 < len(vendedores):
            vendedor2 = vendedores[opcaoConsultaVendedor1].nome
            
            encontrou = False
            for vendedor in vendedores:
                if vendedor.nome == vendedor2:
                    encontrou = True
                    print('\n', 1*'-=', f'Quantidade de vendas do vendedor "{vendedor.nome}":', 1*'-=')
                    print(f'{vendedor.qtdVendas} vendas atualmente')
                    print(26*'-=')
                    newQtdVendas = int(input(f'\nInsira o acréscimo de vendas para o vendedor "{vendedor.nome}": '))
                    vendedor.atualizaQuantidadeVendas(newQtdVendas)
                    print('Quantidade de vendas atualizada com sucesso para o vendedor selecionado!')
            if not encontrou:
                print('Vendedor não encontrado')
        else:
            print('Opção inválida')
            
            
    elif opcao == 8: #CALCULA SALARIO
        cont = 0
        print('\nVendedores cadastrados no sistema:')
        for vendedor in vendedores:
            cont = cont + 1
            print(f'{cont} - {vendedor.nome}')
        print()
        
        opcaoConsultaVendedor2 = int(input('Digite o vendedor desejado: ')) -1
        if opcaoConsultaVendedor2 >= 0 and opcaoConsultaVendedor2 < len(vendedores):
            vendedor3 = vendedores[opcaoConsultaVendedor2].nome
            
            encontrou = False
            for vendedor in vendedores:
                if vendedor.nome == vendedor3:
                    encontrou = True
                    print('\n', 5*'-=', f'Salário do vendedor "{vendedor.nome}":', 5*'-=')
                    print(f'Salário atual: R${vendedor.salario:.2f}')
                    print(f'Salário com comissão: R${vendedor.calculaSalario()}')
                    print(28*'-=')
            if not encontrou:
                print('Vendedor não encontrado')
        else:
            print('Opção inválida')
                    
                    
    elif opcao == 0: #ENCERRAR PROGRAMA
        print('Encerrando o programa')
        break
    
    else:
        print('Opção inválida')