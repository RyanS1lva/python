cpf_bruto = str(input('Digite o seu cpf: '))

cpf_sem_ponto = cpf_bruto.replace('.','')
cpf_trabalhado = cpf_sem_ponto.replace('-', '')
cpf_algarismos_10 = cpf_trabalhado[0:10]
cpf_algarismos_9 = cpf_sem_ponto[0:9]
soma_multiplicacao_9 = 0
multiplicador = 10
for i in cpf_algarismos_9:
    i = int(i)
    multiplicacao = i * multiplicador
    soma_multiplicacao_9 += multiplicacao
    multiplicador -= 1

soma_multiplicacao_9 = soma_multiplicacao_9 * 10

resto_divisao_9 = soma_multiplicacao_9 % 11

if resto_divisao_9 > 9:
    resultado_1 = 0

else:
    resultado_1 = resto_divisao_9


multiplicador_1 = 11
soma_multiplicacao_10 = 0
for j in cpf_algarismos_10:
    j = int(j)
    multiplicacao_1 = j * multiplicador_1
    soma_multiplicacao_10 += multiplicacao_1
    multiplicador_1 -= 1

soma_multiplicacao_10 = soma_multiplicacao_10 * 10
resto_divisao_10 = soma_multiplicacao_10 % 11

if resto_divisao_10 > 9:
    resultado_2 = 0

else:
    resultado_2 = resto_divisao_10

final_cpf = str(resultado_1) + str(resultado_2)

if final_cpf == cpf_trabalhado[9:11]:
    print('Este cpf é válido!')

else:
    print('Este cpf não é válido!')