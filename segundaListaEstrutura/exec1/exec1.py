#Crie uma Lista Encadeada Simples que armazene 5 nomes de pessoas. Demonstre o
#funcionamento de todos os métodos da classe.

class No():
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostraNo(self):
        return self.valor

class listaEncadeada():
    def __init__(self):
        self.primeiro = None

    def inserirInicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if(self.listaVazia()):
            print("Erro Lista vazia")
            return None
        atual = self.primeiro
        while(atual != None):
            print(atual.mostraNo())
            atual = atual.proximo
        
    def excluirInicio(self):
        if(self.listaVazia()):
            print("Erro Lista vazia")
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

    def pesquisar(self, valor):
        if(self.listaVazia()):
            print("Erro lista vazia")
            return None
        atual = self.primeiro
        while(atual.valor != valor):
            if(atual.proximo == None):
                return None
            else:
                atual = atual.proximo
        return atual

    def excluirValor(self, valor):
        if(self.listaVazia()):
            print("Lista vazia...")
            return None
        atual = self.primeiro
        anterior = self.primeiro
        while(atual.valor != valor):
            if(atual.proximo == None):
                return None
            else:
                anterior = atual
                atual = atual.proximo
        if (atual == self.primeiro):
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        return atual

    def listaVazia(self):
        return self.primeiro == None

