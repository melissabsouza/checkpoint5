from validador import validador_RG

def fazer_login():
    print("Qual seu tipo de Login?\n" 
          + "1 - RG\n"
          + "2 - CPF\n"
          + "3 - E-mail\n"
          + "4 - Username\n")
    
    tipo_login = input("Digite uma opção: ")

    match tipo_login:
        case "1":
            rg = input("Digite seu RG, sem pontos ou traço: ")
            validador = validador_RG(rg)
            if (validador == True):
                print("RG validado com sucesso.")
            else:
                print("Documento inválido.")
        case "2":
            ... #cpf
        case "3":
            ... #email
        case "4":
            ... #username