#4 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for
#maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo
#concedido.

salario = float(input("Digite o seu salario: "))
pret = float(input("Digite a prestação: "))
if(pret>salario*0.20):
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido")