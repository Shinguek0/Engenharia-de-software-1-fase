from abc import ABC

class Cadastro(ABC):
    nome = ""

class Usuario(Cadastro):
    def __init__(self, nome, usuario, senha, cpf, numero, idade):
        self.nome = nome
        self.usuario = usuario
        self.__senha = senha
        self.cpf = cpf
        self.numero = numero
        self.idade = idade

    @property
    def senha(self): 
        return self.__senha

    @senha.setter
    def senha(self, novo_senha): 
        raise ValueError("Impossivel alterar senha diretamente")
    
    def cadastroUsuario(self):
        #abre / cria um txt (metodo a de append)
        arquivo = open("./BancodeDados/usuarios.txt", "a")
        #escreve no txt
        arquivo.write(f"{self.nome},{self.usuario},{self.senha},{self.cpf},{self.numero},{self.idade}\n")
        #fecha o arquivo
        arquivo.close

class Cliente(Cadastro):
    def __init__(self, nome, idade, cpf, email, rg, cep, endereco, ddd, tel1, tel2):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.rg = rg
        self.cep = cep
        self.endereco = endereco
        self.ddd = ddd
        self.tel1 = tel1
        self.tel2 = tel2

    def idCliente(self):
        arquivo = open("./BancodeDados/clientes.txt", "r")
        listaClientes = arquivo.readlines()
        arquivo.close

        for i in listaClientes:
            id, nome, idade, cpf, email, rg, cep, endereco, ddd, tel1, tel2 = i.split(",")
            idCliente = int(id)+1
        return idCliente

    def cadastroCliente(self):
        id = self.idCliente()
        arquivo = open("./BancodeDados/clientes.txt", "a")
        #escreve no txt
        arquivo.write(f"{id},{self.nome},{self.idade},{self.cpf},{self.email},{self.rg},{self.cep},{self.endereco},{self.ddd},{self.tel1},{self.tel2}\n")
        #fecha o arquivo
        arquivo.close

class Produto(Cadastro):
    def __init__(self, nome, codigo, data, tipo, qtd, bula, fabricante):
        self.nome = nome
        self.codigo = codigo
        self.data = data
        self.tipo = tipo
        self.qtd = qtd
        self.bula = bula
        self.fabricante = fabricante

    def cadastroProduto(self):
        arquivo = open("./BancodeDados/produtos.txt", "a")
        arquivo.write(f"{self.nome},{self.codigo},{self.data},{self.tipo},{self.qtd},{self.bula},{self.fabricante}\n")
        arquivo.close

def lerProdutos(cod):
    arquivo = open("./BancodeDados/produtos.txt", "r")
    listaProdutos = arquivo.readlines()
    arquivo.close

    arquivo = open("./BancodeDados/produtosExcluidos.txt", "r")
    listaProdutosE = arquivo.readlines()
    arquivo.close
    estoque = 0
    np,cp,dp,tp,qp,bp,fp = "semnada"
    for i in listaProdutos:
        for j in listaProdutosE:
            nomeE, codigoE, dataE, tipoE, qtdE, bulaE, fabricanteE = j.split(",")
            nome, codigo, data, tipo, qtd, bula, fabricante = i.split(",")
            if(estoque==0):
                estoque = qtd
            if(codigoE == codigo):
                estoque = int(estoque) - int(qtdE)
            if(cod == codigo):
                np,cp,dp,tp,qp,bp,fp = nome,codigo,data,tipo,qtd,bula,fabricante
        print(f"Nome do remedio: {nome}\n codigo: {codigo}\n data: {data}\n tipo: {tipo}\n estoque: {estoque}\n bula: {bula}\n fabricante: {fabricante}\n")
        print("-"*10)
        estoque = 0
    return np,cp,dp,tp,qp,bp,fp

def execluirProduto(nome, codigo, data, tipo, qtd, bula, fabricante):
    arquivo = open("./BancodeDados/produtosExcluidos.txt", "a")
    arquivo.write(f"{nome},{codigo},{data},{tipo},{qtd},{bula},{fabricante}\n")
    arquivo.close


def login(usuarioL, senhaL):
    arquivo = open("./BancodeDados/usuarios.txt", "r")
    listaUsuario = arquivo.readlines()
    arquivo.close
    login = False
    for i in listaUsuario:
        nome, user, password, cpf, numero, idade = i.split(",")
        if (usuarioL == user) and (senhaL == password):
            login = True
    return login



""" def procurar(cod):
    arquivo = open("./BancodeDados/produtos.txt", "r")
    listaProdutos = arquivo.readlines()
    arquivo.close
    np,cp,dp,tp,qp,bp,fp = "semnada"
    for i in listaProdutos:
        nome, codigo, data, tipo, qtd, bula, fabricante = i.split(",")
        if(cod == codigo):
            np,cp,dp,tp,qp,bp,fp = nome,codigo,data,tipo,qtd,bula,fabricante
    
    return np,cp,dp,tp,qp,bp,fp """

#cadastroUsuario("Ricardo","B","B",1,123,12)

""" if(login("A","a")):
    print("Logado com sucesso")
else:
    print("Erro, usuario ou senha errados!!") """

#cadastroCliente("Cliente teste",0,0,"cliente@email.com",0,0,"Terra",00,0,0)

#cadastroProduto("Remedio",1,"20/10/2022","Anestesico",1,"Bula","nenhum")

#lerProdutos('não')
#print(lerProdutos("não"))

#execluirProduto("Remedio",1,"20/10/2022","Anestesico",2,"Bula","nenhum")

#print(procurar(0))