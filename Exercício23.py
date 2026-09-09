# 10. Cálculo de Desconto (Aritmética e Decisão)
# Peça o valor de um produto (real).
# Se o produto custar mais de R$ 100.00, aplique um desconto de 10% e mostre o preço final.
# Senão, exiba o preço original.

import time

print("Bem-vindo ao programa de desconto!")
time.sleep(0.5)

produto = float(input("Digite o valor do produto: R$"))

if produto > 100:
    desconto = produto * 0.10  # CALCULA 10% DE DESCONTO
    produto_final = produto - desconto  # SUBTRAI O DESCONTO DO PREÇO ORIGINAL
    print(f"O valor do produto com desconto é: R${produto_final:.2f}")
    time.sleep(1)
else:
    time.sleep(1)
    print(f"O valor do produto é: R${produto:.2f}")

print("Obrigado por participar do programa! :)")
