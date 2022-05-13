#11 - Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado
#pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, os valoresinicial
#e final devem ser informados também pelo usuário, conforme exemplo abaixo:

num = int(input("Mostrar a tabuada de: "))
ini = int(input("Começar por: "))
fin = int(input("Terminar em: "))

for i in range(ini,fin+1):
    print(num,"x",i,"=",num*i)