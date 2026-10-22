#Escreva um programa em Python que solicite um número inteiro e informe se ele é primo ou não, utilizando while e if/else.
#
#Um número primo é um inteiro maior que 1 que possui exatamente dois divisores positivos: 1 e ele mesmo.

contador = 1

contador_de_divisores = 0

numero = int(input("Digite um número inteiro: "))

while contador <= numero:

    if numero % contador == 0:
        contador_de_divisores = contador_de_divisores + 1
    contador = contador + 1

if contador_de_divisores == 2:

    print ("É primo")

else: 
    
    print("Não é primo")
