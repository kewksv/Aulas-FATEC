#Escreva um programa em Python que utilize while para mostrar os números de 1 a 20, um por linha. 

import time

contador = 1 

while contador <= 20:

    print(contador)
    time.sleep(0.5)
    contador = contador + 1

print ("Contagem encerrada!")
