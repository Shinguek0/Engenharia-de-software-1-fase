#8 - Faça um programa que receba dois números. Calcule e mostre:
#• A soma dos números pares desse intervalo de números, incluindo os números digitados;
#• A multiplicação dos números ímpares desse intervalo, incluindo os digitados;

from math import prod

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
par = []
impar = []

for i in range(n1,n2+1):
    if(i % 2 == 0):
        par.append(i)
    else:
        impar.append(i)

print("• A soma dos números pares desse intervalo de números:",sum(par))
print("• A multiplicação dos números ímpares desse intervalo:",prod(impar))
