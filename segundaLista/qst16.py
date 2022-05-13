#16 - Escreva um programa Python para imprimir os números pares de uma determinada lista.

from random import randint

lista = []
for i in range(10):
    lista.append(randint(1, 100))

print(lista)

for i in lista:
    if(i % 2 == 0):
        print(i)