import time
print("Bem-vindo ao programa de desconto!")
time.sleep (0.5)
produto = float(input("Digite o valor do produto: R$"))
if produto > 100:
    desconto = produto * 0.10
    produto_final = produto - desconto
    print(f"O valor do produto com desconto é: R${produto_final:.2f}")
    time.sleep(1)
else:
    time.sleep(1)
    print(f"O valor do produto é: R${produto:.2f}")
print ("Obrigado por participar do programa! :)")