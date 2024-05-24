#CRUD

import oracledb
from login import validar_usuario
from validador import *
from numero_primo import maior_numero_primo
from db import *

from pprint import pprint

numero_input = int(input("Digite um numero: "))
print(f'o maior numero primo menor que "{numero_input}" é {maior_numero_primo(numero_input)}')

def gerar_user_id(login, senha_hashed):
    dados = login + str(senha_hashed)
    user_id = 0

    for char in dados:
        user_id += ord(char)

    return user_id

def hashed(senha, numero_input):
    senha_ord = ''.join(str(ord(c)) for c in senha)
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
                (id, login, senha, email, nome, rg, cpf, data_nascimento, endereco) 
                VALUES (:id, :login, :senha, :email, :nome, :rg, :cpf, :data_nascimento, :endereco)
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
                })

                query_login = """
                INSERT INTO LOGIN_CP
                (id, login, senha, role) VALUES (:id, :login, :senha, :role)
                """
                cursor.execute(query_login, {
                    'id': user_id,
                    'login': login,
                    'senha': senha_hashed,
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

def delete_by_user(login):
    conn, cursor = create_oracle_connection()
    try:
        query = "DELETE FROM CADASTRO_CP WHERE login = :login"
        query_2 = "DELETE FROM LOGIN_CP WHERE login = :login"
        cursor.execute(query, {'login': login})
        cursor.execute(query_2, {'login': login})
        conn.commit()
    except oracledb.DatabaseError as e:
        print(f"Erro ao excluir: {e}")
    finally:
        cursor.close()
        conn.close()

def att_cadastro(login, updates):
    conn, cursor = create_oracle_connection()
    try:
        # Verifica os campos válidos na tabela CADASTRO_CP
        valid_columns = set()
        cursor.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'CADASTRO_CP'")
        for row in cursor.fetchall():
            valid_columns.add(row[0].lower())
        
        
        updates = {k: v for k, v in updates.items() if k.lower() in valid_columns}
        
        set_clause = ', '.join([f"{key} = :{key}" for key in updates.keys()])
        updates['original_login'] = login
        query = f"UPDATE CADASTRO_CP SET {set_clause} WHERE login = :original_login"
        
        
        cursor.execute(query, updates)
        
        
        login_cp_updates = {k: updates[k] for k in ['login', 'senha'] if k in updates}
        if login_cp_updates:
            set_clause = ', '.join([f"{key} = :{key}" for key in login_cp_updates.keys()])
            login_cp_updates['original_login'] = login
            query_2 = f"UPDATE LOGIN_CP SET {set_clause} WHERE login = :original_login"
            cursor.execute(query_2, login_cp_updates)

        conn.commit()
        print("Atualizado!")
    except oracledb.DatabaseError as e:
        print(f"Erro ao atualizar registro: {e}")
    finally:
        cursor.close()
        conn.close()
