#Escreva um programa em Python que solicite uma senha. A senha correta será “python123”.
#Utilize while para pedir novamente enquanto a senha estiver incorreta. A cada erro, exiba “Senha incorreta.
#Tente novamente!”.
#Quando o usuário acertar, exiba “Acesso permitido!” e a quantidade total de tentativas, incluindo a tentativa correta.
#Dica: solicite a primeira senha antes do while e inicie tentativas em 1. Compare os textos utilizando senha !=
#"python123". Aumente o contador de tentativas a cada nova senha digitada.
#Teste: se o usuário digitar “abc”, “123” e “python123”, o programa deverá informar 3 tentativas
senha = input("Digite a senha: ")
tentativas = 1

while senha != "python123":
    print("Senha incorreta. Tente novamente!")
    senha = input("Digite a senha: ")
    tentativas = tentativas + 1

print("Acesso permitido!")
print(f"Quantidade total de tentativas: {tentativas}")