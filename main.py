# RM552525 - Melissa Barbosa de Souza


from cadastrar_user import menu_cad
from login import validar_usuario
#Menu

print("1 - Validação de Login e Senha\n"
      + "2 - Cadastrando usuários\n"
      + "4 - Encontrar número primo\n"
      + "5 - Atualizar Login e Senha\n"
      + "6 - Encontrar Pokemon\n")

opcao = input("\nDigite uma opção: ")

match opcao:
    case '1':
        validar_usuario()
    case '2':
        menu_cad()