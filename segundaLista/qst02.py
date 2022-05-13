#2 - Escreva um programa que, dados dois números inteiros fornecidos pelo usuário, mostre na tela o
#maior deles, assim como a diferença existente entre ambos.

n = [int(input("Digite um numero: ")), int(input("Digite outro numero: "))]
print(f"O maior numero é: {max(n)}\nA diferença entre ambos é: {max(n)-min(n)}")