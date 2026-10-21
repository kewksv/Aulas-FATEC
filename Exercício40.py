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