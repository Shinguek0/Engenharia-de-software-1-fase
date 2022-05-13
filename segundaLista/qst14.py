#14 - Escreva uma função para imprimir o nome e salário de um funcionário usando as seguintes condições.
#Deve aceitar o nome e o salário do funcionário.
#Se o salário estiver faltando na chamada de função, atribua o valor padrão 9000 ao salário.

def empregado(nome, salario = 9000):
    print("Nome:",nome)
    print("Salario:",salario)


#acho que essa parte nao precisava mas :/
nome = input("Digite o nome do funcionário: ")
salario = input("Digite o salario do funcionário: ")
if(salario == ""):
    empregado(nome)
else:
    empregado(nome, salario)