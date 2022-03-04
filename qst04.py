#4. Faça um programa que lê o nome de um produto, a quantidade comprada, o valor
#unitário e o percentual de desconto a ser aplicado para o pagamento. Imprima na tela
#o nome do produto e o valor total da venda.

nomeProduto = input("Digite o nome do produto: ")
qtd = int(input("Digite a quantidade comprada: "))
valorUnidade = float(input("Digite o valor unitario: "))
desconto = int(input("Digite o valor do desconto: "))

total = (qtd*valorUnidade)
total -= (total/100)*desconto 
print(f"Nome do produto: {nomeProduto}\nquantidade: {qtd} x R${valorUnidade}\ndesconto: {desconto}%\nTotal: {total}\n\n")