# RM552525 - Melissa Barbosa de Souza
from validador import validador_RG
from login import fazer_login
#Menu

print("1 - Validação de Login e Senha\n"
      + "2 - Cadastrando usuários\n"
      + "3 - Atualizar Login e Senha\n"
      + "4 - Encontrar Pokemon\n")

opcao = input("\nDigite uma opção: ")

match opcao:
    case '1':
        fazer_login()
    case '2':
        ...