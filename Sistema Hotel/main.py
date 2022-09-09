import re
from time import sleep
import os
from sistema import cadastro, busca, altera

def clear():
    sleep(2)
    os.system("cls")

def cadReserva():
    nome = input("Nome: ")
    cpf = input("Cpf: ")
    nPessoas = int(input("Numero de pessoas: "))
    nDias = int(input("Numero de dias: "))
    tipoQuarto = input("Tipo de quarto (<S>Standar <D>Delux <P>Premium): ").upper()
    status = "R"
    clear()
    if(tipoQuarto == "S"): valor = (100*nPessoas)*nDias
    elif(tipoQuarto == "D"): valor = (100*nPessoas)*nDias
    elif(tipoQuarto == "P"): valor = (100*nPessoas)*nDias
    else: 
        print("Tipo de Quarto invalido!!")
        cadReserva()
    if(nome == "" or cpf == "" or nPessoas == "" or nDias == ""):
        print("Todas as informações precisam ser preenchidas de forma correta!!")
        cadReserva()
    cadastro(nome,cpf,nPessoas,tipoQuarto,valor,nDias,status)
    print(f"Cadastro Realizado de {nome} no valor de {valor}!!\n")

def entradaCliente():
    cpf = input("Procurar por cpf: ")
    clear()
    novaLista = busca()
    reservaEsc = 0
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['valor']},{i['nDias']},{i['status']},\n")
    reservaEsc = int(input("> "))
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            if(reserva == reservaEsc):
                i['status'] = "A"
    altera(novaLista)
    clear()
    print("Check in realizado com sucesso!!")


def saidaCliente():
    cpf = input("Procurar por cpf: ")
    clear()
    novaLista = busca()
    reservaEsc = 0
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['valor']},{i['nDias']},{i['status']},\n")
    reservaEsc = int(input("> "))
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            if(reserva == reservaEsc):
                i['status'] = "F"
    altera(novaLista)
    clear()
    print("Check out realizado com sucesso!!")

def alterarReserva():
    cpf = input("Procurar por cpf: ")
    clear()
    novaLista = busca()
    reservaEsc = 0
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['valor']},{i['nDias']},{i['status']},\n")
    reservaEsc = int(input("> "))
    reserva = 0
    for i in novaLista:
        if(cpf == i['cpf']):
            reserva+=1
            if(reserva == reservaEsc):
                    i['nPessoas'] = int(input("Numero de pessoas: "))
                    i['nDias'] = int(input("Numero de dias: "))
                    i['tipoQuarto'] = input("Tipo de quarto (<S>Standar <D>Delux <P>Premium): ").upper()
                    i['status'] = input("Status do quarto: ").upper()
                    if(i['tipoQuarto'] == "S"): i['valor'] = (100*i['nPessoas'])*i['nDias']
                    elif(i['tipoQuarto'] == "D"): i['valor'] = (100*i['nPessoas'])*i['nDias']
                    elif(i['tipoQuarto'] == "P"): i['valor'] = (100*i['nPessoas'])*i['nDias']
    altera(novaLista)
    clear()
    print("Alteração realizada com sucesso!!")

def relatorio():
    clear()
    novaLista = busca()
    cho = int(input("1 - Relatório de todas as reservas com status R\n2 - Relatório de todas as reservas com status C\n3 - Relatório de todas as reservas com status A\n4 - Relatório de todas as reservas com status F\n5 - Relatório total recebido\n6 – Relatório de Reserva por pessoa\n> "))
    if cho == 1:
        clear()
        reserva = 0
        for i in novaLista:
            if("R" == i['status']):
                reserva+=1
                print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['valor']},{i['nDias']},{i['status']},\n")
    elif cho == 2: 
        clear()
        reserva = 0
        for i in novaLista:
            if("C" == i['status']):
                reserva+=1
                print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['valor']},{i['nDias']},{i['status']},\n")
    elif cho == 3: 
        clear()
        reserva = 0
        for i in novaLista:
            if("A" == i['status']):
                reserva+=1
                print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['valor']},{i['nDias']},{i['status']},\n")
    elif cho == 4: 
        clear()
        reserva = 0
        for i in novaLista:
            if("F" == i['status']):
                reserva+=1
                print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['valor']},{i['nDias']},{i['status']},\n")
    elif cho == 5: 
        clear()
        totalRecebido=0
        for i in novaLista:
            totalRecebido+=int(i["valor"])
        print(f"Total Recebido = {totalRecebido}")
    elif cho == 6: 
        cpf = input("Procurar por cpf: ")
        clear()
        reserva = 0
        for i in novaLista:
            if(cpf == i['cpf']):
                reserva+=1
                print(f"Reserva<{reserva}> - {i['nome']},{i['cpf']},{i['nPessoas']},{i['tipoQuarto']},{i['valor']},{i['nDias']},{i['status']},\n")
        

while True:
    print('-'*40)
    choice = int(input("1 - Cadastrar uma reserva\n2 - Entrada do cliente\n3 - Saída do cliente\n4 - Alterar reserva\n5 - Relatorio\n6 - Sair\n> "))
    if choice == 1: cadReserva()
    elif choice == 2: entradaCliente()
    elif choice == 3: saidaCliente()
    elif choice == 4: alterarReserva()
    elif choice == 5: relatorio()
    elif choice == 6: break