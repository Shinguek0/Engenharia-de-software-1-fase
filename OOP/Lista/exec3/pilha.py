#Crie uma pilha que armazene 5 palavras. Além dos métodos básicos vistos em aula, crie um método que permita a impressão dos valores da pilha.
#Dica: lembre-se que é uma pilha, logo os valores da impressão devem aparecer na ordem inversa, ou seja, da base para o topo.

class Pilha():
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.topo = -1
        self.pilha = [""] * tamanho
    
    def empilhar(self, valor):
        if(self.pilhaCheia()):
            return print("Pilha cheia")
        self.topo+=1
        self.pilha[self.topo] = valor

    def desempilhar(self):
        if(self.pilhaVazia()):
            return print("Pilha Vazia!")
        self.topo-=1

    def pilhaCheia(self):
        return self.topo == self.tamanho-1

    def pilhaVazia(self):
        return self.topo == -1

    def mostrarTopo(self):
        if(self.pilhaVazia()):
            return -1
        return self.pilha[self.topo]
    
    def mostrarPilha(self):
        if(self.pilhaVazia()):
            return -1
        return self.pilha

def show():
    print(a.mostrarPilha())
    print(a.mostrarTopo())

a = Pilha(5)

a.desempilhar()

a.empilhar("Era")
show()

a.empilhar("uma")
show()

a.empilhar("vez")
show()

a.empilhar("uma")
show()

a.desempilhar()
show()

a.empilhar("em")
show()

a.empilhar("Fim!!")
show()

a.empilhar("Fim!!")