# Ex1. Verificador Lógico de Maioridade Aula 2 LAB 

# Quando fazemos perguntas para o computador (como: "este número é maior que aquele?"), ele nos responde estritamente com True (Verdadeiro) ou False (Falso) 
# Desenvolva um programa no que verifique se a pessoa está com idade para dirigir ou não: 

# 1. Solicite ao usuário que digite o seu ano de nascimento utilizando input() 

# 2. Converta essa entrada para inteiro (int) e calcule a idade atual da pessoa (considere o ano atual como 2026). 
# 3. Crie uma variável lógica chamada pode_dirigir. 

# Essa variável deve receber o resultado da comparação se a idade calculada é maior ou igual a 18 (idade >= 18).

#  4. Sem usar if, exiba na tela a seguinte mensagem utilizando f-strings "Tem permissão para dirigir?

ano_de_nascimento = int(input("Digite a data do seu nascimento: "))
idade = 2026 - ano_de_nascimento
podedirigir = idade >= 18
print(f"Você tem permissão para dirigir? {['Não', 'Sim'][podedirigir]}")