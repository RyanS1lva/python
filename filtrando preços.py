print('Bem vindo a fruteira Sol da Manhã!')
print()
produtos = [
    {'Produto': 'Leite (Litro)', 'Preço': 6.75},
    {'Produto': 'Pão (Fatia)', 'Preço': 7.0},
    {'Produto': 'Ovos (Dúzia)', 'Preço': 6.50},
    {'Produto': 'Maçãs (Por KG)', 'Preço': 4.99},
    {'Produto': 'Arroz (Saco de 1 KG)', 'Preço': 8.0},
    {'Produto': 'Cereal (Caixa)', 'Preço': 10.00},
    {'Produto': 'Bananas (Por KG)', 'Preço': 3.99},
    {'Produto': 'Frango (Kg)', 'Preço': 12.50},
    {'Produto': 'Carne Moída (Kg)', 'Preço': 9.99},
    {'Produto': 'Peixe (Kg)', 'Preço': 14.75},
    {'Produto': 'Cenouras (Por KG)', 'Preço': 2.49},
    {'Produto': 'Batatas (Por KG)', 'Preço': 1.99},
    {'Produto': 'Tomates (Por KG)', 'Preço': 5.50},
    {'Produto': 'Cebolas (Por KG)', 'Preço': 3.25},
    {'Produto': 'Pimentão (Unidade)', 'Preço': 1.75},
    {'Produto': 'Alho (Por KG)', 'Preço': 8.99},
    {'Produto': 'Café (Pacote de 250g)', 'Preço': 9.25},
    {'Produto': 'Chá (Caixa)', 'Preço': 3.99},
    {'Produto': 'Açúcar (Kg)', 'Preço': 4.49},
    {'Produto': 'Sal (Pacote de 1Kg)', 'Preço': 2.50},
    {'Produto': 'Azeite (Garrafa 500ml)', 'Preço': 7.99},
    {'Produto': 'Vinagre (Garrafa 250ml)', 'Preço': 2.25},
    {'Produto': 'Massa (Pacote)', 'Preço': 1.99},
    {'Produto': 'Sopa enlatada', 'Preço': 3.75},
    {'Produto': 'Molho de Tomate (Frasco)', 'Preço': 2.99},
    {'Produto': 'Queijo (250g)', 'Preço': 5.99},
    {'Produto': 'Iogurte (500g)', 'Preço': 3.49},
    {'Produto': 'Manteiga (250g)', 'Preço': 4.99},
    {'Produto': 'Oleo de Cozinha (Garrafa 1L)', 'Preço': 5.25},
    {'Produto': 'Biscoitos (Pacote)', 'Preço': 3.29},
    {'Produto': 'Chocolate (Barra)', 'Preço': 2.99},
    {'Produto': 'Refrigerante (Lata)', 'Preço': 1.99},
    {'Produto': 'Água Mineral (Garrafa 500ml)', 'Preço': 0.99},
    {'Produto': 'Sabonete (Unidade)', 'Preço': 1.50},
    {'Produto': 'Papel Higiênico (Rolo)', 'Preço': 1.75},
    {'Produto': 'Escova de Dentes', 'Preço': 2.50},
    {'Produto': 'Shampoo (Frasco)', 'Preço': 5.99},
    {'Produto': 'Condicionador (Frasco)', 'Preço': 5.99},
    {'Produto': 'Detergente (Frasco)', 'Preço': 2.49},
    {'Produto': 'Esponja de Cozinha', 'Preço': 1.99},
    {'Produto': 'Papel Toalha (Rolo)', 'Preço': 2.25},
    {'Produto': 'Lâmpada (Unidade)', 'Preço': 3.99},
    {'Produto': 'Pilhas (Pacote)', 'Preço': 4.99},
    {'Produto': 'Fraldas Descartáveis (Pacote)', 'Preço': 8.50},
    {'Produto': 'Ração para Cães (Saco 2Kg)', 'Preço': 9.99},
    {'Produto': 'Ração para Gatos (Saco 1Kg)', 'Preço': 7.99},
    {'Produto': 'Sabão em Pó (Caixa 1Kg)', 'Preço': 6.49}
]

print('Você pode filtar produtos de determinado valor.')
preco_definido = float(input('Digite até o valor desejado $: '))

produtos_filtrados = filter(
    lambda item: item["Preço"] <= preco_definido,
    produtos
)

print()
print(f'Produtos até ${preco_definido}:')
print(*produtos_filtrados, sep='\n')