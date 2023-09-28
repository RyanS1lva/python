print(f'{"=-" * 10}TABUADA{"=-" * 10}')
def funcao_tabuada(numero_tabuada):
    tabuada_completa = [numero_tabuada * numero for numero in range(1, 11)]
    return tabuada_completa

for numeros_tabuada in range(1, 11):
    tabuada_resultado = funcao_tabuada(numeros_tabuada)
    print(f'Tabuada do número {numeros_tabuada}: {tabuada_resultado}')