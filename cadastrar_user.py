import oracledb
from login import validar_usuario
from validador import *
from numero_primo import maior_numero_primo
from db import *


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

    senha_hashed = hashed(senha, numero_input)

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

def create_sign_up():
    conn, cursor = create_oracle_connection()

    try:
        print("Criando cadastro...")
        login = input("Digite seu login: ")
        email = input("Digite seu email: ")
        nome = input("Digite seu nome: ")
        rg = input("Digite seu RG: ")
        cpf = input("Digite seu CPF: ")
        data_nascimento = input("Digite sua data de nascimento: ")
        senha = input("Digite sua senha: ")
        endereco = input("Digite seu endereco: ")
        role = 'user'

        senha_hashed = hashed(senha, numero_input)
        user_id = gerar_user_id(login, senha_hashed)


        if validar_login_senha(login, senha) and validador_email(email) and validador_CPF(cpf) and validador_RG(rg):
            print("Válido")
            if role in ['admin', 'user']:
                query = """
                INSERT INTO CADASTRO_CP
                (id, login, senha, email, nome, rg, cpf, data_nascimento, endereco, role) 
                VALUES (:id, :login, :senha, :email, :nome, :rg, :cpf, :data_nascimento, :endereco, :role)
                """
                cursor.execute(query, {
                    'id': user_id,
                    'login': login,
                    'senha': senha_hashed,
                    'email': email,
                    'nome': nome,
                    'rg': rg,
                    'cpf': cpf,
                    'data_nascimento': data_nascimento,
                    'endereco': endereco,
                    'role': role
                })
                conn.commit()

                print("Cadastro criado com sucesso!")
            else:
                print('Role inválido')
        else:
            print('Usuário não cadastrado: e-mail, cpf ou rg inválidos')
    except oracledb.DatabaseError as e:
        print(f"Erro ao criar cadastro: {e}")
    finally:
        cursor.close()
        conn.close()

def read_by_user(login):
    conn, cursor = create_oracle_connection()
    try:
        query = "SELECT * FROM CADASTRO_CP WHERE login = :login"
        cursor.execute(query, {'login': login})
        results = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

        return [dict(zip(columns, row)) for row in results]
    except oracledb.DatabaseError as e:
        print(f"Erro na consulta: {e}")
    finally:
        cursor.close()
        conn.close()


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

    while True:
        print('\tCadastrando usuários\n'
            + '1 - Cadastrar\n'
            + '2 - Ler Cadastro\n'
            + '3 - Excluir Cadastro\n'
            + '4 - Alterar Cadastro\n'
            + '5 - Sair')
        opcao = input("Digite uma opcão: ")

        match opcao:
            case '1':
                create_sign_up()
            case '2':
                login = input("Digite o username para filtrar: ")
                resultado_username = read_by_user(login)
                if resultado_username:
                    print(read_by_user(login))
            case '3':
                ...
            case '5':
                break
            case _:
                print('opção inválida')

menu_cad()