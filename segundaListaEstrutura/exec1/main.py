from exec1 import listaEncadeada

def x():
    print("-"*10)

lista = listaEncadeada()
lista.inserirInicio(2)
lista.inserirInicio(45)
lista.inserirInicio(353)
lista.inserirInicio(124)
lista.mostrar()

x()

lista.excluirInicio()
lista.mostrar()

x()

print(lista.pesquisar(3))
print(lista.pesquisar(353))

x()

print("Item excluido:",lista.excluirValor(353))
