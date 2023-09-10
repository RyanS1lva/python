from time import sleep
print('Faça o seu checklist!')
checklist = []
tarefas_concluidas = []
contador = 0
def adicionar_item():
    while True:
        print('\nPara parar de adicionar tarefas digite "quit"')
        tarefa_adicionada = str(input('Adicione uma tarefa: ')).lower().strip()
        tarefa_semespaco = tarefa_adicionada.replace(' ', '')
        if tarefa_semespaco == 'quit':
            break
        elif tarefa_semespaco.isalpha():
            checklist.append(tarefa_adicionada)
            print('Adicionando tarefa...')
            sleep(1)
            print('Tarefa adicionada!')
        else:
            print('Digite uma tarefa válida!')
            continue

adicionar_item()
def mostra_lista():
    print('\nSuas tarefas são:')
    for itens in checklist:
        print(itens)
def mostra_concluidos():
    print('\nSuas tarefas concluídas são:')
    for itens in tarefas_concluidas:
        print(itens)
mostra_lista()
while True:
    funcao = str(input('\nO que você deseja fazer?\n'
                    'Adicionar tarefa na lista[A]\n'
                    'Remover tarefa da lista[R]\n'
                    'Marcar tarefa como concluída[C]\n'
                    'Sair do programa[S]\n'
                    'Digite a função desejada: ')).lower().strip()
    if funcao == 'a':
        adicionar_item()
        mostra_lista()
    elif funcao == 'r':
        print('')
        for itens in checklist:
            print(f'{itens} [{contador}]')
            contador += 1
        remover_item = int(input('Digite o número da tarefa que você gostaria de remover: '))
        print('Removendo tarefa...')
        sleep(1)
        print('Tarefa removida!')
        del(checklist[remover_item])
        contador = 0
        mostra_lista()
    elif funcao == 'c':
        print('')
        for itens in checklist:
            print(f'{itens} [{contador}]')
            contador += 1
        marcar_concluida = int(input('Digite o número da tarefa que você concluiu: '))
        print('Adicionando tarefa nos concluidos...')
        sleep(1)
        print('Tarefa concluida!')
        tarefas_concluidas.append(checklist[marcar_concluida])
        del(checklist[marcar_concluida])
        contador = 0
        mostra_lista()
        mostra_concluidos()
    elif funcao == 's':
        print('saindo do programa...')
        sleep(1)
        print('---volte sempre!---')
        break
    


      

