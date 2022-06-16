def cadastroUsuario(nome, usuario, senha, cpf, numero, idade):
    #abre / cria um txt (metodo a de append)
    arquivo = open("./BancodeDados/usuarios.txt", "a")
    #escreve no txt
    arquivo.write(f"{nome},{usuario},{senha},{cpf},{numero},{idade}\n")
    #fecha o arquivo
    arquivo.close

def login(usuario, senha):
    arquivo = open("./BancodeDados/usuarios.txt", "r")
    listaUsuario = arquivo.readlines()
    arquivo.close
    login = False

    for i in listaUsuario:
        nome, user, password, cpf, numero, idade = i.split(",")
        if (usuario == user) and (senha == password):
            login = True
    return login

def idCliente():
    arquivo = open("./BancodeDados/clientes.txt", "r")
    listaClientes = arquivo.readlines()
    arquivo.close

    for i in listaClientes:
        id, nome, idade, cpf, email, rg, cep, endereco, ddd, tel1, tel2 = i.split(",")
        idCliente = int(id)+1
    return idCliente

def cadastroCliente(nome, idade, cpf, email, rg, cep, endereco, ddd, tel1, tel2):
    id = idCliente()
    arquivo = open("./BancodeDados/clientes.txt", "a")
    #escreve no txt
    arquivo.write(f"{id},{nome},{idade},{cpf},{email},{rg},{cep},{endereco},{ddd},{tel1},{tel2}\n")
    #fecha o arquivo
    arquivo.close

def cadastroProduto(nome, codigo, data, tipo, qtd, bula, fabricante):
    arquivo = open("./BancodeDados/produtos.txt", "a")
    arquivo.write(f"{nome},{codigo},{data},{tipo},{qtd},{bula},{fabricante}\n")
    arquivo.close

def lerProdutos():
    arquivo = open("./BancodeDados/produtos.txt", "r")
    listaProdutos = arquivo.readlines()
    arquivo.close

    arquivo = open("./BancodeDados/produtosExcluidos.txt", "r")
    listaProdutosE = arquivo.readlines()
    arquivo.close
    estoque = 0
    print(listaProdutos)
    for i in listaProdutos:
        for j in listaProdutosE:
            nomeE, codigoE, dataE, tipoE, qtdE, bulaE, fabricanteE = j.split(",")
            nome, codigo, data, tipo, qtd, bula, fabricante = i.split(",")
            if(estoque==0):
                estoque = int(qtd)
            if(codigoE == codigo):
                estoque -= int(qtdE)
        print(nome, codigo, data, tipo, estoque, bula, fabricante)

def execluirProduto(nome, codigo, data, tipo, qtd, bula, fabricante):
    arquivo = open("./BancodeDados/produtosExcluidos.txt", "a")
    arquivo.write(f"{nome},{codigo},{data},{tipo},{qtd},{bula},{fabricante}\n")
    arquivo.close
        

#cadastroUsuario("Ricardo","B","B",1,123,12)

""" if(login("A","a")):
    print("Logado com sucesso")
else:
    print("Erro, usuario ou senha errados!!") """

#cadastroCliente("Cliente teste",0,0,"cliente@email.com",0,0,"Terra",00,0,0)

#cadastroProduto("Remedio",1,"20/10/2022","Anestesico",1,"Bula","nenhum")

lerProdutos()

#execluirProduto("Remedio",1,"20/10/2022","Anestesico",2,"Bula","nenhum")