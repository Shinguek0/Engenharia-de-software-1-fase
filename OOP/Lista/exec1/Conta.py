#Escreva um método para a classe ContaCorrente() vista em aula, que permita a
#transferência de valores entre duas contas (objetos). Esse método deverá receber
#como parâmetro: valor, origem e destino.
#Dica: o método deve sacar o valor da origem e depositar o valor no destino.

class ContaCorrente():
    def __init__(self, numeroConta, titular, saldo):
        self.__numeroConta = numeroConta
        self.__titular = titular
        self.__saldo = saldo

    def sacar(self, valorSaque):
        self.__saldo -= valorSaque
        return self.__saldo

    def depositar(self, valorDeposito):
        self.__saldo += valorDeposito
        return self.__saldo

    def transferir(self, origem, destino, valorTransferencia):
        origem.__saldo -= valorTransferencia
        destino.__saldo += valorTransferencia
        return print("Transferencia concluida")

    @property
    def saldo(self): 
        return self.__saldo