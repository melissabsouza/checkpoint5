# RM552525 - Melissa Barbosa de Souza
#Questao 2, 3



import requests
from login import validar_usuario
from validador import validar_senha
from numero_primo import maior_numero_primo
from salvar_json import salvar_bd
from salvar_json import abrir_bd


numero_input = int(input("Digite um numero: "))
print(f'o maior numero primo menor que "{numero_input}" é {maior_numero_primo(numero_input)}')

#questão 8
def gerar_user_id(login, senha_hashed):
    dados = login + str(senha_hashed)
    user_id = 0

    for char in dados:
        user_id += ord(char)

    return user_id



#Questão 5
def hashed(senha, numero_input):
    senha_ord = ''
    for c in senha:
        senha_ord += str(ord(c))

    senha_hash = int(senha_ord) % maior_numero_primo(numero_input)

    return senha_hash


def validar_login_senha(login, senha):

    senha_hash = hashed(senha, numero_input) #questão 6

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
    senha_hashed = hashed(senha, numero_input)
    user_id = gerar_user_id(login, senha_hashed)

    cadastro_user = {
        'id': user_id,
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

#Questão 10
def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Erro ao acessar a API:", response.status_code)
        return None

def atualizar_pokemon_usuario(user_id, BD):
    for usuario in BD:
        if usuario['user_id'] == user_id:
            pokemon_id = int(user_id) % maior_numero_primo() + 1  # Gerar um número de Pokémon entre 1 e 151
            pokemon_data = get_pokemon_data(pokemon_id)
            if pokemon_data:
                usuario['poke_human'] = {
                    'name': pokemon_data['name'].capitalize(),
                    'abilities': []
                }
                for ability in pokemon_data['abilities']:
                    ability_data = get_ability_data(ability['ability']['url'])
                    usuario['poke_human']['abilities'].append({
                        'name': ability_data['name'],
                        'effects': [effect['effect'] for effect in ability_data['effect_entries']],
                        'flavors': [flavor['flavor_text'] for flavor in ability_data['flavor_text_entries']],
                        'pokemon_with_ability': get_pokemon_with_ability(ability_data['pokemon'])
                    })
                print("Dados do Pokémon atualizados para o usuário:", usuario['login'])
                #Questão 10
                salvar_bd(arquivo, BD)
            else:
                print("Não foi possível encontrar dados para o Pokémon do usuário.")
            return
    print("Usuário não encontrado.")

def get_ability_data(ability_url):
    response = requests.get(ability_url)
    if response.status_code == 200:
        ability_data = response.json()
        return ability_data
    else:
        print("Erro ao acessar a API de habilidades:", response.status_code)
        return None

def get_pokemon_with_ability(pokemon_list):
    return [pokemon['pokemon']['name'].capitalize() for pokemon in pokemon_list]

def encontrar_user_id(login, BD):
    for usuario in BD:
        if usuario['login'] == login:
            return usuario.get('user_id')
    print("Usuário não encontrado.")
    return None

def menu_cad(BD, arquivo):

    BD = []
    while True:
        print('\tCadastrando usuários\n'
            + '1 - Cadastrar\n'
            + '2 - Atualizar cadastro\n'
            + '3 - Procurar Pokemon por ID\n'
            + '4 - Sair')
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
            case '4':
                break
            case '3':
                login = input("Digite seu username: ")
                user_id = encontrar_user_id(login, BD)
                if user_id:
                    atualizar_pokemon_usuario(user_id, BD)
            case _:
                print('opção inválida')

arquivo = 'users.json'
BD = abrir_bd(arquivo)
menu_cad(BD, arquivo)