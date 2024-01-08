consonantes = {
    'b': 'b',
    'c': 'c',
    'd': 'd',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'j': 'j',
    'k': 'k',
    'l': 'l',
    'll': 'll',
    'm': 'm',
    'n': 'n',
    'ñ': 'ñ',
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': 's',
    't': 't',
    'v': 'v',
    'w': 'w',
    'x': 'x',
    'z': 'z'
}

vocales_abiertas = {
    'a': 'a',
    'e': 'e',
    'o': 'o',
    'á': 'á',
    'é': 'é',
    'ó': 'ó',
    'ú': 'ú'
}

vocales_cerradas = {
    'i': 'i',
    'u': 'u',
    'ü': 'ü'
}

semivocales = {
    'y': 'y'
}

pares_consonantes = {
    'bl': 'bl',
    'cl': 'cl',
    'fl': 'fl',
    'gl': 'gl',
    'kl': 'kl',
    'pl': 'pl',
    'tl': 'tl',
    'br': 'br',
    'cr': 'cr',
    'dr': 'dr',
    'fr': 'fr',
    'gr': 'gr',
    'kr': 'kr',
    'pr': 'pr',
    'tr': 'tr',
    'ch': 'ch',
    'll': 'll',
    'rr': 'rr'
}

va=str(vocales_abiertas)
vc=str(vocales_cerradas)

diptongos = (vc + vc) or (va + vc) or (vc + va)
triptongos = (vc + va + vc)



palabra = str(input("Di una palabra > "))

deletreo=(list(palabra))
 
for letra in deletreo:
    if letra in consonantes:
        print(f"{letra.upper()} - es una consonante.")
    elif letra in va:
        print(f"{letra.upper()} - es una vocal abierta.")
    elif letra in vc:
        print(f"{letra.upper()} - es una vocal cerrada.")
    elif letra in semivocales:
        print(f"{letra.upper()} - es una semivocal.")
    else:
        print(f"{letra.upper()} - no está en ninguna categoría definida en el código.")
        
        
        
        
        