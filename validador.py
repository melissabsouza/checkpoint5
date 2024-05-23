#Questão 1

import re


class DocumentoInvalido(ValueError):
    pass

class SenhaInvalida(ValueError):
    pass

def validador_RG(login):
 
    num = 9
    soma = 0
    for digito in login[0:8]:
        soma += int(digito) * num
        num -= 1

    dv = soma % 11

    if ((dv == 10) & (login[-1] == 'X')):
        return True
    elif (int(login[-1]) == dv):
         return True
    else:
        return False
    
def validador_CPF(login):

    nove_digitos = login[:9]
    contador = 10

    resultado_digito = 0
    for digito in nove_digitos:
        resultado_digito += int(digito) * contador
        contador -= 1
    digito_1 = (resultado_digito * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    try:
        if cpf_gerado_pelo_calculo == login:
            print("CPF validado com sucesso.")
            return True
        else:
            raise DocumentoInvalido("Documento Inválido")
    except DocumentoInvalido as e:
            print(e)


def validador_email(login):
    regex = r'^[\w.-]+@[a-z\d]+\.[\w]{2,}$'
    return re.match(regex, login) is not None

def validador_username(login):
    regex = r'^[a-z0-9_-]{3,10}$'
    return re.match(regex, login) is not None

def validar_senha(senha):
        try:
            if len(str(senha)) < 15:
                raise SenhaInvalida("Senha não pode ter menos que 15 digitos")
            elif senha.isalpha() :
                raise SenhaInvalida("A senha necessita de números")
            elif senha.isalnum() :
                raise SenhaInvalida("Senha precisa de caractere especial")
            elif senha.islower():
                raise SenhaInvalida("Senha tem que ter caracteres maiusculos")
            else:
                print('senha válida')
                return True
    
        except SenhaInvalida as e:
            print(e)