# Exercícios de Fixação
# Ex2. Sensor de Temperatura de Servidor
# Aula 2 LAB
#
# Em salas de servidores, a temperatura não pode passar
# de 40°C. Vamos criar o sistema lógico de um sensor.
#
# Desenvolva um programa que:
#
# 1. Solicite ao usuário que digite a temperatura atual
# medida pelo sensor (ex: 38.5).
#
# 2. Converta essa entrada para número decimal (float).
#
# 3. Crie uma variável booleana chamada alerta_ativo.
# Ela deve receber True se a temperatura lida for maior
# que 40.0, e False caso contrário.
#
# 4. Exiba o status do alerta no terminal usando uma
# f-string:
# "Alerta de superaquecimento ativo:"

temperatura = input("Digite a temperatura atual em Celsius: ")

alerta_ativo = float(temperatura) > 40.0 # VERIFICA SE PASSOU DE 40°C

print(f"Alerta de superaquecimento ativo? {alerta_ativo}")
