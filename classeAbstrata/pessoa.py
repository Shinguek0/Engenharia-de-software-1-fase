# Importa ABC, Abstract Base Classes, que serve para fazer classes e metodos abstratos em python
from abc import ABC, abstractmethod

#cria uma classe abstrata chamada pessoa
class Pessoa():
    #Define suas caracteristicas
    nome = 'Sem nome'
    idade = 0
    sexo = "Sem sexo"

    #cria um metodo abstrato andar
    @abstractmethod
    def andar(self, distancia, velocidade):
        pass

#cria outra classe abstrata que herda a primeira classe abstrata Pessoa 
class Empregado(Pessoa):
    #da uma caracteristica especifica dessa classe
    salario = 0

    #cria um metodo abstrato especifico para essa classe
    @abstractmethod
    def reajuteSalario(self, aumento):
        pass

#cria outra classe abstrata que herda a primeira classe abstrata Pessoa 
class Desempregado(Pessoa):
    #da uma caracteristica especifica dessa classe
    tempoLivre = 0

    #cria um metodo abstrato especifico para essa classe
    @abstractmethod
    def tempoLivreGasto(self, tempoGasto):
        pass

#cria a classe empresario que herda Empregado, que por sua vez herda Pessoa
class Empresario(Empregado):
    def __init__(self, nome, idade, sexo, salario, tempoTrabalho):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.__salario = salario
        #caso tirar a calsse abstrata empresario, cria salario igual a classe tempoTrabalho, ela foi criada meramente como teste
        self.tempoTrabalho = tempoTrabalho #Variavel nao ultilizada criada so para teste
    
    #encapsula salario
    @property
    def salario(self): 
        return self.__salario

    @salario.setter
    def salario(self, novo_salario): 
        raise ValueError("Impossivel alterar salario diretamente. Use a funcao reajusteSalario().")

    #funçoes que vem das classes abstratas
    def reajusteSalario(self, aumento):
        #aumenta o salario recebendo uma porcentagem de aumento
        self.__salario += self.__salario*(aumento/100)

    def andar(self, distancia, velocidade):
        print("Tempo andado:",distancia*velocidade)

#cria a classe Aluno que herda Empregado, que por sua vez herda Pessoa
class Aluno(Desempregado):
    def __init__(self, nome, idade, sexo, tempoLivre):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.tempoLivre = tempoLivre

    #funçoes que vem das classes abstratas
    def tempoLivreGasto(self, tempoGasto):
        self.tempoLivre -= tempoGasto

    def andar(self, distancia, velocidade):
        print("Tempo andado:",distancia*velocidade)