class Editora:
    def __init__(self, codigo, razao, nome, telefone):
        self.codigo = codigo
        self.razao = razao
        self.nome = nome
        self.telefone = telefone
        
    def setCodigoEditora(self, codigo):
        self.codigo = codigo
    def setRazaoSocial(self, razao):
        self.razao = razao
    def setNomeContato(self, nome):
        self.nome = nome
    def setTelefone(self, telefone):
        self.telefone = telefone
        
    def getCodigoEditora(self):
        return self.codigo
    def getRazaoSocial(self):
        return self.razao
    def getNomeContato(self):
        return self.nome
    def getTelefone(self):
        return self.telefone
    
class Livro:
    def __init__(self, codigo, titulo, isbn, Editora):
        self.codigo = codigo
        self.titulo = titulo
        self.isbn = isbn
        self.editora = Editora
        
    def setCodigoLivro(self, codigo):
        self.codigo = codigo
    def setTituloLivro(self, titulo):
        self.titulo = titulo
    def setISBN(self, isbn):
        self.isbn = isbn
    def setEditora(self, Editora):
        self.editora = Editora
        
    def getCodigoLivro(self):
        return self.codigo
    def getTituloLivro(self):
        return self.titulo
    def getISBN(self):
        return self.isbn
    def getEditora(self):
        return self.editora
    
editoras = []
livros = []
    
while True:
    print('\nEscolha uma opção:')
    print('1 - Cadastrar editora:')
    print('2 - Cadastrar livro:')
    print('3 - Pesquisar editora (razão social):')
    print('4 - Pesquisar livro (título):')
    print('5 - Sair')
    opcao = int(input('Digite a opção: '))
    
    if opcao == 1:
        codigoEditora = int(input('\nInsira o código da editora: '))
        razaoSocial = input('Insira a razão social da editora: ')
        nomeContato = input('Insira o nome do contato da editora: ')
        telefone = input('Insira o telefone para contato: ')
        editora = Editora(codigoEditora, razaoSocial, nomeContato, telefone)
        editoras.append(editora)
        print('Editora cadastrada com sucesso!')
        
    elif opcao == 2:
        codigoLivro = int(input('\nInsira o código do livro: '))
        tituloLivro = input('Insira o título do livro: ')
        ISBN = input('Insira o código ISBN: ')
        print('\nEditoras cadastradas:')
        
        cont = 0
        for editora in editoras:
            cont = cont + 1
            print(f'{cont} - {editora.getRazaoSocial()}')
            
        opcaoEditora = int(input(f'Insira qual a editora você quer selecionar para o livro "{tituloLivro}": ')) -1
        if opcaoEditora >= 0 and opcaoEditora < len(editoras):
            editoraLivro = editoras[opcaoEditora]
            livro = Livro(codigoLivro, tituloLivro, ISBN, editoraLivro)
            livros.append(livro)
            print('Livro cadastrado com sucesso!')
        else:
            print('Editora inválida')
    
    elif opcao == 3:
        cont = 0
        for editora in editoras:
            cont = cont + 1
            print(f'{cont} - {editora.getRazaoSocial()}')
            
        razao = input('Insira a razão social da editora desejada: ')
        encontrou = False
        for editora in editoras:
            if editora.getRazaoSocial() == razao:
                encontrou = True
                print('\nDados da editora selecionada:')
                print(f'Código: {editora.getCodigoEditora()}')
                print(f'Razão social: {editora.getRazaoSocial()}')
                print(f'Nome do contato: {editora.getNomeContato()}')
                print(f'Telefone: {editora.getTelefone()}')
        if not encontrou:
            print('Editora não econtrada')
                
    elif opcao == 4:
        titulo = input('Insira o título do livro desejado: ')
        encontrou = False
        for livro in livros:
            if livro.getTituloLivro() == titulo:
                encontrou = True
                print('\nDados do livro selecionado:')
                print(f'Código: {livro.getCodigoLivro()}')
                print(f'Título: {livro.getTituloLivro()}')
                print(f'ISBN: {livro.getISBN()}')
                print(f'Editora: {livro.getEditora().getNomeContato()}')
        if not encontrou:
            print('Livro não encontrado')
                
    elif opcao == 5:
        print('Encerrando o programa')
        break