#17 - Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A
#função deve imprimir todos os elementos da lista numerando-os.
from random import randint

def impLista(a = []):
    for i in range(len(a)):
        print(i+1,"-",a[i])

lista = []
for i in range(10):
    lista.append(randint(1, 100))

impLista(lista)