from validador import validador_RG
from validador import validador_CPF
from validador import validador_email
from validador import validador_username


class DocumentoInvalido(ValueError):
    pass


class ExpressaoInvalida(ValueError):
    pass


def validar_usuario(login):
    print("Qual seu tipo de Login?\n"
          + "1 - RG\n"
          + "2 - CPF\n"
          + "3 - E-mail\n"
          + "4 - Username\n")
    
    tipo_login = input("Digite uma opção: ")

    match tipo_login:
        case "1":
            login = login.replace("-", "")
            login = login.replace(".", "")
            validador = validador_RG(login)
            try:
                if (validador == True):
                    print("RG validado com sucesso.")
                    return True
                else:
                    raise DocumentoInvalido("Documento Inválido")
            except DocumentoInvalido as e:
                print(e)
        case "2":
            login = login.replace("-", "")
            login = login.replace(".", "")
            
            validador_CPF(login)
        case "3":
            
            validador = validador_email(login)

            try:
                if validador == True:
                    print("E-mail válido")
                    return True
                else:
                    raise ExpressaoInvalida("E-mail inválido")
            except ExpressaoInvalida as e:
                print(e)
        case "4":
            validador = validador_username(login)
            try:
                if validador == True:
                    print("Username válido")
                    return True
                else:
                    raise ExpressaoInvalida("Username inválido")
            except ExpressaoInvalida as e:
                print(e)
        case _:
            return False
