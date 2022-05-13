#15 - Escreva uma função Python que receba uma lista e retorne uma nova lista com elementos exclusivos da primeira lista.

def sla(a = []):
    x = a
    return x

from random import randint

lista = []
for i in range(10):
    lista.append(randint(1, 100))

print(lista)
print(sla(lista))