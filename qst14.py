#14. Dadas duas listas L1 e L2, com n valores inteiros, respectivamente, escreva um
# programa que concatene as listas L1 e L2 em uma nova lista L3. Em seguida, imprima
# a lista L3 ordenada de maneira crescente e decrescente.

l1 = [1,2,4,8,12]
l2 = [3,5,87,100,0]
l3 = []
l3 = [*l1, *l2]

print(sorted(l3))
print(sorted(l3, reverse=True))
