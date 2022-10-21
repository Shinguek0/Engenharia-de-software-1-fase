from exec2 import listaDuplamenteEncadeada

def x():
    print("-"*10)

lista = listaDuplamenteEncadeada()
print(lista.listaVazia())

x()

lista.insereInicio(1)
lista.insereInicio(2)
lista.insereInicio(3)
lista.insereInicio(4)
lista.insereInicio(42)
lista.insereInicio(312)
lista.insereInicio(456)
lista.insereInicio(683)
lista.insereInicio(728)

lista.mostrarFrente()
x()
lista.mostrarTras()
x()

print(lista.pesquisar(123))
print(lista.pesquisar(42).valor)

x()

lista.excluirInicio()
lista.excluirFinal()
lista.excluirPosicao(312)
lista.mostrarFrente()