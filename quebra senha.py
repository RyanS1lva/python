import copy, time

caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
caracteres_maius = copy.deepcopy(caracteres)
for letra in caracteres_maius:
    letra = letra.upper()
    caracteres.append(letra)
caracteres_especiais = [' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '<', '>', ',', '.', '?', '/', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'ç', '€', '£', '¥', '§', '°', '²', '³', '©', '®', '¼', '½', '¾']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
caracteres.extend(caracteres_especiais)
caracteres.extend(numeros)


senha = str(input('Digite a senha para ser quebrada: '))
palavra_formada = ''
print('')
while True:
    for letra in senha:
        for caracter in caracteres:
            time.sleep(0.002)
            if palavra_formada == senha:
                break
            elif len(palavra_formada) == len(senha):
                break
            if caracter == letra:
                palavra_formada += letra
                print(palavra_formada)
            else:
                print(f'{palavra_formada}{caracter}')