# 6. Detetive do Resto (Operador Módulo % e Condicional)
# O operador % (Módulo) nos devolve o resto da divisão inteira entre dois números.
# Escreva um programa em Python que:
# I. II. Solicite ao usuário um número inteiro qualquer através do teclado
# (lembre-se de usar o int(input()) para converter o dado).
# Use a estrutura condicional if/else e o operador % para verificar se o número digitado é PAR ou ÍMPAR.
# (Dica: Todo número par dividido por 2 deixa resto igual a 0. Se o resto for 1, o número é ímpar!)

import time

print("Bem-vindo ao programa de verificação de números pares e ímpares!")
numero = int(input("Digite um número: "))

if numero % 2 == 0:  # SE O RESTO DA DIVISÃO POR 2 FOR 0, É PAR
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

print("Obrigado por participar do programa!")
