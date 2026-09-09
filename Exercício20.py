# 7. Classificação de Triângulos (Aritmética, Relacionais e Lógica)
# Para construir um triângulo, a regra matemática diz que a soma de dois lados deve ser sempre maior que o terceiro lado.
# Peça ao usuário para digitar três valores inteiros: ladoA, ladoB e ladoC.
# I. Primeiro, verifique se os lados formam um triângulo válido usando o operador and:
# if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
# II. Se for um triângulo válido, use o if/elif/else para classificá-lo:
# Equilátero: Se todos os lados forem iguais (ladoA == ladoB and ladoB == ladoC).
# Isósceles: Se pelo menos dois lados forem iguais.
# Escaleno: Se todos os lados forem diferentes.
# III. Se a primeira validação for falsa, o programa deve exibir:
# "Os valores não podem formar um triângulo!"

import time

print("Seja bem vindo ao programa : Classificação de triângulos!")
time.sleep(0.5)

ladoA = int(input("Digite o valor do lado A: "))
ladoB = int(input("Digite o valor do lado B: "))
ladoC = int(input("Digite o valor do lado C: "))

if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):  # VALIDA O TRIÂNGULO
    if ladoA == ladoB and ladoB == ladoC:
        time.sleep(0.5)
        print("O triângulo é equilátero.")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        time.sleep(0.5)
        print("O triângulo é isósceles.")
    else:
        time.sleep(0.5)
        print("O triângulo é escaleno.")
else:
    print("Os valores não podem formar um triângulo.")

print("Obrigado por participar do programa!")
