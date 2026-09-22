#Exercício 8: Frete Grátis na Loja Virtual
#Um e-commerce oferece frete grátis se o cliente for assinante do clube VIP ('s') OU se o valor total da
#compra for maior ou igual a R$ 150.00. Crie um programa que peça o valor da compra (float) e se o cliente é
#assinante ('s'/'n') e exiba o resultado com f-string.

print("Bem vindo ao verificador de frete grátis!")

valor_compra = float(input("Digite o valor total da compra: R$ ").replace(",", "."))

assinante = input("Você é assinante do clube VIP? (sim/não): ").strip().lower()

if valor_compra >= 150.00 or assinante == "sim":
    print("Frete Grátis liberado")
else: 
    print("Frete Grátis negado")