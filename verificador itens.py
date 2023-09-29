lista = [21, 'Ryan', True, 17.5, False]


for item in lista:
    if isinstance(item, str):
        print(f'Este item é uma string: {item}')

for item in lista:
    if isinstance(item, int):
        print(f'Este item é um inteiro {item}')

for item in lista:
    if isinstance(item, bool):
        print(f'Este item é um boolean: {item}')
    
for item in lista:
    if isinstance(item, float):
        print(f'Este item é um float: {item}')