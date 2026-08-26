# 1. Crie um programa de monitoramento de segurança.
# O sistema possui um limite padrão de 5 tentativas de login.
# Solicite ao usuário quantas tentativas ele já realizou sem sucesso.
# Calcule quantas chances ainda restam e exiba usando f-strings.
import time
print ("SISTEMA DE MONITORAMENTO DE SEGURANÇA")
LIMITE = 5
tentativas = input("Digite quantas tentativas foram realizadas: ")
restam = (LIMITE - int(tentativas))
time.sleep (1.5)
print (f"Então restam: {restam} tentativas")