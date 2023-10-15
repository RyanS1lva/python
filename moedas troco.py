moeda_25 = 0.25

moeda_10 = 0.10

moeda_5 = 0.05

moeda_1 = 0.01

uso_25 = 0
uso_10 = 0
uso_5 = 0
uso_1 = 0

# O usuário deve informar o troco a ser dado para que o programa calcule a melhor maneira de devolver este troco,
# Utilizando uma ordem de prioridade com as moedas de maior valor

troco = float(input('Digite o troco devido: '))

while True:
    if troco != 0:
        resto = troco % moeda_25
        uso_25 = troco // moeda_25
        troco = troco - (uso_25 * moeda_25)


        if resto > 0:
            resto = troco % moeda_10
            uso_10 = troco // moeda_10
            troco = troco - (uso_10 * moeda_10)
        
        if resto > 0:
            resto = troco % moeda_5
            uso_5 = troco // moeda_5
            troco = troco - (uso_5 * moeda_5)
        
        if resto > 0:
            resto = troco % moeda_1
            uso_1 = troco // moeda_1
            troco = troco - (uso_1 * moeda_1)

        break

print('')
print(f'Podem ser utilizadas:\n{uso_25} moedas de $0.25\n{uso_10} moedas de $0.10\n{uso_5} moedas de $0.05\n{uso_1} moedas de $0.01')

