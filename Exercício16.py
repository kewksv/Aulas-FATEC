# 3. Triagem de Exame (Operador Lógico and)
# Em hospitais, antes de aplicar certos tipos de medicamentos de contraste, é necessário fazer uma triagem de segurança.
# Escreva um programa que peça o nome, a idade (Inteiro) e o peso (float) de um paciente.
# O paciente só estará liberado para o exame se atender a duas condições simultaneamente:
# I. II. III. Ter idade maior ou igual a 18 anos and peso maior ou igual a 50.0 kg.
# Se atender aos requisitos, exiba: "Paciente {Nome} liberado para o exame de contraste."
# Senão, exiba: "Alerta! Paciente {Nome} necessita de avaliação médica especial."

import time

print("Seja bem vindo ao programa de triagem!")
time.sleep(0.5)

nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade por gentileza: "))
peso = float(input("Digite o seu peso em kg: "))

time.sleep(0.5)
print(f"Obrigado {nome}! Vamos prosseguir com a aplicação.")
time.sleep(0.5)

if idade >= 18 and peso >= 50:  # VERIFICA AS DUAS CONDIÇÕES AO MESMO TEMPO
    time.sleep(1)
    print(f"Paciente {nome} liberado para o exame de contraste.")
else:
    time.sleep(1)
    print(f"Alerta! Paciente {nome} necessita de avaliação médica especial.")

print("Obrigado por participar do programa!")
