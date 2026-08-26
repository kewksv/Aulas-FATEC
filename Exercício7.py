# 7. Crie um programa para auxiliar uma professora na divisão
# de guloseimas.
# Solicite a quantidade total de doces e o número de alunos.
# Calcule:
# 1. Quantos doces cada aluno receberá (divisão inteira);
# 2. Quantos doces restarão para a professora (resto da divisão).
# Utilize f-strings para uma exibição clara.
import time
print ("DIVISÃO DE GULOSEIMAS")
input ("Pressione Enter para continuar Professora...")
quantidade_total_de_doces = int(input ("Digite a quantidade total de doces: "))
numero_de_alunos = int(input ("Digite o número de alunos: "))
doces_por_aluno = quantidade_total_de_doces // numero_de_alunos # QUANTOS PARA CADA UM?
time.sleep (1.5)
print (f"Cada aluno receberá {doces_por_aluno} doces.")
resto = quantidade_total_de_doces % numero_de_alunos  # QUANTOS SOBRARAM?
time.sleep (2)
print (f"Restarão {resto} doces para a senhora, professora.")