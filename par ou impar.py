print('O número é par ou impar?')
def parimpar(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
resultado = parimpar(int(input('Digite o seu número: ')))
if resultado == True:
    print('O seu número é par!')

else:
    print('O seu número é impar!')