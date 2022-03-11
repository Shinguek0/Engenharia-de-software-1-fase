#11. Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

n = []

for i in range(0, 5):
    n.append(int(input("Digite um numero: ")))

for i in range(len(n)):
    print(f"numero: {n[i]} na posiçao {i}")