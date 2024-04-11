from login import validar_usuario
from validador import validar_senha
from numero_primo import maior_numero_primo

numero_input = int(input("Digite um numero: "))
print(f'o maior numero primo menor que "{numero_input}" é {maior_numero_primo(numero_input)}')

def hashed(senha, numero_input):
    senha_ord = ''
    for c in senha:
        senha_ord += str(ord(c))

    senha_hash = int(senha_ord) % maior_numero_primo(numero_input)

    return senha_hash


def validar_login_senha(login, senha):
    
    senha_hash = hashed(senha, numero_input)

    if validar_senha(senha):
        print("Senha válida")
    else:
        print("Senha inválida")
        return False

    if validar_usuario(login):
        print("Usuário válido")
        return True
    else:
        print("Usuário inválido")
        return False

def cadastrando(login, senha, role, BD, numero_input):

    cadastro_user = {
        'login': login,
        'senha': hashed(senha, numero_input),
        'role': role
    }

    role.lower()

    if validar_login_senha(login, senha) == True:
        print("Login e senha válidos")
        if role == 'admin' or role == 'user':
            print("role válido!")
            print("Usuário cadastrado com sucesso!")
            BD.append(cadastro_user)
        else:
            print("usuario não cadastrado, role inválido")
            return False
    else:
        print('login ou senha inválidos, não adicionado na lista')
    return BD

def atualizar_cadastro(BD):
    login_atual = input("Digite o login atual: ")
    senha_atual = input("Digite a senha atual: ")
    novo_login = input("Digite o novo login: ")
    nova_senha = input("Digite a nova senha: ")

    nova_senha_hashed = hashed(nova_senha, numero_input)

    for usuario in BD:
        if usuario['login'] == login_atual and usuario['senha'] == hashed(senha_atual, numero_input):
            usuario['login'] = novo_login
            usuario['senha'] = nova_senha_hashed
            print("Cadastro atualizado")
            print(BD)
            return

    print("Usuário não encontrado ou senha incorreta.")


def menu_cad():

    BD = []
    while True:
        print('\tCadastrando usuários\n'
            + '1 - Cadastrar\n'
            + '2 - Atualizar cadastro\n'
            + '3 - Sair')
        opcao = input("Digite uma opcão: ")

        match opcao:
            case '1':
                login = input("Digite seu login: ")
                senha = input("digite sua senha: ")
                role = input("Digite seu role (admin ou user): ")
                BD = cadastrando(login, senha, role, BD, numero_input)
                print(BD)
            case '2':
                atualizar_cadastro(BD)
            case '3':
                break
            case _:
                print('opção inválida')

menu_cad()