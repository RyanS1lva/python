print('---JOGO DA FORCA---')
print( '_________\n' 
   '|         |\n'
   '|         O\n'
   '|        /|\ \n'
   '|        / \  \n'
 '===\n')

palavra_secreta = 'rato'.lower()
palavra_formada = []
while True:
    letra_digitada = str(input('\nDigite uma letra: ')).lower()
    if letra_digitada in palavra_secreta:
        palavra_formada.append(letra_digitada)
    
    for letra in palavra_formada:
        print(letra, end='')

    
    if len(palavra_formada) == len(palavra_secreta):
        print(f'\nParabéns, você venceu, a palavra era {palavra_secreta}!')
        break
