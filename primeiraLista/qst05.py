#Faça um programa que lê um valor em reais e calcule o valor equivalente em dólares.
#O usuário deve informar, além do valor em reais da compra, o valor da cotação do
#dólar.

reais = float(input("Digite um valor em reais: "))
cotacao = float(input("Digite a cotação do dólar: "))

print("O valor em dólares é:",reais*cotacao)