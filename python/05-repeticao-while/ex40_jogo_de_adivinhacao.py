#Escreva um programa em Python que tenha o número 7 como número secreto.
#
#Solicite ao usuário um palpite inteiro e utilize while para continuar pedindo palpites até que ele acerte. 
#
#Dentro do laço, utilize if/else para mostrar uma dica:
#
#• Se o palpite for menor que o número secreto, exiba “Tente um número maior!”.
#
#• Caso contrário, exiba “Tente um número menor!”. Quando o usuário acertar, exiba “Parabéns! Você acertou!”. 

print("Jogo de adivinhação!")

numero_secreto = 7

palpite = 0

while palpite != numero_secreto:

    palpite = int(input("Digite um palpite inteiro: "))

    if palpite < numero_secreto:

        print("Tente um número maior!")

    else:

        print("Tente um número menor!")
        
print("Parabéns! Você acertou!")
