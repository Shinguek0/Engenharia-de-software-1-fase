#9 - Faca um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
#• adição (opção 1)
#• subtração (opção 2)
#• multiplicação (opção 3)
#• divisão (opção 4)
#• saída (opção 5)
def Num():
    num.append(float(input("Digite o primeiro numero: ")))
    num.append(float(input("Digite o segundo numero: ")))
    print("\n\n\n")

jorge = True
num = []

while(jorge):
    print("-"*40)
    print("\n\n")
    print("Escolha a opção:\n1 - adição\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair")
    escolha = int(input("Opção: "))
    print("-"*40)

    if(escolha == 1):
        Num()
        print(num[0],"+",num[1],"=",sum(num))
    elif(escolha == 2):
        Num()
        print(max(num),"-",min(num),"=",max(num)-min(num))
    elif(escolha == 3):
        Num()
        print(num[0],"x",num[1],"=",max(num)*min(num))
    elif(escolha == 4):
        Num()
        if(num[1]==0):
            print("O divisor nao pode ser 0!!!")
        else:
            print(num[0],"/",num[1],"=",num[0]/num[1])
    elif(escolha == 5):
        jorge = False
    else:
        print("Opção invalida!")
