print('Bem-vindo ao jogo de perguntas!')

perguntas = [
    {
        'Pergunta': 'Quanto é 33 x 3?',
        'Opções': ['99', '55', '44', '100'],
        'Resposta': '99',
    },
    {
        'Pergunta': 'Qual a capital do Brasil?',
        'Opções': ['Rio Pardo', 'São Paulo', 'Rio de Janeiro', 'Brasília'],
        'Resposta': 'Brasília',
    },
      {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

acertos = 0
erros = 0

for pergunta_k in perguntas:
    pergunta_coletada = pergunta_k['Pergunta']
    opcoes_coletadas = pergunta_k['Opções']
    resposta_coletada = pergunta_k['Resposta']

    while True:
        pergunta_input = input(f'\n{pergunta_coletada}\nOpções: {opcoes_coletadas}\nDigite uma das opções: ').strip()

        if pergunta_input == resposta_coletada:
            print(f'Você acertou, a resposta era {resposta_coletada}!')
            acertos += 1
            break
        elif pergunta_input not in opcoes_coletadas:
            print('Você não digitou uma opção válida!')
            continue
        else:
            print(f'Você errou, a resposta era {resposta_coletada}!')
            erros += 1
            break

print(f'\nJogo encerrado!\nTotal de acertos: {acertos}\nTotal de erros: {erros}')




