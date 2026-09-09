import time
print("Seja bem vindo ao programa de triagem!")
time.sleep(0.5)
nome = input("Digite seu nome: ")
idade = (int(input("Digite a sua idade por gentileza: ")))
peso = (float(input("Digite o seu peso em kg: ")))
time.sleep(0.5)
print (f"Obrigado {nome}! Vamos prosseguir com a aplicação.")
time.sleep(0.5)
if idade >=18 and (float(peso) >= 50):
    time.sleep (1)
    print(f"{nome} liberado para o exame de contraste")
else:
    time.sleep(1)
print("Obrigado por participar do programa!")