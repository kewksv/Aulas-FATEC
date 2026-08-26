# 6. Crie um programa que peça ao usuário dois valores distintos (Valor A e Valor B).
# O programa deve primeiro exibir os valores na ordem em que foram digitados.
# Em seguida, utilize a sintaxe simplificada do Python para trocar os valores entre
# as variáveis e exiba o resultado final, mostrando que agora A possui o valor de B
# e vice-versa.
import time
Valor_A = int(input("Digite o valor de A: "))
Valor_B = int(input("Digite o valor de B: "))
if Valor_A == Valor_B:
    print ("Os valores digitados são iguais, por favor digite valores distintos.")
if Valor_A < 0 or Valor_B < 0:
    print ("Os valores digitados são negativos, por favor digite valores positivos.")
time.sleep (1.5)
print (f"Os valores digitados antes da troca foram: A = {Valor_A} e B = {Valor_B}")
input ("Pressione Enter para realizar a troca dos valores...")
#troca de valores 
Valor_A, Valor_B = Valor_B, Valor_A
time.sleep (1.5)
print (f"Os valores digitados após a troca foram: A = {Valor_A} e B = {Valor_B}")