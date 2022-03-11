#7. Faça um programa que dada duas strings, s1 e s2 retornam uma nova 
# string composta do primeiro, do meio e do último caracteres de cada string de entrada.

s1 = input("Digite uma frase: ")
s2 = input("Digite outra frase: ")

s3 = (s1[0] + s1[round(len(s1)/2)] + s1[len(s1)-1])
s3 += (s2[0] + s2[round(len(s2)/2)] + s2[len(s2)-1])
print(s3)