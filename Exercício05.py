# 5. Média de Notas:
# Peça 3 notas. Calcule a média garantindo que a soma seja
# priorizada pelos parênteses: (n1 + n2 + n3) / 3.
import time
print ("Calculadora de médias")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
media = (nota1 + nota2 + nota3) / 3
time.sleep(1.5)
print (f"A média das notas acima é de {media}")
print("Obrigado por utilizar a calculadora de médias!")
input ("Deseja saber se você foi aprovado ou reprovado? ")
if media >= 6:
    print ("Parabéns! Você foi aprovado!")
if media < 6:
    print ("Infelizmente você foi reprovado!")