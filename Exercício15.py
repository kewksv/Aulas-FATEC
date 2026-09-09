# 2. O Mensageiro de Boas-Vindas (Concatenação)
# Escreva um programa em Python que solicite ao usuário o seu nome e a sua idade.
# O programa deve exibir na tela a mensagem:
# "Olá (Nome), você tem (Idade) anos!".
# Resolver este exercício usando concatenação (+), e realizar a conversão usando str().

import time

print("Seja bem vindo ao programa!")
time.sleep(0.5)

nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))

mensagem = "Olá " + nome + ", você tem " + str(idade) + " anos!"  # CONCATENA AS INFORMAÇÕES
time.sleep(0.5)
print(mensagem)

print("Obrigado por participar do programa! :)")
