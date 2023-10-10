import random

alunos = []

# Adiciona os dados do aluno dentro de um dicionário,
# que por sua vez é acrescentado em uma lista chamada "alunos".
def adiciona_aluno(nome, identificacao_aluno, xp, nivel):
    aluno = {
        'Nome': nome,
        'Id': identificacao_aluno,
        'Xp': xp,
        'Nível': nivel
    }
    alunos.append(aluno)

# Função responsável por gerar as questões do aluno,
# Bem como por retornar os valores do seu xp e nível de acordo com suas respostas.
def gerador_questoes(nivel, xp):
        if nivel == 1:
            v1 = random.randint(2, 10)
            v2 = random.randint(1, 10)
            
            while True:
                if (v2 == v1):
                    v2 = random.randint(1, 10)
                    continue
                else:
                    break
                    
            print("Qual o resultado da seguinte operação?")
            print("{} + {} = ?".format(v1, v2))
            try:
                resultado = int(input('>>> '))
                if resultado == (v1 + v2):
                    print('Resposta correta!\n+10 XP')
                    xp += 10
                else:
                    print('Resposta incorreta!')
            except ValueError:
                print('ERRO, valores inseridos não conferem com o esperado!')

        
            while True:    
                if (v2 > v1) or (v2 == v1):
                    v2 = random.randint(1, 10)
                    continue
                else:
                    break
            print("{} - {} = ?".format(v1, v2))
            try:
                resultado = int(input('>>> '))
                if resultado == (v1 - v2):
                    print('Resposta correta!\n+10 XP')
                    xp += 10
                else:
                    print('Resposta incorreta!')
            except ValueError:
                print('ERRO, valores inseridos não conferem com o esperado!')  
                
                if xp == 20:
                    nivel = 2
        
    
        return nivel, xp


# Loop principal, coleta o nome do aluno e víncula a ele os dados iniciais do jogo.
while True:
    nome = str(input('Digite o seu nome: '))
    id_aluno = len(alunos) + 1
    print('')
    # Valores iniciais
    nivel = 1
    xp = 0
    nivel, xp = gerador_questoes(nivel, xp)
    adiciona_aluno(nome, id_aluno, xp, nivel)

    # Fazendo com que os alunos fiquem ordenados dentro da lista de acordo com o seu XP (ORDEM DECRESCENTE)
    alunos.sort(key=lambda item: item['Xp'], reverse=True)
    
    posicao = 0
    print(f'{"=-" * 4}RANKING DE ALUNOS{"-=" * 4}')
    for aluno in alunos:
        posicao += 1
        print(f'{posicao}° {aluno}')

