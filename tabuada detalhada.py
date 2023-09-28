# import os seguido de os.system('cls) pode não funcionar em alguns sistemas operacionais
import os
from time import sleep
numero = 0
for numeros_tabuada in range(1, 11):
    print()
    numero += 1
    if numero > 1:
        sleep(2)
        os.system('cls')
    print(f'{"-=" * 2}Tabuada do número {numero}{"-=" * 2}')
    print()
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f'{numero:>9} X {multiplicador} = {resultado}')
        sleep(0.25)









    
    
