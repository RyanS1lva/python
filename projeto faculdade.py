# Projeto inicial da atividade extensionista
from time import sleep
print(f'{"=-" * 4}Bem vindo ao DrawMath⭐🚀!{"=-" * 4}')
print('Instruções para o jogo:\n'
      '-Você pode consultar no seu material didático para responder as perguntas.'
      '\n-Responda as perguntas conforme recomendado pelo sistema para evitar erros.'
      '\n-Seja competitivo mas compreendendo que errar é parte do aprendizado.'
      '\n-Caso tenha dificuldades de passar alguma fase, converse com o seu tutor.\n'
      'Tenha um ótimo jogo e multiplique o seus conhecimentos, \033[34mnem mesmo o céu é o limite!\033[0m')
print()


# O jogo fica dentro de um looping, permitindo encerrar o programa quando desejado 
# e controlar as condicionais sem encerrar o programa fora do tempo previsto.
while True:
    iniciar_jogo = int(input('Digite 0 para iniciar o jogo ou 1 para sair do programa: '))
    if iniciar_jogo == 0:
        print()
        print()
        dados_alunos = {}
        nome_aluno = str(input('Digite o seu nome astronauta: ')).lower().strip()
        dados_alunos['Nome'] = nome_aluno

        questao_1 = f'Astronauta {nome_aluno}, em ordem decrescente (maior para o menor), qual a ordem de prioridade dos elementos matemáticos:\n(A) 1° Multiplicação e Divisão, 2° Soma e Subtração\n(B) 1° Soma e subtração, 2° Multiplicação e divisão\n(C) 1° Multiplicação, 2° Divisão, 3° Soma, 4° Subtração\nEscreva a letra da alternativa correta: '
        nivel_1 = {'Questão 1': questao_1}

        for key, value in nivel_1.items():
            print()
            quest = input(value)



        print(dados_alunos)
    elif iniciar_jogo == 1:
        print('Saindo do programa...')
        sleep(1)
        print('Até breve astronauta :D')
        break
    else:
        print('Função inválida')






