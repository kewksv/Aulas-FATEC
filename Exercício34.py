#Solicite um número inteiro positivo e utilize while para mostrar os números de 1 até o valor informado.
#
#Considere que o usuário digitará um número positivo. Se digitar 4, mostre 1, 2, 3 e 4.

import time

numero = int(input("Digite um número inteiro: ")) 

contador = 1

while contador <= numero:

    print(contador)
    time.sleep(0.5)
    contador = contador + 1

print ("Contagem encerrada!")
