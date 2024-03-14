
def num_divi(numeros) -> list:
    pares = [numeros.text[i:i+2] for i in range(0, len(numeros.text), 2)]
    return pares

def quina_filtrar_numeros(num: list) -> str:
    num.insert(0, 0)
    resultado_sem_virgula = str(num).replace(',', '')
    resultado_sem_espacos = resultado_sem_virgula.replace(" ", "")
    resultado_sem_conchete1 = resultado_sem_espacos.replace("[", "")
    resultado_sem_conchete2 = resultado_sem_conchete1.replace("]", "")
    return resultado_sem_conchete2