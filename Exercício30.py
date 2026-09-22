#Exercício 7: Aluguel de Veículo
#Para alugar um carro, uma locadora exige que o cliente tenha pelo menos 21 anos 
# E possua carteira de habilitação (CNH) ('s' para sim ou 'n' para não).
#Crie um programa que solicite a idade (inteiro) e a confirmação
#da CNH e exiba se o aluguel foi liberado ou negado usando f-string.

print ("Bem vindo ao Aluguel de Veículo!")

idade = (int(input("Digite a sua idade: ")))

cnh = input("Insira se possuí Carteira de Motorista (CNH). sim/não: ").strip().lower()

if idade >= 21 and cnh == "sim":
    print("Liberado! Vamos continuar a aplicação")
else:
    print("Acesso Negado")