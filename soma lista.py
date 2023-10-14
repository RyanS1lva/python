lista_a = [1, 2, 3, 4, 5, 6, 7]

lista_b = [1, 2, 3, 4]


def soma_listas(lista1, lista2):
    maximo_intervalo = min(len(lista1), len(lista2))
    lista_soma = []
    for i in range(maximo_intervalo):
        lista1[i] += lista2[i]
        lista_soma.append(lista1[i])
    
    return lista_soma

print(soma_listas(lista_a, lista_b))