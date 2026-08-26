# Exercícios de Fixação
# Ex4. Calculadora de Combustível de Viagem
# Aula 2 LAB
#
# Três amigos vão fazer uma viagem de carro e querem
# dividir igualmente o custo do combustível.
#
# Escreva um programa que ajude a calcular os custos.
#
# Seu programa deve solicitar:
#
# 1. A distância total planejada para a viagem em
# quilômetros (ex: 350.5)
#
# 2. O consumo médio de combustível do carro
# (quantos km o carro faz por litro, ex: 12.0)
#
# 3. O preço atual do litro do combustível (ex: 5.89)
#
# O programa deve calcular:
#
# 1. A quantidade de litros necessários para a viagem
# (distancia / consumo).
#
# 2. O custo total do combustível
# (litros_necessarios * preco_combustivel).
#
# 3. Quanto cada um dos 3 amigos deverá pagar
# (custo_total / 3).
#
# 4. Ao final, exiba na tela usando f-strings:
# O custo total do combustível formatado em R$ com
# 2 casas decimais.
#
# O valor que cada amigo deve pagar também em R$ com
# 2 casas decimais.

import time

print("Olá companheiro(a)!")
time.sleep(1)

distancia_total = float(input("Digite por gentileza a distância total planejada para a viagem em quilômetros: "))

print("Perfeito!")
time.sleep(1)

consumo_medio = float(input("Agora, por favor digite o consumo médio do seu veículo em quilômetros por litro: "))

preço_atual_combustivel = float(input("Por último, digite o preço atual do combustível em reais: "))

time.sleep(1)

print(f"A quantidade de litros necessários para a viagem é de {distancia_total / consumo_medio:.2f} litros.") # CALCULA QUANTOS LITROS SERÃO NECESSÁRIOS

time.sleep(1)

print(f"O custo total da viagem é de R$ {distancia_total / consumo_medio * preço_atual_combustivel:.2f}.") # CALCULA O CUSTO TOTAL

valor_total_viagem = distancia_total / consumo_medio * preço_atual_combustivel # ARMAZENA O CUSTO TOTAL

input("Deseja saber quanto cada passageiro deve pagar? Digite qualquer tecla para continuar.")

time.sleep(1)

print("Maravilha!")
time.sleep(0.5)

num_passageiros = int(input("Digite o número de passageiros que irão viajar: "))

time.sleep(1)

print("Obrigado! Calculando o valor que cada passageiro deverá pagar...")

time.sleep(1)

print(f"Cada passageiro deverá pagar em R$ {valor_total_viagem / num_passageiros:.2f}.") # DIVIDE O CUSTO ENTRE OS PASSAGEIROS
