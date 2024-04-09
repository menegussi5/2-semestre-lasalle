class Produto:
    def __init__(self, codigo, descricao, preco, custo):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.custo = custo
        
    def setCodigo(self, codigo):
        self.codigo = codigo
    def setDescricao(self, descricao):
        self.descricao = descricao
    def setPreco(self, preco):
        self.preco = preco
    def setCusto(self, custo):
        self.custo = custo
        
    def getCodigo(self):
        return self.codigo
    def getDescricao(self):
        return self.descricao
    def getPreco(self):
        return self.preco
    def getCusto(self):
        return self.custo
    
    def calculaMargem(self):
        return (self.custo/self.preco)*100

produtos = []

while True:
    print("\nEscolha uma opção:")
    print("1 - Cadastrar o produto")
    print("2 - Calcular a margem")
    print("3 - Sair")
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        codigo = int(input("Insira o código do produto: "))
        descricao = input("Insira a descrição do produto: ")
        preco = float(input("Insira o preço do produto: "))
        custo = float(input("Insira o custo do produto: "))
        produto = Produto(codigo, descricao, preco, custo)
        produtos.append(produto)
        print("Produto cadastrado com sucesso!")
        
    elif opcao == 2:
        print()
        if produtos:
            cont = 0
            for produto in produtos:
                cont = cont + 1
                print(f"Margem de lucro do produto {cont}. {produto.getDescricao()}: {produto.calculaMargem():.2f}%")
        else:
            print("Não há nenhum produto cadastrado!")
            
    elif opcao == 3:
        print("Encerrando o programa")
        break
    
    else:
        print("***OPÇÃO INVÁLIDA***")