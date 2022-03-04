#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
n = []

for i in range(1, 5):
    n.append(float(input(f"Digite a {i}ª nota: ")))


print(f"Primeira nota: {n[0]}\nSegunda nota: {n[1]}\nTerceira nota: {n[2]}\nQuarta nota: {n[3]}\nmedia: {sum(n)/4}")
