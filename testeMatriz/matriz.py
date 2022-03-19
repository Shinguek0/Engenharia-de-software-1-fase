def bas():
    l1 = A[0][:]
    l2 = A[1][:]
    l3 = A[2][:]
    l4 = A[3][:]
    return l1,l2,l3,l4

#def to show the matrix on the screen
def printMatriz():
    print("-"*60)
    l1,l2,l3,l4 = bas() 
    print(f"\n\n{l1}\n{l2}\n{l3}\n{l4}")

def opr(choice, line):
    l1,l2,l3,l4 = bas()
    if(choice == 1):
        num = float(input("\nDigite por que numero você quer multiplicar essa linha: "))
        for i in range (0,4):
            A[line][i] *= num
    if(choice == 2):
        num = float(input("\nDigite por que numero você quer dividir essa linha: "))
        for i in range (0,4):
            A[line][i] /= num
    if(choice==3):
        lineChange = int(input("Por qual linha você quer trocar: \n")) - 1
        placeHolder = A[line][:]
        secondHolder = A[lineChange][:]
        for i in range (0,4):
            A[line][i] = secondHolder[i]
        for i in range (0,4):
            A[lineChange][i] = placeHolder[i]
    if(choice==4):
        pass

A = []  # Set 'A' as a list
choice = 0
#turn list 'A' to matrix 
for i in range(4):
    A.append( [0] * 4 )

# exemple how set matrix values
""" A[0][0] = 1
A[0][1] = 0
A[0][2] = 0
A[0][3] = 0

A[1][0] = 2
A[1][1] = 1
A[1][2] = 0
A[1][3] = 0

A[2][0] = 3
A[2][1] = 2
A[2][2] = 1
A[2][3] = 0

A[3][0] = 4
A[3][1] = 3
A[3][2] = 2
A[3][3] = 1 """

#for to alter all the matrix values
for j in range (0,4):
    for i in range (0,4):
        printMatriz()
        A[j][i] = int(input(""))

while choice!=5:
    l1,l2,l3,l4 = bas()
    line = int(input(f"\nDigite a linha que você deseja alterar:\n<1> - {l1}\n<2> - {l2}\n<3> - {l3}\n<4> - {l4}\n"))-1
    choice = int(input("Digite que operação você deseja fazer:\n<1> multiplicação <2> divisão <3> trocar com outra linha <4> fazer operação com outra linha\n"))
    opr(choice,line)

printMatriz()
