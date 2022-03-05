""" 15. Crie um Python Script que conte quantas vezes um nome está presente em uma lista
[’nome1’, ’nome2’, ...] e armazena essa contagem em um dicionário {’nome’: xvezes}. """

nomes = []
dicio = {}

print("Digite 6 nomes: ")
for i in range(0,6):
    nomes.append(input(""))
    if(nomes.count(nomes[i])<=1):
      dicio[nomes[i]] = 1
    else:
      dicio[nomes[i]] += 1

for chave in dicio.keys():
  print(f'nome: {chave} vezes que ele aparece: {dicio[chave]}')