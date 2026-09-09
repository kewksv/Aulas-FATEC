# 8. O Alerta da Estufa de Biologia (Condicionais if, elif e else)
# O laboratório de ciências possui uma estufa automatizada para plantas tropicais sensíveis.
# O sistema de monitoramento precisa ler a temperatura atual e disparar um alerta visual na tela
# para que os alunos saibam se as condições físicas do ambiente estão adequadas.
# I. Temperaturas abaixo de 15.0 °C são classificadas como "Muito Frio".
# II. Temperaturas entre 15.0 °C e 25.0 °C (inclusive) são classificadas como "Temperatura Ideal".
# III. Temperaturas acima de 25.0 °C são classificadas como "Muito Quente".
# Escreva o programa em Python que solicite a temperatura medida (float).
# Usando a estrutura de decisão, exiba na tela o status correspondente para alertar o operador da estufa.

import time

print("Seja bem vindo ao alerta da estufa de biologia!")
time.sleep(1)

temperatura = float(input("Olá aluno! Digite a temperatura apresentada no termômetro (em celsius): "))

if temperatura < 15.0:  # VERIFICA SE ESTÁ ABAIXO DA TEMPERATURA IDEAL
    print("Muito Frio")
    time.sleep(1)
elif temperatura <= 25.0:  # SE CHEGOU AQUI, ESTÁ ENTRE 15 E 25
    print("Temperatura Ideal")
    time.sleep(1)
else:
    print("Muito Quente")
    time.sleep(1)

print("Obrigado por utilizar!")
