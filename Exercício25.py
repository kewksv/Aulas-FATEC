#Exercício 2: Menu Interativo de Atendimento (SAC)

#Monte o menu de um robô de atendimento

#Mostre na tela as opções:
#1 - Suporte Técnico
#2 - Financeiro
#3 - Falar com Atendente.

#Solicite que o usuário digite a opção desejada.

#Exiba para qual setor a chamada está sendo transferida ou diga "Opção inválida" se for digitado algo fora do menu.

print("Seja bem vindo ao SAC!")

print ("1 - Suporte Técnico")
print ("2 - Financeiro")
print ("3 - Falar com atendente")

escolha = input("Digite o número de qual serviço deseja utilizar: ")

if escolha == "1":
    print("Encaminhando para o Suporte Técnico...")
elif escolha == "2":
    print("Encaminhando para o Financeiro...")
elif escolha == "3":
    print("Encaminhando para o Help Desk...")
else:
    print("Opção inválida! Tente novamente, por favor.")
