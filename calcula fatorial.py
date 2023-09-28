numero_usuario = int(input('Defina um número para calcular o seu fatorial: '))
fatorial = [numero for numero in range(numero_usuario, 0, -1)]
resultado = 1

print(f'{"=" * 3} Fatorial de {numero_usuario}! {"=" * 3}')
for numero in fatorial:
    valor = resultado
    resultado *= numero
    print(f'{numero} X {valor} = {resultado}')
