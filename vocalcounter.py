
def contadorvocales(palabra):
    palabra = palabra.lower()
    VOCALES = ('a', 'e', 'i', 'o', 'u')
    vocalcounter = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for letra in palabra:
        if letra in VOCALES:
            vocalcounter[letra] += 1
    return vocalcounter



