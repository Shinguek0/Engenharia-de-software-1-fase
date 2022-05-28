def salvarString():
    #Abre/cria um arquivo txt
    arquivo = open("./arquivosSalvos/usuario.txt", "a")

    texto = "pog"
    #escreve no txt
    arquivo.write(texto)
    #fecha o arquivo para nao fuder com tudo
    arquivo.close

def salvarIteraveis():
    arquivoComLista = open("./arquivosSalvos/listas.txt", "a")
    usuarios = ["jorge,12,10/10/2003","joao,13,10/10/0202","Roberta,15,12/12/1202"]
    #usa writeline para escrever uma lista
    arquivoComLista.writelines(usuarios)
    arquivoComLista.close()

def lerArquivo():
    arquivo = open("./arquivosSalvos/listas.txt", "r")   
    print(arquivo.readlines())
    arquivo.close()

def lerComSplit():
    arquivo = open("./arquivosSalvos/listas.txt", "r")
    listaUsuario = arquivo.readlines()
    arquivo.close

    for i in listaUsuario:
        nome, idade, dataCadastro = i.split(",")
        print(f"Usuario: {nome}\nIdade: {idade}\nData do cadastro: {dataCadastro}\n")

def criarSemSplit():
    arquivoComLista = open("./arquivosSalvos/listasSemSplit.txt", "a")
    usuarios = ["jorge \n", "15 \n", "12/10/2003 \n"]
    for i in range(2):
        usuarios.append(input("Nome: ")+"\n")
        usuarios.append(input("Idade: ")+"\n")
        usuarios.append(input("Data Cadastro: ")+"\n")
    #usa writeline para escrever uma lista
    arquivoComLista.writelines(usuarios)
    arquivoComLista.close()

def lerSemSplit():
    #ler arquivos
    arquivo = open("./arquivosSalvos/listasSemSplit.txt", "r")
    listaUsuario = arquivo.readlines()
    arquivo.close()
    g = 0
    for i in range(3):
        print(f"Usuario: {listaUsuario[0+g]}\nIdade: {listaUsuario[1+g]}\nData do cadastro: {listaUsuario[2+g]}\n")
        g+=3

criarSemSplit()
lerSemSplit()