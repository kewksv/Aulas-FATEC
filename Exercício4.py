# 4. Desenvolva um programa que solicite o preço de um produto.
# Calcule um desconto de 15% sobre esse valor e exiba:
# 1. O valor exato do desconto;
# 2. O preço final após a subtração.
# Utilize f-strings para a saída dos dados.
import time
print ("O valor do desconto é de 15%")
desconto = 0.15
produto = input("Digite o valor do produto: ")
Valor_do_desconto = (float(produto)) * (desconto)
time.sleep(1.5)
print (f"O valor exato do seu desconto é de: {Valor_do_desconto} ")
print ("Agora iremos calcular o preço final do produto!")
time.sleep(2.5)
preço_final=(float(produto)) - (float(Valor_do_desconto))
print (f"O preço final do seu produto é de: {preço_final:2f}")
