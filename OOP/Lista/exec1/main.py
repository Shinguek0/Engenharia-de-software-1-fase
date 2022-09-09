#Escreva um método para a classe ContaCorrente() vista em aula, que permita a
#transferência de valores entre duas contas (objetos). Esse método deverá receber
#como parâmetro: valor, origem e destino.
#Dica: o método deve sacar o valor da origem e depositar o valor no destino.
from Conta import ContaCorrente

conta1 = ContaCorrente(1,"Jorge",1000)
conta2 = ContaCorrente(2, "Roberto", 2000)

def saldos():
    print(conta1.saldo)
    print(conta2.saldo)

saldos()

conta1.sacar(10)

saldos()

conta1.transferir(conta1,conta2, 50)

saldos()




