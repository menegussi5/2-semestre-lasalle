class Montadora:
    def __init__(self, codigoMontadora, estado, razao):
        self.codigoMontadora = codigoMontadora
        self.estado = estado
        self.razao = razao
        
    def setCodigoMontadora(self, codigoMontadora):
        self.codigoMontadora = codigoMontadora
    def setEstado(self, estado):
        self.estado = estado
    def setRazao(self, razao):
        self.razao = razao
    
    def getCodigoMontadora(self):
        return self.codigoMontadora
    def getEstado(self):
        return self.estado
    def getRazao(self):
        return self.razao
    
class Modelo:
    def __init__(self, codigoModelo, nome, Montadora):
        self.codigoModelo = codigoModelo
        self.nome = nome
        self.montadora = Montadora
        
    def setCodigoModelo(self, codigoModelo):
        self.codigoModelo = codigoModelo
    def setNome(self, nome):
        self.nome = nome
    def setMontadora(self, Montadora):
        self.montadora = Montadora
        
    def getCodigoModelo(self):
        return self.codigoModelo
    def getNome(self):
        return self.nome
    def getMontadora(self):
        return self.montadora
    
class Carro:
    def __init__(self, placa, fabricacao, Modelo):
        self.placa = placa
        self.fabricacao = fabricacao
        self.modelo = Modelo
    
    def setPlaca(self, placa):
        self.placa = placa
    def setFabricacao(self, fabricacao):
        self.fabricacao = fabricacao
    def setModelo(self, Modelo):
        self.modelo = Modelo
    
    def getPlaca(self):
        return self.placa
    def getFabricacao(self):
        return self.fabricacao
    def getModelo(self):
        return self.modelo
    
montadoras = []
modelos = []
carros = []

while True:
    print('\nEscolha uma opção:')
    print('1 - Cadastrar montadora')
    print('2 - Cadastrar modelo')
    print('3 - Cadastrar carro')
    print('4 - Pesquisar dados')
    print('5 - Alterar dados')
    print('6 - Fechar programa')
    opcao = int(input('Digite uma opção: '))
    
    if opcao == 1: #cadastro montadora
        codigoMontadora = int(input('\nInsira o código da montadora: '))
        estado = input('Insira o estado da montadora (XX): ')
        razaoSocial = input('Insira a razão social da montadora: ')
        montadora = Montadora(codigoMontadora, estado, razaoSocial)
        montadoras.append(montadora)
        print('Montadora cadastrada com sucesso!')
        
    elif opcao == 2: #cadastro modelo
        codigoModelo = int(input('\nInsira o código do modelo: '))
        nome = input('Insira o nome do modelo: ')
        print('\nMontadoras cadastradas:')
        
        cont = 0
        for montadora in montadoras:
            cont = cont + 1
            print(f'{cont} - {montadora.getCodigoMontadora()}')
            
        opcaoMontadora = int(input(f'Insira qual montadora você quer selecionar para o modelo "{nome}": ')) -1
        if opcaoMontadora >= 0 and opcaoMontadora < len(montadoras):
            modeloMontadora = montadoras[opcaoMontadora]
            modelo = Modelo(codigoModelo, nome, modeloMontadora)
            modelos.append(modelo)
            print('Modelo cadastrado com sucesso!')
        else:
            print('Montadora inválida')
    
    elif opcao == 3: #cadastro carro
        placa = input('\nInsira a placa do carro: ')
        fabricacao = int(input('Insira o ano de fabricação do carro (xxxx): '))
        print('Modelos cadastrados:')
        
        cont = 0
        for modelo in modelos:
            cont = cont + 1
            print(f'{cont} - {modelo.getNome()}')
            
        opcaoModelo = int(input(f'Insira qual modelo você quer selecionar para o carro com a placa "{placa}": ')) -1
        if opcaoModelo >= 0 and opcaoModelo < len(modelos):
            carroModelo = modelos[opcaoModelo]
            carro = Carro(placa, fabricacao, carroModelo)
            carros.append(carro)
            print('Carro cadastrado com sucesso!')
        else:
            print('Modelo inválido')
            
    elif opcao == 4: #INICIO laço consulta dados
        while True:
            print('\nEscolha uma opção')
            print('1 - Consultar montadora')
            print('2 - Consultar modelo')
            print('3 - Consultar carro')
            print('4 - Voltar')
            opcao1 = int(input('Digite a opção: '))
            
            if opcao1 == 1: #consulta montadora
                cont = 0
                print('\nCódigos das montadoras cadastradas no sistema:')
                for montadora in montadoras:
                    cont = cont + 1
                    print(f'{cont} - {montadora.getCodigoMontadora()}')
                print()
                    
                opcaocodigo = int(input('Insira a montadora desejada: ')) -1
                if opcaocodigo >= 0 and opcaocodigo < len(montadoras):
                    codigo = montadoras[opcaocodigo].getCodigoMontadora()

                    encontrou = False
                    for montadora in montadoras:
                        if montadora.getCodigoMontadora() == codigo:
                            encontrou = True
                            print('\n', 5*'=-', 'Dados da montadora selecionada:', 5*'=-')
                            print(f'Código da montadora: {montadora.getCodigoMontadora()}')
                            print(f'Estado da montadora: {montadora.getEstado()}')
                            print(f'Razão Social da montadora: {montadora.getRazao()}')
                            print(27*'=-')
                    if not encontrou:
                        print('Montadora não encontrada')   
                else:
                    print('Opção inválida')
                    
                    
            elif opcao1 == 2: #consulta modelo
                cont = 0
                print('\nNomes dos modelos cadastrados no sistema:')
                for modelo in modelos:
                    cont = cont + 1
                    print(f'{cont} - {modelo.getNome()}')
                print()
                
                opcaomodelo = int(input('Insira o nome do modelo desejado: ')) -1
                if opcaomodelo >= 0 and opcaomodelo < len(modelos):
                    nomeModelo = modelos[opcaomodelo].getNome()
                    
                    encontrou = False
                    for modelo in modelos:
                        if modelo.getNome() == nomeModelo:
                            encontrou = True
                            print('\n', 5*'=-', 'Dados do modelo selecionado:', 5*'=-')
                            print(f'Código do modelo: {modelo.getCodigoModelo()}')
                            print(f'Nome do modelo: {modelo.getNome()}')
                            print(10*'-'+'>')
                            print(f'Código da montadora: {modelo.montadora.getCodigoMontadora()}')
                            print(f'Estado da montadora: {modelo.montadora.getEstado()}')
                            print(f'Razão Social da montadora: {modelo.montadora.getRazao()}')
                            print(25*'=-')
                    if not encontrou:
                        print('Modelo não encontrado')
                else:
                    print('Opção inválida')
                    
            
            elif opcao1 == 3: #consulta carro
                cont = 0
                print('\nPlacas de carros cadastrados no sistema:')
                for carro in carros:
                    cont = cont + 1
                    print(f'{cont} - {carro.getPlaca()}')
                print()
                
                opcaocarro = int(input('Insira a placa do carro desejado: ')) -1
                if opcaocarro >= 0 and opcaocarro < len(carros):
                    carro1 = carros[opcaocarro].getPlaca()
                    
                    encontrou = False
                    for carro in carros:
                        if carro.getPlaca() == carro1:
                            encontrou = True
                            print('\n', 5*'=-', 'Dados do carro selecionado:', 5*'=-')
                            print(f'Placa: {carro.getPlaca()}')
                            print(f'Ano de fabricação: {carro.getFabricacao()}')
                            print(10*'-'+'>')
                            print(f'Nome do modelo: {carro.modelo.getNome()}')
                            print(f'Código do modelo: {carro.modelo.getCodigoModelo()}')
                            print(10*'-'+'>')
                            print(f'Código da montadora: {carro.modelo.montadora.getCodigoMontadora()}')
                            print(f'Estado da montadora: {carro.modelo.montadora.getEstado()}')
                            print(f'Razão Social da montadora: {carro.modelo.montadora.getRazao()}')
                            print(27*'=-')
                    if not encontrou:
                        print('Carro não encontrado')
                else:
                    print('Opção inválida')
                    
                    
            elif opcao1 == 4: #FIM laço consulta dados
                break
    
    
    elif opcao == 5: #INICIO laço alterar dados
        while True:
            print('\nQual dado você quer alterar?')
            print('1 - Montadora')
            print('2 - Modelo')
            print('3 - Carro')
            print('4 - Voltar')
            opcao2 = int(input('Digite a opção: '))
        
            if opcao2 == 1: #alterar montadora
                cont = 0
                print('\nCódigos das montadoras cadastradas no sistema:')
                for montadora in montadoras:
                    cont = cont + 1
                    print(f'{cont} - {montadora.getCodigoMontadora()}')
                print()
            
                opcaocodigo = int(input('Insira a montadora desejada: ')) -1
                if opcaocodigo >= 0 and opcaocodigo < len(montadoras):
                    codigo = montadoras[opcaocodigo].getCodigoMontadora()

                    encontrou = False
                    for montadora in montadoras:
                        teste = len(montadoras)
                        if montadora.getCodigoMontadora() == codigo:
                            encontrou = True
                            codigoMontadora1 = int(input('\nInsira o código da montadora: '))
                            estado1 = input('Insira o estado da montadora (XX): ')
                            razaoSocial1 = input('Insira a razão social da montadora: ')
                            montadoras[opcaocodigo].setCodigoMontadora(codigoMontadora1)
                            montadoras[opcaocodigo].setEstado(estado1)
                            montadoras[opcaocodigo].setRazao(razaoSocial1)
                            print('Montadora atualizada com sucesso!')

                    if not encontrou:
                        print('Montadora não encontrada')   
                else:
                    print('Opção inválida')
                
                
            elif opcao2 == 2: #alterar modelo
                cont = 0
                print('\nNomes dos modelos cadastrados no sistema:')
                for modelo in modelos:
                    cont = cont + 1
                    print(f'{cont} - {modelo.getNome()}')
                print()
                
                opcaomodelo = int(input('Insira o nome do modelo desejado: ')) -1
                if opcaomodelo >= 0 and opcaomodelo < len(modelos):
                    nomeModelo = modelos[opcaomodelo].getNome()
                    
                    encontrou = False
                    for modelo in modelos:
                        if modelo.getNome() == nomeModelo:
                            encontrou = True
                            codigoModelo1 = int(input('\nInsira o código do modelo: '))
                            nome1 = input('Insira o nome do modelo: ')
                            print('\nMontadoras cadastradas:')
        
                            cont = 0
                            for montadora in montadoras:
                                cont = cont + 1
                                print(f'{cont} - {montadora.getCodigoMontadora()}')
            
                            opcaoMontadora = int(input(f'Insira qual montadora você quer selecionar para o modelo "{nome1}": ')) -1
                            if opcaoMontadora >= 0 and opcaoMontadora < len(montadoras):
                                modeloMontadora1 = montadoras[opcaoMontadora]
                                modelos[opcaomodelo].setCodigoModelo(codigoModelo1)
                                modelos[opcaomodelo].setNome(nome1)
                                modelos[opcaomodelo].setMontadora(modeloMontadora1)
                                print('Modelo atualizado com sucesso!')
                            else:
                                print('Montadora inválida')
                    if not encontrou:
                        print('Modelo não encontrado')
                else:
                    print('Opção inválida')
                
                
            elif opcao2 == 3: #alterar carro
                cont = 0
                print('\nPlacas de carros cadastrados no sistema:')
                for carro in carros:
                    cont = cont + 1
                    print(f'{cont} - {carro.getPlaca()}')
                print()
                
                opcaocarro = int(input('Insira a placa do carro desejado: ')) -1
                if opcaocarro >= 0 and opcaocarro < len(carros):
                    carro1 = carros[opcaocarro].getPlaca()
                    
                    encontrou = False
                    for carro in carros:
                        if carro.getPlaca() == carro1:
                            encontrou = True
                            placa1 = input('\nInsira a placa do carro: ')
                            fabricacao1 = int(input('Insira o ano de fabricação do carro (xxxx): '))
                            print('Modelos cadastrados:')
        
                            cont = 0
                            for modelo in modelos:
                                cont = cont + 1
                                print(f'{cont} - {modelo.getNome()}')
            
                            opcaoModelo = int(input(f'Insira qual modelo você quer selecionar para o carro com a placa "{placa1}": ')) -1
                            if opcaoModelo >= 0 and opcaoModelo < len(modelos):
                                carroModelo1 = modelos[opcaoModelo]
                                carros[opcaocarro].setPlaca(placa1)
                                carros[opcaocarro].setFabricacao(fabricacao1)
                                carros[opcaocarro].setModelo(carroModelo1)
                                print('Carro cadastrado com sucesso!')
                            else:
                                print('Modelo inválido')
                    if not encontrou:
                        print('Carro não encontrado')
                else:
                    print('Opção inválida')
                    
                    
            elif opcao2 == 4: #FIM laço alterar dados
                break                
                
                
    elif opcao == 6: #encerrar programa
        print('Encerrando o programa')
        break