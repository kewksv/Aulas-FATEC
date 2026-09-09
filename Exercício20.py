import time
print("Seja bem vindo ao programa : Classificação de triângulos!")
time.sleep (0.5)
LadoA = float(input("Digite o valor do lado A: "))
LadoB = float(input("Digite o valor do lado B: "))
LadoC = float(input("Digite o valor do lado C: "))
if (LadoA + LadoB > LadoC) and (LadoA + LadoC > LadoB) and (LadoB + LadoC >LadoA):
    if LadoA == LadoB and LadoB == LadoC:
     time.sleep (0.5)
     print("O triângulo é equilátero.")
    elif LadoA == LadoB or LadoA == LadoC or LadoB == LadoC:
        time.sleep (0.5)
        print("O triângulo é isósceles.")
    elif LadoA != LadoB and LadoA != LadoC and LadoB != LadoC:
        time.sleep (0.5)
        print("O triângulo é escaleno.")
else:
    print("Os valores informados não formam um triângulo.")
print("Obrigado por participar do programa!")