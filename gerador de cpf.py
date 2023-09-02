import random
algarismos = []
for i in range(0, 9):
    algarismos.append(random.randint(0, 9))


multiplicador = 10
soma_multiplicacao = 0
for i in algarismos:
    soma_multiplicacao += i * multiplicador
    multiplicador -= 1

soma_multiplicacao = soma_multiplicacao * 10

resto_divisao = soma_multiplicacao % 11

if resto_divisao > 9:
    algarismos.append(0)

else:
    algarismos.append(resto_divisao)

multiplicador_1 = 11
soma_multiplicacao_1 = 0
for i in algarismos:
    soma_multiplicacao_1 += i * multiplicador_1
    multiplicador_1 -= 1

soma_multiplicacao_1 = soma_multiplicacao_1 * 10

resto_divisao_1 = soma_multiplicacao_1 % 11

if resto_divisao_1 > 9:
    algarismos.append(0)

else:
    algarismos.append(resto_divisao_1)


cpf = ''.join(map(str, algarismos))
cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

print(f'Aqui está o seu cpf: {cpf_formatado}')


