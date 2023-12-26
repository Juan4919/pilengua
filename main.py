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

va=str(vocales_abiertas)
vc=str(vocales_cerradas)

diptongos = (vc + vc) or (va + vc) or (vc + va)
triptongos = (vc + va + vc)

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


    
    