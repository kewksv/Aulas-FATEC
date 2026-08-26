# Exercícios de Fixação
# Ex3. Validador de Meta de Vendas
# Aula 2 LAB
#
# Uma loja de eletrônicos estabeleceu uma meta de vendas
# diária de R$ 1.500,00.
#
# Desenvolva um programa que:
#
# 1. Peça ao vendedor para digitar o valor total que ele
# vendeu hoje.
#
# 2. Converta a entrada para float.
#
# 3. Crie uma variável do tipo bool chamada meta_atingida
# que armazene se o valor vendido foi maior ou igual à
# meta de 1500.00.
#
# 4. Exiba o resultado formatando a saída com f-strings:
# "Meta diária alcançada?"

META_VENDAS_DIARIAS = 1500

print("Olá vendedor(a)! Vamos calcular o seu desempenho de vendas hoje.")

vendas_hoje = float(input("Digite o valor total de vendas realizadas hoje: "))

meta_atingida = vendas_hoje >= META_VENDAS_DIARIAS # VERIFICA SE A META FOI ATINGIDA

print(f"Meta diária alcançada? {meta_atingida}")
