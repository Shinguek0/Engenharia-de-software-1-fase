#12. Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.

n = []

for i in range(0,4):
    n.append(float(input("Digite uma nota: ")))

print(f"nota 1 = {n[0]}\nnota 2 = {n[1]}\nnota 3 = {n[2]}\nnota 4 = {n[3]}\nmedia final: {sum(n)/4}")