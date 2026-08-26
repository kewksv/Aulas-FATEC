# 3. Desenvolva um programa que solicite o nome de um produto,
# seu preço unitário e a quantidade em estoque.
# Calcule o valor total em estoque e exiba uma frase informativa
# utilizando f-strings.
import time
produto = input("Digite o nome do produto: ")
preço = (input(f"Digite o preço da {produto} por unidade: "))
estoque = (input("Digite a quantidade no estoque: "))
valor_total_em_estoque = (float(preço)) * (int(estoque))
time.sleep (1.5)
print(f"O valor total em estoque é de: {valor_total_em_estoque:2f} ")
