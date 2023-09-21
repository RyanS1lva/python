lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

ordem_nome = sorted(lista, key=lambda item: item['nome'])
ordem_sobrenome = sorted(lista, key=lambda item: item['sobrenome'])
print('-=-=Ordenando por nome=-=-')
for nome in ordem_nome:
    print(nome) 
print()
print('-=-=Ordenando por sobrenome=-=-')
for sobrenome in ordem_sobrenome:
    print(sobrenome)