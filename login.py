from validador import validador_RG

class DocumentoInvalido(ValueError):
    pass

class SenhaInvalida(ValueError):
    pass


def validar_senha():
    senha = input("Digite sua senha: ")
    try:
        if len(str(senha)) > 9:
            raise SenhaInvalida("Não pode ter mais que 9 digitos")
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
            ... #cpf
        case "3":
            ... #email
        case "4":
            ... #username
        case _:
            return
