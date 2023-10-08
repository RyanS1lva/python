from time import sleep
checklist = []
xp = 0
nivel = 0
tarefas_concluidas = 0
def visualizar_tarefas(lista):
    id_tarefa = 0
    print(f'{"=-" * 3}CHECKLIST{"=-" * 3}')
    for tarefa in lista:
        id_tarefa += 1
        print(f'{id_tarefa} - {tarefa}')

def verifica_nivel(xp, nivel):
    print('')
    if xp == 20:
        nivel = 1
        print(f'Parabéns, você está no nível {nivel}!\nContinue cumprindo suas tarefas para subir de nível.')
    
    elif xp == 50:
        nivel = 2
        print(f'Parabéns, você está no nível {nivel}!\nContinue cumprindo suas tarefas para subir de nível.')
    
    elif xp == 90:
        nivel = 3
        print(f'Parabéns, você está no nível {nivel}!\nContinue cumprindo suas tarefas para subir de nível.')
    
    elif xp == 100:
        nivel = 4
        print(f'Parabéns, você está no nível {nivel}!\nContinue cumprindo suas tarefas para subir de nível.')
    
    return xp, nivel
    

print('Bem vindo ao seu checklist!')
while True:
    print('')
    try:
        funcoes = int(input('[0] Adicionar uma tarefa\n'
                            '[1] Visualizar o checklist\n'
                            '[2] Marcar uma tarefa como concluida\n'
                            '[3] Remover uma tarefa\n'
                            '[4] Sair do programa\n'
                            'Digite a função desejada: '))
    except ValueError:
        print('ERRO, tente digitar o número da função!')
    print('')
    if funcoes == 0:
        tarefa = str(input('Digite uma tarefa: '))
        checklist.append(tarefa)

    elif funcoes == 1:
        visualizar_tarefas(checklist)

    elif funcoes == 2:
        visualizar_tarefas(checklist)
        print('')
        tarefa_concluida = int(input('Digite o número da tarefa concluida: '))
        tarefa_concluida = tarefa_concluida - 1
        del[checklist[tarefa_concluida]]
        tarefas_concluidas += 1
        xp += 10
        xp, nivel = verifica_nivel(xp, nivel)
 

    elif funcoes == 3:
        visualizar_tarefas(checklist)
        print('')
        tarefa_removida = int(input('Digite o número da tarefa que deseja remover: '))
        tarefa_removida = tarefa_removida - 1
        del[checklist[tarefa_removida]]

    elif funcoes == 4:
        print('Finalizando...')
        sleep(1)
        print(f'Você concluiu {tarefas_concluidas} tarefas e chegou até o nível {nivel}!')
        sleep(1)
        print('Volte sempre!')
        break

    else:
        print('Função não encontrada!')
        continue

    


