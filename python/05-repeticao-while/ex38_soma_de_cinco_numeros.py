#Solicite cinco números inteiros, um de cada vez, utilizando while. Ao final, exiba a soma dos valores digitados.
#
#Dica: Use contador para controlar as cinco entradas e soma para acumular os valores. Teste: 2, 4, 1, 3 e 5 → soma 15.

contador = 1

soma = 0

while contador <=5:

    numero = int(input("Digite um número inteiro: "))
    soma = soma + numero
    contador = contador + 1
    

print(f"A soma dos valores digitados é: {soma}")
