def inverter_texto(texto):
    return texto[::-1]

def contar_caracteres(texto):
    return len(texto)

def contar_vogal_e_consoante(texto):
    cont_vogal = 0
    cont_consoante = 0
    for letra in texto:
        if letra.lower() in 'aeiou':
            cont_vogal += 1
        elif letra.lower() in 'bcdfghjklmnpqrstvwxyz':
            cont_consoante += 1
    return [cont_vogal, cont_consoante]