#Validador de Sistema de Autenticação (Login)

#Crie um programa que simule a tela de login de um sistema.

# Solicite o nome de usuário e a senha

#Se o usuário for "admin" E a senha for "python123", exiba "Acesso liberado! Bem-vindo ao painel."

# Caso contrário, exiba "Usuário ou senha incorretos."

print("Seja bem vindo ao validador de autenticação")

user = input("Digite o nome de usuário: ")

print(f"Obrigado {user}!")

passw = input("Digite a sua senha: ")

if user == "admin":
    print ("Acesso liberado, seja bem vindo ao painel!")
else:
    print("Acesso Negado.")
