# RM552525 - Melissa Barbosa de Souza
from cadastrar_user import *

def menu_cad():
    while True:
        print('\tCadastrando usuários\n'
              '1 - Cadastrar\n'
              '2 - Ler Cadastro\n'
              '3 - Excluir Cadastro\n'
              '4 - Alterar Cadastro\n'
              '5 - Sair')
        opcao = input("Digite uma opção: ")

        match opcao:
            case '1':
                create_sign_up()
            case '2':
                login = input("Digite o username para filtrar: ")
                resultado_username = read_by_user(login)
                if resultado_username:
                    pprint(resultado_username)
                else:
                    print("Usuário não encontrado.")
            case '3':
                login = input("Digite o username para exclusão de cadastro: ")
                resultado_login = read_by_user(login)
                if resultado_login:
                    deletar = input("Deseja deletar este registro? (s/n): ")
                    if deletar.lower() == 's':
                        delete_by_user(login)
                        print("Cadastro excluído com sucesso.")
                    else:
                        print("Operação cancelada.")
                else:
                    print("Usuário não encontrado.")
            case '4':
                login = input("Digite o username que você deseja atualizar: ")
                resultado_username = read_by_user(login)
                
                if resultado_username:
                    atualizar = input("Deseja atualizar este registro? (s/n): ")
                    
                    if atualizar.lower() == 's':
                        updates = {}
                        
                        novo_login = input("Digite o novo username (ou pressione Enter para manter o atual): ")
                        if novo_login:
                            updates['login'] = novo_login
                        
                        senha = input("Digite a nova senha (ou pressione Enter para manter a atual): ")
                        if senha:
                            numero_input = input("Digite um número para o hashing: ")
                            senha_hashed = hashed(senha, int(numero_input))
                            updates['senha'] = senha_hashed
                        
                        email = input("Digite o novo email (ou pressione Enter para manter o atual): ")
                        if email:
                            updates['email'] = email
                        
                        nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
                        if nome:
                            updates['nome'] = nome
                        
                        endereco = input("Digite o novo endereco (ou pressione Enter para manter o atual): ")
                        if endereco:
                            updates['endereco'] = endereco

                        if updates:
                            att_cadastro(login, updates)
                        else:
                            print("Nenhuma atualização foi feita.")
                    else:
                        print("Atualização cancelada.")
                else:
                    print("Usuário não encontrado.")
            case '5':
                break
            case _:
                print('Opção inválida.')

menu_cad()
