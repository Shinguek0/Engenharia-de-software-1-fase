#Utilize a estrutura de dados do tipo Fila e simule um programa de emissão de senhas de atendimento de uma farmácia. A Fila deverá ter uma capacidade máxima de 10
#elementos que deverão ser do tipo Dicionário, cujo as chaves devem ser a palavra “senha” (para as 10 posições) e valores sequenciais de 1 a 10. Ao chamar a função
#primeiro(), ela deverá mostrar o conteúdo do dicionário (chave e valor) Dica: crie um dicionário vazio e depois passe um Array de 10 posições contendo o
#Dicionário criado para o parâmetro “valores” da Lista. Ex: [{},{},{},...{}]

class Fila():
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.final = -1
        self.inicio = 0
        self.nElementos = 0
        self.lugarFila = 0
        self.fila = []
        for i in range(self.tamanho):
            self.fila.append({})

    def enfileirar(self):
        if(self.filacheia()):
            return print("A fila está cheia!")
        self.final+=1
        if(self.final == self.tamanho):
            self.final = 0
        self.nElementos+=1
        self.lugarFila+=1
        self.fila[self.final] = {"Senha" : self.lugarFila}
        return self.fila

    def desenfileirar(self):
        if(self.filaVazia()):
            return print("A fila está vazia!")
        temp = self.primeiro()
        self.inicio+=1
        if(self.inicio == self.tamanho):
            self.inicio = 0
        self.nElementos -= 1
        return temp

    def showFila(self):
        return self.fila

    def primeiro(self):
        if(self.filaVazia()):
            return print("A fila está vazia!")
        return self.fila[self.inicio]

    def filacheia(self):
        return self.nElementos == self.tamanho

    def filaVazia(self):
        return self.nElementos == 0

fila = Fila(10)

fila.desenfileirar()

for i in range(10):
    fila.enfileirar()
    print(fila.showFila()) 

fila.enfileirar()
print(fila.showFila()) 

print(fila.primeiro())

print(fila.desenfileirar())
print(fila.showFila())

fila.enfileirar()
print(fila.showFila()) 

print(fila.primeiro())

for i in range(10):
    print(fila.desenfileirar())
    print(fila.showFila())

fila.desenfileirar()