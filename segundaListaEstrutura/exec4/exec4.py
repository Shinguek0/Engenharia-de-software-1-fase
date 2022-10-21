#Faça uma análise comparativa entre os algoritmos de ordenação Bubble Sort, Quick Sort e Merge Sort. Para testar se efetivamente teremos resultados mais rápidos, siga 
# o seguinte roteiro:
# ● Crie um vetor com 5000 números (do tipo float) aleatórios entre 0 e 1 (utilize a biblioteca random)
# ● Use o comando %timeit para medir o desempenho e compare o tempo de execução de cada algoritmo;
# ● Lembre de utilizar o mesmo vetor em todos os experimentos!
# ● Qual algoritmo foi mais rápido? Demonstre os tempos.

import random
import timeit, functools
import time

# BubbleSort
def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return lista


# Quick Sort 

def quickSortMetodo(array, low, high):
    quickSort(array, low, high)

def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


# Merge Sort
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


tamVetor = 5000
vetorTeste = []
for _ in range(tamVetor):
    vetorTeste.append(random.random())

listaTempos = []

execBubbleSort = timeit.Timer(functools.partial(bubbleSort, vetorTeste)) 
execMergeSort = timeit.Timer(functools.partial(mergeSort, vetorTeste)) 


inicio = time.time()
quickSort(vetorTeste, 0, len(vetorTeste)  - 1)
fim = time.time()
tempoQuickSort = (fim - inicio)

tempoBubbleSort = execBubbleSort.timeit(1)
tempoMergeSort = execMergeSort.timeit(1)

listaTempos.append(tempoBubbleSort)
listaTempos.append(tempoQuickSort)
listaTempos.append(tempoMergeSort)

print(f'Tempo bubble sort: {tempoBubbleSort}')
print(f'Tempo quick sort: {tempoQuickSort}')
print(f'Tempo merge sort: {tempoMergeSort}')

menorTempo  = min(listaTempos)
maisRapido = ""
if menorTempo == tempoBubbleSort:
    maisRapido = "Bubble Sort"
elif menorTempo == tempoQuickSort: 
    maisRapido = "Quick Sort"
else:
    maisRapido = "Merge Sort"


print('-' * 20)
print(f'Menor tempo: {menorTempo}')
print(f'Mais rápido: {maisRapido}')




