numero_blocos = int(input('Digite o número de blocos de altura(1 a 8): '))


if numero_blocos >= 1 and numero_blocos <= 8:
    for bloco in range(1 ,numero_blocos + 1):
        print(f'{bloco * "#":>8}  {bloco * "#"}')

else:
    print('Número inválido!')