#6 - Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:
#IMC = peso/(altura²)

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso/(altura**2)

if(imc<18.5):
    print("Abaixo do peso")
elif(imc>18.5 and imc<=24.9):
    print("Saudável")
elif(imc>24.9 and imc<=29.9):
    print("Peso em exesso")
elif(imc>29.9 and imc<=34.9):
    print("Obesidade Grau I")
elif(imc>34.9 and imc<=39.9):
    print("Obesidade Grau II")
elif(imc>39.9):
    print("Obesidade Grau III")
else: 
    print("Tem algo de errado com você!!")