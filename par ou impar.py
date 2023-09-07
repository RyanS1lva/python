print('O número é par ou impar?')
def parimpar(num):
    if num % 2 == 0:
        return f"O número {num} é par!"
    else:
        return f"O número {num} é impar!"
    
resultado = parimpar(int(input('Digite o seu número: ')))
print(resultado)
