""" 16. Crie um programa que cadastre informações de uma pessoa (nome, idade e cpf) e
depois coloque em um dicionário. Depois o usuário poderá escolher alguma das
informações para acessa-la. """

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cpf = int(input("Digite seu cpf: "))
info = 0

pessoa = {"nome" : nome,"idade" : idade,"cpf" : cpf}

while(info!=4):
    print("Qual informação você gostaria de acessar(digite o numero correspondente)")
    info = int(input("<1> nome  <2> idade  <3> cpf  <4> cancelar\n"))
    if(info==1):
        print("\nO nome é:",pessoa['nome'])
    elif(info==2):
        print("\nA idade é:",pessoa["idade"])
    elif(info==3):
        print("\nO cpf é:",pessoa["cpf"])
    print("="*60,"\n")
