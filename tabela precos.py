from time import sleep
print(f'{"-=" * 5}TABELA DE PREÇOS{"-=" * 5}')
def exibe_tabela():
    for k, v in produtos.items():
        print(f' {k:<15}  {"." * 9}R${v:>5.2f}')
#Tabela pré-configurada
produtos = {'Arroz': 10,
                'Feijão': 11,
                'Chocolate': 6.80,
                'Pipoca': 6,
                'Refrigerante': 10,
                'Massa': 6.5,
                'Pizza': 14,}
while True:
    funcao = str(input('Adicionar produto[A]\n'
                       'Remover produto[R]\n'
                       'Visualizar tabela[V]\n'
                       'Sair do programa[S]\n'
                       'Digite a função desejada: ')).upper()
    if funcao == 'V':
        exibe_tabela()
    elif funcao == 'A':
        nome_produto = str(input('Adicione o nome do produto: ')).title()
        valor_produto = float(input('Adicione o valor do produto: '))
        produtos[nome_produto] = valor_produto
    elif funcao == 'R':
        produto_removido = str(input('Digite o nome do produto que você deseja remover: ')).title()
        produtos.pop(produto_removido)
    elif funcao == 'S':
        print('Finalizando o programa...')
        sleep(1)
        print('Volte sempre!')
        break

