# Ex4. Calculadora de Combustível de Viagem

import time

print ("Olá companheiro(a)!")
time.sleep (1)

distancia_total = float(input("Digite por gentileza a distância total planejada para a viagem em quilomêtros: "))
print ("Perfeito!")
time.sleep (1)

consumo_medio = float(input("Agora, por favor digite o consumo médio do seu veículo em quilometros por litro: "))
preço_atual_combustivel = float(input("Por último, digite o preço atual do combustivel em reais:"))
time.sleep (1)

print(f"A quantidade de litros necessários para a viagem é de {distancia_total/consumo_medio:.2f} litros.")
time.sleep (1)

print(f"O custo total da viagem é de R$ {distancia_total/consumo_medio * preço_atual_combustivel:.2f}.")
valor_total_viagem = distancia_total/consumo_medio * preço_atual_combustivel

input("Deseja saber quanto cada passageiro deve pagar? Digite qualquer tecla para continuar.")
time.sleep (1)

print("Maravilha!")
time.sleep(0.5)

num_passageiros = int(input("Digite o número de passageiros que irão viajar: "))
time.sleep (1)

print("Obrigado! Calculando o valor que cada passageiro deverá pagar...")
time.sleep (1)

print (f"Cada passageiro deverá pagar em R$ {valor_total_viagem/num_passageiros:.2f}.")