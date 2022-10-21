#Repita o exercício 1 utilizando uma Lista Duplamente Encadeada. Demonstre o
#funcionamento de todos os métodos da classe.

class No():
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

    def mostraNo(self):
        return self.valor

class listaDuplamenteEncadeada():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def listaVazia(self):
        return self.primeiro == None

    def insereInicio(self, valor):
        novo = No(valor)
        if self.listaVazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insereFinal(self, valor):
        novo = No(valor)
        if self.listaVazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo
  
    def excluirInicio(self):
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp

    def excluirFinal(self):
        temp = self.ultimo
        if self.primeiro.proximo == None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior
        return temp

    def excluirPosicao(self, valor):
        atual = self.primeiro
        while atual.valor != valor:
            atual = atual.proximo
            if atual == None:
                return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo

        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        return atual

    def mostrarFrente(self):
        atual = self.primeiro
        while atual != None:
            print(atual.mostraNo())
            atual = atual.proximo

    def mostrarTras(self):
        atual = self.ultimo
        while atual != None:
            print(atual.mostraNo())
            atual = atual.anterior

    def pesquisar(self, valor):
      if self.primeiro == None:
        print('A lista está vazia')
        return None

      atual = self.primeiro
      while atual.valor != valor:
        if atual.proximo == None:
          return None
        else:
          atual = atual.proximo
      return atual