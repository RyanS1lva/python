def tabuada(multiplicador):
    def numero_multiplicado(numero):
        return numero * multiplicador
    return numero_multiplicado


tabuada_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_digitado = int(input('Digite o número para ver a sua tabuada: '))
for num in tabuada_numeros:
    multiplicacao = tabuada(num)
    print(multiplicacao(numero_digitado))