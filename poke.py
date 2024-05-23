import requests
from numero_primo import primo

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
            pokemon_id = int(user_id) % primo() + 1  # Gerar um número de Pokémon entre 1 e 151
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