print('---BEM VINDO AO JOGO DA FORCA---')
print('_________ \n'
  ' |         |  \n'
  ' |         O  \n'
  ' |        /|\ \n'
  ' |        / \ \n'
  '===')

letra_palpite = []
letra_acertada = []
erros = 0

while True:
    palavra_secreta = 'rato'
    letra_digitada = str(input('\nDigite uma letra: '))

    if letra_digitada in letra_palpite:
        print(f'A letra "{letra_digitada}" já foi digitada!')

    if letra_digitada in palavra_secreta and letra_digitada not in letra_palpite:
        letra_acertada.append(letra_digitada)
        letra_palpite.append(letra_digitada)

    
    if letra_digitada not in palavra_secreta and letra_digitada not in letra_palpite:
        erros += 1
    
    
    if erros == 1:
        print('\n_________ \n'
  ' |         |  \n'
  ' |         O  \n'
  ' |         \n'
  ' |         \n'
  '===')
    
    elif erros == 2:
        print('_________ \n'
  ' |         |  \n'
  ' |         O  \n'
  ' |        /|\ \n'
  ' |         \n'
  '===')
    
    elif erros == 3:
        print('_________ \n'
  ' |         |  \n'
  ' |         O  \n'
  ' |        /|\ \n'
  ' |        / \ \n'
  '===')
        print('você perdeu!')
        break

    for letra in palavra_secreta:
        if letra in letra_acertada:
            print(letra, end='')

        else:
            print('_', end='')