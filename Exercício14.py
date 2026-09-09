# 1. O Dobro da Idade (Operadores Aritméticos e f-String)
# Crie um programa que peça a idade de um aluno.
# Em seguida, calcule e exiba o dobro dessa idade.

import time

print("Seja bem vindo ao programa!")
time.sleep(0.5)

nome = input("Digite seu nome: ")
time.sleep(0.3)
print(f"Obrigado {nome}! Vamos prosseguir com a aplicação.")
time.sleep(0.3)

idade = input("Digite a sua idade por gentileza: ")
resposta = input(f"{nome} deseja descobrir o dobro da sua idade? (responda sim ou não): ")

if resposta == "sim":
    idade = int(idade)
    dobro_idade = idade * 2  # CALCULA O DOBRO DA IDADE
    print(f"O dobro da sua idade é: {dobro_idade}")
else:
    print("Ok, obrigado por participar do programa!")
