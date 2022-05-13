#12 - Fazer uma função que receba três notas de um aluno, e que retorne a média dessas 3 notas.

def media(n1,n2,n3):
    media = (n1 + n2 + n3)/3
    return media

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
print(media(n1,n2,n3))