# Exercícios de Fixação
# Ex5. Sistema de Segurança de Parque de Diversões
# Aula 2 LAB
#
# Uma montanha-russa radical possui regras rígidas de segurança.
# Para poder andar no brinquedo, o visitante precisa cumprir
# dois requisitos obrigatórios ao mesmo tempo:
#
# 1. Ter idade igual ou maior que 12 anos.
#
# 2. Ter altura igual ou maior que 1.50 metros.
#
# Desenvolva um programa que:
#
# 1. Peça ao usuário o seu ano de nascimento e calcule sua
# idade (considere o ano atual como 2026).
#
# 2. Peça sua altura em metros (ex: 1.48).
#
# 3. Crie uma variável booleana chamada pode_entrar.
# Ela deve receber o resultado lógico que valide se a idade
# é suficiente E (and) se a altura é suficiente.
#
# 4. Exiba o resultado final na tela de forma amigável
# usando f-strings:
# "Autorização para entrar na montanha-russa"

import time

ano_de_nascimento = int(input("Digite a data do seu nascimento: "))

idade = 2026 - ano_de_nascimento # CALCULA A IDADE ATUAL

time.sleep(0.5)

altura = float(input("Digite a sua altura em metros: "))

pode_entrar = idade >= 12 and altura >= 1.50 # VERIFICA IDADE E ALTURA

time.sleep(0.5)

print(f"Autorização para entrar na montanha-russa: {pode_entrar}")
