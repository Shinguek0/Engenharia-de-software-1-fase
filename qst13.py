
#13. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
# informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a
# ordem lida.

idade = []
altura = []

for i in range(0,5):
    idade.append(int(input("Digite sua idade: ")))
    altura.append(int(input("Digite sua altura: ")))

#print("Idades:",sorted(idade, reverse=True))   #ordem decrescente
#print("Alturas:",sorted(altura, reverse=True)) #ordem decrescente

idade.reverse()
altura.reverse()
print("idades:",idade)
print("Alturas:",altura)