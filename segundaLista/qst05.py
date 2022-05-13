#5 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva
#uma mensagem de erro se a opção for invalidar.
def Num():
    num.append(float(input("Digite o primeiro numero: ")))
    num.append(float(input("Digite o segundo numero: ")))


print("Escolha uma opção:\n1 - Soma de dois numeros\n2 - Diferença entre dois numeros\n3 - Produto de dois numeros\n4 - Divisão entre dois numeros")
n = int(input("Opção: "))
num = []

if(n == 1):
    Num()
    print(num[0],"+",num[1],"=",sum(num))
elif(n == 2):
    Num()
    print(max(num),"-",min(num),"=",max(num)-min(num))
elif(n == 3):
    Num()
    print(num[0],"x",num[1],"=",max(num)*min(num))
elif(n == 4):
    Num()
    if(num[1]==0):
        print("O divisor nao pode ser 0!!!")
    else:
        print(num[0],"/",num[1],"=",num[0]/num[1])
else:
    print("Opção invalida!")