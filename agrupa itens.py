from itertools import groupby
videogames = [{'Empresa': 'Sony','Console': 'Playstation 1'},
              {'Empresa': 'Microsoft','Console': 'XBOX 360'},
              {'Empresa': 'Sony','Console': 'Playstation 2'},
              {'Empresa': 'Nintendo','Console': 'Super Nintendo'},
              {'Empresa': 'Nintendo','Console': 'Wii'},
              {'Empresa': 'Microsoft','Console': 'Xbox One'},
              {'Empresa': 'Microsoft','Console': 'Xbox Series X'},
              {'Empresa': 'Sony','Console': 'Playstation 4'},
              {'Empresa': 'Sony','Console': 'Playstation 5'},
              {'Empresa': 'Nintendo','Console': 'Nintendo 64'},
              {'Empresa': 'Nintendo','Console': 'Gameboy'},
              {'Empresa': 'Microsoft','Console': 'Xbox Series S'},]

# Ordenando os consoles por empresa para evitar conflitos com o 'groupby', de forma que ele adicione todos os consoles,
# Independente da ordem alfabética
videogames.sort(key=lambda item: item['Empresa'])
videogames_agrupados = {}

# Neste looping o código agrupa o item console por empresa
for key, value in groupby(videogames, key=lambda item: item['Empresa']):
    videogames_agrupados[key] = list(value)

for empresa, consoles in videogames_agrupados.items():
    print(f'{"=-" * 4}{empresa}{"=-" * 4}')
    for console in consoles:
        print(f'{console["Console"]}')