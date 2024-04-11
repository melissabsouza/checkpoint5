from numero_primo import maior_numero_primo

def hashed(senha, numero):
    senha_ord = ''
    for c in senha:
        senha_ord += str(ord(c))

    senha_hash = int(senha_ord) % maior_numero_primo(numero)

    return senha_hash