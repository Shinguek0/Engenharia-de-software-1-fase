#Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule e imprima o
#valor de z:
# ## 𝑧 =(𝑥2+𝑦2) 
#         x−y

x = int(input("Digite um valor x: "))
y = int(input("Digite um valor y: "))

if(x-y!=0):
    z = (x**2+y**2)/(x-y)
    print(z)
else:
    print("Os numeros nao podem ser igual!")