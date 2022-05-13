#13 - Agora, faça uma função de acordo com a média informe o status do aluno de acordo com a tabela a seguir:
#Nota acima de 6 à “Aprovado”;
#Nota entre 4 e 6 à Conceito “Verificação Suplementar”;
#Nota abaixo de 4 à Conceito “Reprovado.

def media(n1,n2,n3):
    media = (n1 + n2 + n3)/3
    return media

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = media(n1,n2,n3)
if(media>=6 ):
    print("Aprovado")
elif(media<6 and media >=4):
    print("Verificação Suplementar")
elif(media<4):
    print("Reprovado")

