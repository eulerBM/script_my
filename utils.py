
def num_divi(numeros):
    pares = [numeros.text[i:i+2] for i in range(0, len(numeros.text), 2)]
    return pares