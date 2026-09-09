import time
print ("Seja bem vindo ao teste de tobogã!")
time.sleep (0.5)
nome = input("Escreva seu nome por gentileza: ")
idade = (int(input("Agora, a sua idade: ")))
altura = (input(f"Agora {nome} pra finalizar, a sua altura: ")).replace(",", ".")
if idade >= 12 and float(altura) >= 1.60:
    time.sleep (1)
    print("Acesso liberado!")
else:
 print("Acesso negado")
print("Obrigado por participar do programa! :)")