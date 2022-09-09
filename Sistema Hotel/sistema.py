def cadastro(nome, cpf, nPessoas, tipoQuarto, valor, nDias, status):
    arquivo = open("./BancodeDados/reservaCliente.txt", "a")
    arquivo.write(f"{nome},{cpf},{nPessoas},{tipoQuarto},{valor},{nDias},{status},\n")
    arquivo.close

def busca():
    arquivo = open("./BancodeDados/reservaCliente.txt", "r")
    listaClientes = arquivo.readlines()
    arquivo.close

    novaLista = []
    for i in listaClientes:
        nome,cpf,nPessoas,tipoQuarto,valor,nDias,status,nothing = i.split(",")
        clientes = {"nome" : nome, "cpf" : cpf, "nPessoas" : nPessoas, "tipoQuarto" : tipoQuarto, "valor" : valor, "nDias" : nDias, "status" : status}
        novaLista.append(clientes)
    return novaLista
        
        
def altera(novaLista):
    arquivo = open("./BancodeDados/reservaCliente.txt", "w")
    for i in novaLista:
        arquivo.write(f"{i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['valor']},{i['nDias']},{i['status']},\n")
    arquivo.close