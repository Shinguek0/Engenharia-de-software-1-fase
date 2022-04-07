from pessoa import Empresario,Aluno

jorginho = Aluno("Jorge", 10, "Masculino", 15) #define o objeto de aluno
fernandinho = Empresario("Fernando", 35, "Masculino", 1000) #define o objeto de empresario

jorginho.andar(10,2)       #funçao andar vinda da classe pessoa
fernandinho.andar(10,2)     #funçao andar vinda da classe pessoa

""" fernandinho.salario = 10 """  # da erro pois a variavel esta encapsulada, sendo nessesario usar um metodo para alterar ela


print(f"Salario Atual: {fernandinho.salario}")  #print o salario
fernandinho.reajuteSalario(10) #chama a funçao de aumento
print(f"Salario Ajustado: {fernandinho.salario}") #print o salario

print(f"Tempo livre de Jorge: {jorginho.tempoLivre}") #printa o tempo livre
jorginho.tempoLivreGasto(10) #chama a funçao de alterar tempo livre
print(f"Tempo restante de Jorge: {jorginho.tempoLivre}") #printa o tempo livre