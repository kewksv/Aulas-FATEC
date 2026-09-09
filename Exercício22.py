# 9. Área do Círculo (Potência **)
# Peça o raio (número real) de um círculo.
# Calcule e exiba a área usando a fórmula:
# Área = 3.14 * raio²
# Uso obrigatório do operador de potência **.

import time

print("Bem-vindo ao calculador de área!")
raio = float(input("Digite o valor do raio: "))

potencia = raio ** 2  # ELEVA O RAIO AO QUADRADO
area = 3.14 * potencia  # CALCULA A ÁREA DO CÍRCULO

print(f"A área determinada é de: {area}")
print("Obrigado por participar do programa!")
