def buscar_diptongos_triptongos(palabra):
    vocales_abiertas = {'a', 'e', 'o', 'á', 'é', 'ó', 'ú'}
    vocales_cerradas = {'i', 'u', 'ü'}
    semivocales = {'y'}

    consonantes = {
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'll',
        'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w',
        'x', 'z'
    }

    pares_consonantes = {
        'bl', 'cl', 'fl', 'gl', 'kl', 'pl', 'tl',
        'br', 'cr', 'dr', 'fr', 'gr', 'kr', 'pr', 'tr',
        'ch', 'll', 'rr'
    }

    va = set(vocales_abiertas)
    vc = set(vocales_cerradas)

    # Crear variable para diptongos
    diptongos = [vc + vc for vc in vocales_cerradas] + [va + vc for va in vocales_abiertas for vc in vocales_cerradas] + [vc + va for vc in vocales_cerradas for va in vocales_abiertas]

    # Crear variable para triptongos
    triptongos = [vc + va + vc for vc in vocales_cerradas for va in vocales_abiertas]

    # Convertir palabra a minúsculas para facilitar la comparación
    palabra = palabra.lower()

    # Buscar en cada letra de la palabra
    for letra in palabra:
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

    print("\nAnálisis de diptongos y triptongos:\n")

    # Buscar diptongos y triptongos en la palabra
    for i in range(len(palabra) - 1):
        conjunto = palabra[i:i + 2]
        if conjunto in diptongos:
            print(f"{conjunto.upper()} - es un diptongo")
        elif conjunto in triptongos:
            print(f"{conjunto.upper()} - es un triptongo.")

    for i in range(len(palabra) - 2):
        conjunto = palabra[i:i + 3]
        if conjunto in triptongos:
            print(f"{conjunto.upper()} - es un triptongo.")

    # Separar sílabas
    silabas = separar_silabas(palabra, pares_consonantes)
    print("\nSílabas separadas:", silabas)


def separar_silabas(palabra, pares_consonantes):
    vocales_abiertas = {'a', 'e', 'o', 'á', 'é', 'ó', 'ú'}
    vocales_cerradas = {'i', 'u', 'ü'}
    consonantes = {
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'll',
        'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w',
        'x', 'y', 'z'
    }

    silabas = []
    silaba_actual = ""

    for letra in palabra:
        if letra in vocales_abiertas or letra in vocales_cerradas:
            # 1. Buscar grupos de vocales
            silaba_actual += letra

            # 2. Asignar la consonante de la izquierda si existe
            if len(silaba_actual) > 1 and silaba_actual[-2] in consonantes:
                if silaba_actual[-2:] not in pares_consonantes:
                    silabas.append(silaba_actual[:-2])
                    silaba_actual = silaba_actual[-2:]

        else:
            # 3. Agregar letras sin usar a la sílaba a la izquierda
            silaba_actual += letra

    # Agregar la última sílaba
    silabas.append(silaba_actual)

    return silabas


# Ejemplo de uso
palabra_ingresada = input("Ingrese una palabra: ")
buscar_diptongos_triptongos(palabra_ingresada)
