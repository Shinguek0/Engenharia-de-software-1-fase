#1 - Leia um número real fornecido pelo usuário. Se o número for positivo imprima a raiz quadrada. Do
#contrário, imprima o número ao quadrado.
from math import sqrt

n = float(input("Digite um numero real: "))
if(n>=0):
    print("A raiz do numero é:",sqrt(n))
else:
    print("O numero ao quadrado é:",n**2)