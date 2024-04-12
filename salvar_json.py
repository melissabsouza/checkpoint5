#Questão 7
import json
import os

class ArquivoInvalido(FileNotFoundError):
    pass

def abrir_bd(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as arquivo:
            return json.load(arquivo)
    else:
        return []
    
def salvar_bd(arquivo, BD):
    with open(arquivo, 'w') as f:
        json.dump(BD, f)