# 5. Peneira do Vôlei (Condicional Simples if/else)
# O treinador do time de vôlei da escola estipulou que, para participar da seleção masculina/feminina,
# o candidato deve medir pelo menos 1.70m de altura.
# Escreva um programa que peça a altura do aluno e exiba se ele está
# "Aprovado para o teste" ou "Classificado para outras modalidades".
# Uso do operador relacional de maior ou igual (>=) e a conversão da entrada para número real (float).

import time

print("Bem vindo a peneira do vôlei!")
time.sleep(0.5)

nome = input("Informe seu nome por gentileza: ")
altura = input("Digite a sua altura (em metros): ").replace(",", ".")

if float(altura) >= 1.70:  # VERIFICA SE A ALTURA É SUFICIENTE
    time.sleep(1)
    print(f"{nome}, Aprovado para o teste!")
else:
    time.sleep(1)
    print(f"{nome}, Classificado para outras modalidades!")

print("Obrigado por participar do programa! :)")
