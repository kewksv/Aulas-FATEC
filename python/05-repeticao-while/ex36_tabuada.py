#Solicite um número inteiro e mostre sua tabuada de 1 a 10, utilizando while e f-string. 
#
# Exemplo: para o número 3, mostre de “3 x 1 = 3” até “3 x 10 = 30”
#
#O contador representa o multiplicador. Calcule numero * contador a cada repetição.

import time

numero = int(input("Digite um número inteiro: ")) 

contador = 1

while contador <= 10:

    print(f"{numero} x {contador} = {numero * contador}")
    time.sleep(0.5)
    contador = contador + 1

print ("Contagem encerrada!")
