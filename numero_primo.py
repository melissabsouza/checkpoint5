#questão 4



def maior_numero_primo(num):
    
    for i in range(num, 1, -1):
        if primo(i):
            return i

def primo(numero):

    if numero <= 1:
        return False
    for i in range(2,numero):
        if (numero % i)  == 0:
            return False
    return True

