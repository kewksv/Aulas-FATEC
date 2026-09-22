#Exercício 3: Validador de Cupom de Desconto

#Crie um verificador de cupons para um e-commerce. O usuário deve digitar o código do cupom

#Se digitar "DEV10", exiba "Cupom aceito! Você ganhou 10% de desconto."

#Se digitar "DEV20", exiba "Cupom aceito! Você ganhou 20% de desconto."

#Caso contrário, exiba "Cupom inválido ou expirado."

print("Seja bem vindo ao validador de autenticação")

user = input("Digite o nome de usuário: ")

print(f"Obrigado {user}!")

cupom = input(f"Digite o código de cupom {user}: ")

if cupom == "Dev10":
    print("Cupom aceito! Você ganhou 10% de desconto")
elif cupom == "Dev20":
    print("Cupom aceito! Você ganhou 20% de desconto")
else:
    print("Cupom inválido ou expirado.")