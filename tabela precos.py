print(f'{"-=" * 5}TABELA DE PREÇOS{"-=" * 5}')
produtos = {'Arroz': 10,
            'Feijão': 11,
            'Chocolate': 6.80,
            'Pipoca': 6,
            'Refrigerante': 10,
            'Massa': 6.5,
            'Pizza': 14,
            'Picanha': 120}

for k, v in produtos.items():
    print(f' {k:<15} {"." * 9} R${v:>5.2f}')


