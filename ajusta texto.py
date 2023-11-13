from time import sleep
def remover_acentos(texto):
    texto = texto.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
    texto = texto.replace('À', 'A').replace('È', 'E').replace('Ì', 'I').replace('Ò', 'O').replace('Ù', 'U')
    texto = texto.replace('Â', 'A').replace('Ê', 'E').replace('Î', 'I').replace('Ô', 'O').replace('Û', 'U')
    texto = texto.replace('Ã', 'A').replace('Õ', 'O').replace('Ç', 'C')
    caracteres_especiais = caracteres_especiais = "!@#$%^&*()_+-=[]}{|;':|\"\<>?/"
    for caracter in caracteres_especiais:
        texto = texto.replace(caracter, ' ')
    return texto

print(f'{"=-" * 3}EXECUTÁVEL DESENVOLVIDO POR RYAN{"-=" * 3}')
while True:
    texto = str(input('Digite um texto para formatá-lo: ')).upper().strip()
    texto_sem_acentos = remover_acentos(texto)
    print(texto_sem_acentos)
    print()
    loop = str(input('[S] Sim\n[N] Não\nVocê deseja continuar: ')).upper().strip()[0]
    if loop == 'S':
        print()
        continue
    elif loop == 'N':
        print('Finalizando...')
        sleep(1)
        print('Volte logo!')
        break
    
    else:
        print('Função não encontrada, tente novamente!')
        continue

