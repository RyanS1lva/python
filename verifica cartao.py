# Programa feito seguindo o algoritimo de Luhn.

num_multiplicados = []
num_nao_multiplicados = []
soma_algarismos = 0

print('Bem vindo, descubra se um número de cartão é válido ou não!')
while True:
    numero_cartao = str(input('Digite o número do cartão: '))
    numero_cartao = numero_cartao.replace(' ', '')

    if numero_cartao.isdigit():
        numero_inverso = numero_cartao[::-1]

        for numero in range(0, len(numero_inverso)):
            if numero % 2 != 0:
                multiplicado = int(numero_inverso[numero]) * 2
                num_multiplicados.append(multiplicado)
            
        for numero in range(0, len(numero_inverso)):
            if numero % 2 == 0:
               nao_multiplicado = int(numero_inverso[numero])
               num_nao_multiplicados.append(nao_multiplicado)
        
        for numero_multiplicado in num_multiplicados:
            if numero_multiplicado <= 9:
                soma_algarismos += numero_multiplicado

            elif numero_multiplicado > 9:
                a, b = str(numero_multiplicado)
                soma_ab = int(a) + int(b)
                soma_algarismos += soma_ab
        
        for nao_multiplicado in num_nao_multiplicados:
            soma_algarismos += nao_multiplicado

        break

    else:
        print('Digite somente números!')
        print('')
        continue

print('')
if soma_algarismos % 10 == 0:
    print('Este cartão possui uma numeração válida!')
    
    if len(numero_cartao) == 16 and numero_cartao[0:2] == '55' or numero_cartao[0:2] == '51':
        print('Tipo de cartão: Mastercard')
    
    elif len(numero_cartao) == 16 or len(numero_cartao) == 13 and numero_cartao[0:] == '4':
        print('Tipo de cartão: Visa')
else:
    print('Este cartão possui uma numeração inválida!')



