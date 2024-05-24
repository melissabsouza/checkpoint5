import requests
from login import validar_usuario
from validador import *
from numero_primo import maior_numero_primo
from salvar_json import salvar_bd
from salvar_json import abrir_bd


numero_input = int(input("Digite um numero: "))
print(f'o maior numero primo menor que "{numero_input}" é {maior_numero_primo(numero_input)}')

def gerar_user_id(login, senha_hashed):
    dados = login + str(senha_hashed)
    user_id = 0

    for char in dados:
        user_id += ord(char)

    return user_id




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

def cadastrando(login, senha, role, email, nome, rg, cpf, data_nascimento, endereco, BD, numero_input):
    senha_hashed = hashed(senha, numero_input)
    user_id = gerar_user_id(login, senha_hashed)

    cadastro_user = {
        'id': user_id,
        'login': login,
        'e-mail': email,
        'nome': nome,
        'RG': rg,
        'cpf': cpf,
        'data-nascimento': data_nascimento,
        'senha': hashed(senha, numero_input),
        'endereco': endereco,
        'role': role
        
    }

    role.lower()

    if validar_login_senha(login, senha) == True and validador_email(email) == True and validador_CPF(cpf) == True and validador_RG(rg) == True:
        print("Válido")
        if role == 'admin' or role == 'user':
            print("role válido!")
            BD.append(cadastro_user)
            print("Usuário cadastrado com sucesso!")
        else:
            print("usuario não cadastrado: role inválido")
            return False
    else:
        print('usuario não cadastrado: e-mail, cpf ou rg inválidos')
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


def menu_cad(BD, arquivo):

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
                salvar_bd(arquivo, BD)
                print(BD)
            case '2':
                atualizar_cadastro(BD)
                salvar_bd(arquivo, BD)
            case '3':
                break
            case _:
                print('opção inválida')

arquivo = 'users.json'
BD = abrir_bd(arquivo)
menu_cad(BD, arquivo)