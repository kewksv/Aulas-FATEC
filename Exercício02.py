# 2. Leia a idade como texto usando input(), converta para inteiro
# e imprima a idade da pessoa daqui a 5 anos.
import time
print ("CALCULADORA DE IDADE")
Nome = input(f"Digite o seu nome: ")
Sobrenome = input("Digite seu sobrenome: ")
print ("Olá", Nome)
Idade = input("Agora, sua idade: ")
time.sleep (1.5)
print (f"Obrigado, {Nome}!")
anos = (input("Por quantos anos você quer avançar? "))
time.sleep (1.5)
print(f"Daqui a {anos} anos você terá {str(int(Idade) + int(anos))} anos ")
print ("Obrigado por usar!")