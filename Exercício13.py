# Exercícios de Fixação
# Ex6. Validador de Desconto no Cinema
# Aula 2 LAB
#
# Um cinema local concede o benefício da meia-entrada
# para clientes que cumprem pelo menos um dos seguintes
# critérios:
#
# 1. Ter 60 anos ou mais.
#
# 2. Ser estudante (identificado se o usuário digitar
# exatamente a letra "S").
#
# Desenvolva um programa que:
#
# 1. Peça para o usuário digitar sua idade (converta para int).
#
# 2. Pergunte se ele é estudante com a mensagem:
# "Você é estudante? (S/N): ".
#
# 3. Crie uma variável booleana chamada e_estudante que
# armazena o resultado de verificar se o que ele digitou
# é igual a "S".
#
# 4. Crie uma variável booleana chamada tem_direito_desconto.
# Ela deve receber True se a idade for maior ou igual a 60
# OU (or) se ele for estudante.
#
# 5. Exiba na tela a resposta final utilizando f-strings:
# "Tem direito a meia-entrada?"

import time

idade = int(input("Digite a sua idade: "))

time.sleep(0.5)

print("Perfeito!")

estudante = input("Você é estudante? (S/N): ")

e_estudante = estudante == "S" # VERIFICA SE É ESTUDANTE

time.sleep(0.5)

tem_direito_desconto = idade >= 60 or e_estudante # VERIFICA SE TEM DIREITO AO DESCONTO

print("Aguarde um instante, estamos verificando se você tem direito ao desconto de meia-entrada...")

time.sleep(1)

print(f"Tem direito a meia-entrada? {tem_direito_desconto}")
