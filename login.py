from validador import validador_RG
from validador import validador_CPF
from validador import validador_email
from validador import validador_username


class DocumentoInvalido(ValueError):
    pass

class SenhaInvalida(ValueError):
    pass

class ExpressaoInvalida(ValueError):
    pass


def validar_senha():
        senha = input("Digite sua senha: ")
        try:
            if len(str(senha)) > 9:
                raise SenhaInvalida("Não pode ter mais que 9 digitos")
            elif senha.islower():
                raise SenhaInvalida("Tem que ter caracteres maiusculos")
            elif senha.isalpha() :
                raise SenhaInvalida("A senha necessita de números")
            elif senha.isalnum() :
                raise SenhaInvalida("Precisa de caractere especial")
    
        except SenhaInvalida as e:
            print(e)

def validar_usuario():
    print("Qual seu tipo de Login?\n"
          + "1 - RG\n"
          + "2 - CPF\n"
          + "3 - E-mail\n"
          + "4 - Username\n")
    
    tipo_login = input("Digite uma opção: ")

    match tipo_login:
        case "1":
            rg = input("Digite seu RG: ")
            rg = rg.replace("-", "")
            rg = rg.replace(".", "")
            validador = validador_RG(rg)
            try:
                if (validador == True):
                    print("RG validado com sucesso.")
                else:
                    raise DocumentoInvalido("Documento Inválido")
            except DocumentoInvalido as e:
                print(e)
            
            validar_senha()
        case "2":
            cpf = input("Digite seu CPF: ")
            cpf = cpf.replace("-", "")
            cpf = cpf.replace(".", "")
            
            validador_CPF(cpf)
            validar_senha()
        case "3":
            email = input("Digite seu Email: ")
            validador = validador_email(email)

            try:
                if validador == True:
                    print("E-mail válido")
                else:
                    raise ExpressaoInvalida("E-mail inválido")
            except ExpressaoInvalida as e:
                print(e)
        case "4":
            username = input("Digite seu Username: ")
            validador = validador_username(username)

            try:
                if validador == True:
                    print("Username válido")
                else:
                    raise ExpressaoInvalida("Username inválido")
            except ExpressaoInvalida as e:
                print(e)
        case _:
            return
