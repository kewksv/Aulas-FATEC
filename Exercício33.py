#Escreva um programa que utilize while para mostrar os números de 10 até 1, em ordem decrescente. Depois da repetição, exiba “Contagem encerrada!”. 

import time

contador = 10

while contador >= 0:

    print(contador)
    time.sleep(0.5)
    contador = contador - 1

print("Contagem encerrada!")
