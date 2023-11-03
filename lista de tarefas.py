lista = []
lista_desfazer = []
lista_refazer = []
print('Bem vindo, faça a sua lista de tarefas!')
while True:
    print('')
    try:
        funcoes = int(input('[0] Adicionar\n'
                            '[1] Defazer\n'
                            '[2] Refazer\n'
                            '[3] Visualizar\n'
                            'Digite a função desejada: '))
        if funcoes == 0:
            tarefa = str(input('Adicione uma tarefa a sua lista: ')).strip().title()
            lista.append(tarefa)
        
        elif funcoes == 1:
            lista_refazer.append(lista[-1])
            lista.pop()
        
        elif funcoes == 2:
            lista.append(lista_refazer[-1])
            del(lista_refazer[-1])
        
        elif funcoes == 3:
            print('=-=-LISTA DE TAREFAS-=-=')
            print(*lista, sep='\n')
        else:
            raise ValueError
    except ValueError:
        print('ERRO, VALOR FORA DO ESPERADO!')