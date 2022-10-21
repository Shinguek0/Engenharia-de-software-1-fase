#Crie uma função recursiva que calcule o valor de a (base) elevado a b (expoente)
#- Se o expoente for zero, a potência é igual 1 (critério de parada)
#- Não considere exponenciação de números negativos

def funcExponencial(num, expoente):
    if(expoente == 0 or num < 0):
        return 1
    return num * funcExponencial(num, expoente - 1)
    
print(funcExponencial(20, 3))