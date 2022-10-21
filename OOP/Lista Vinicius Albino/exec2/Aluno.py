#Crie uma classe chamada Aluno() com os seguintes atributos: Nome, Nota 1, Nota 2 Crie os seguintes métodos:
#● Calcula média, retornando a média aritmética entre as notas.
#● Mostra dados, que somente imprime o valor de todos os atributos.
#● Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for
#maior ou igual a 6.0, o aluno está aprovado). Crie dois objetos (aluno1 e aluno2) e teste todos os métodos.
#Dica: no construtor da classe não passe a média como atributo, mas a inicialize com valor igual a zero.

class Aluno():
    def __init__(self, nome, nota1, nota2):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__media = 0
    
    #● Calcula média, retornando a média aritmética entre as notas.
    def media(self):
        self.__media = (self.__nota1 + self.__nota2)/2
        return self.__media

    #● Mostra dados, que somente imprime o valor de todos os atributos.
    def mostrar(self):
        print(f"Nome: {self.__nome}\nPrimeira nota: {self.__nota1}\nSegunda nota: {self.__nota2}\nMedia: {self.__media}\n")
        return 1

    #● Resultado, que verifica se o aluno está aprovado ou reprovado
    def resultado(self):
        if(self.__media>=6):
            print("Aprovado!")
        else:
            print("Reprovado!")