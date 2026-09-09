# 4. O Teste do Tobogã (Operador Lógico or)
# No parque aquático da escola, as regras de segurança para o tobogã gigante são flexíveis para garantir a diversão com segurança.
# Para ter o acesso liberado, o aluno precisa cumprir pelo menos um dos seguintes requisitos:
# I. II. Ter idade maior ou igual a 12 anos or altura maior ou igual a 1.60 m.
# Escreva o programa em Python que receba o nome, a idade e a altura do aluno,
# faça o teste lógico correto e exiba se o acesso foi "Liberado" ou "Bloqueado".

import time

print("Seja bem vindo ao teste de tobogã!")
time.sleep(0.5)

nome = input("Escreva seu nome por gentileza: ")
idade = int(input("Agora, a sua idade: "))
altura = input(f"Agora {nome} pra finalizar, a sua altura: ").replace(",", ".")

if idade >= 12 or float(altura) >= 1.60:  # PELO MENOS UMA DAS CONDIÇÕES PRECISA SER VERDADEIRA
    time.sleep(1)
    print(f"{nome}, acesso Liberado!")
else:
    time.sleep(1)
    print(f"{nome}, acesso Bloqueado!")

print("Obrigado por participar do programa! :)")
