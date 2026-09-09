import time
print ("Bem vindo a paneira do vôlei!")
time.sleep (0.5)
nome = input("Informe seu nome por gentileza: ")
altura =  input("Digite a sua altura (em metros): ").replace(",", ".")
if (float(altura)) >= 1.70:
    time.sleep (1)
    print(f"{nome} liberado para jogar vôlei!")
else:
    time.sleep (1)
    print(f"{nome} não liberado para jogar vôlei!")
print("Obrigado por participar do programa! :)")