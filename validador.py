
def validador_RG(rg):
    num = 9
    soma = 0
    for digito in rg[0:8]:
        soma += int(digito) * num
        num -= 1

        dv = soma % 11

    if ((dv == 10) & (rg[-1] == 'X')):
        return(True)
    elif (int(rg[-1]) == dv):
         return(True)
    else:
        return(False)
    
def validador_cpf(cpf):
    ...