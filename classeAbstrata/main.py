from pessoa import Empresario,Aluno

jorginho = Aluno("Jorge", 10, "Masculino", 15) #define o objeto de aluno
fernandinho = Empresario("Fernando", 35, "Masculino", 1000, 200) #define o objeto de empresario

jorginho.andar(10,2)       #funçao andar vinda da classe pessoa
fernandinho.andar(10,2)     #funçao andar vinda da classe pessoa

""" fernandinho.salario = 10 """  # da erro pois a variavel esta encapsulada, sendo nessesario usar um metodo para alterar ela


print(fernandinho.salario)  #print o salario
fernandinho.reajusteSalario(10) #chama a funçao de aumento
print(fernandinho.salario) #print o salario

""" print(fernandinho.tempoTrabalho) """

print(jorginho.tempoLivre) #print o salario
jorginho.tempoLivreGasto(10) #chama a funçao de alterar tempo livre
print(jorginho.tempoLivre) #print o salario