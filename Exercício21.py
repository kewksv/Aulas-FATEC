import time
print ("Seja bem vindo ao alerta da estufa de biologia!")
time.sleep(1)
temperatura = (float(input(f"Olá aluno! Digite a temperatura apresentada no termômetro (em celsius): ")))
if 15 > temperatura:
 print("Muito Frio")
 time.sleep(1)
elif 25 >= temperatura and temperatura >= 15:
 print ("Temperatura Ideal")
 time.sleep (1)
else:
 print("Muito Quente")
time.sleep (1)
print("Obrigado por utilizar")
