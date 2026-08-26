# SISTEMA DE SEGURANÇA DE PARQUE DE DIVERSÕES

import time

ano_de_nascimento = int(input("Digite a data do seu nascimento: "))

idade = 2026 - ano_de_nascimento

time.sleep(0.5)

altura = float(input("Digite a sua altura em metros: "))

pode_entrar = (idade >= 12 and altura >= 1.50)

time.sleep(0.5)

print(f"Você tem permissão para entrar na montanha russa? {pode_entrar}")