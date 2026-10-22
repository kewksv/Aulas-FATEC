#Escreva um programa em Python que solicite a nota final de cinco alunos, um de cada vez, utilizando while e float.
#
#Considere notas válidas entre 0 e 10. Dentro do laço, utilize if/elif/else para mostrar a situação de cada aluno:
#
#Nota maior ou igual a 7: “Aprovado”. Nota maior ou igual a 5 e menor que 7: “Recuperação”.
#
#Nota menor que 5: “Reprovado”. Ao terminar, exiba “Classificação encerrada!”.
#
#Dica: utilize um contador de 1 a 5. A leitura da nota e a classificação ficam dentro do while.
#
#Atualize o contador após o if/elif/else.
#
#Teste: para as notas 8, 6, 4, 7 e 5, as situações serão Aprovado, Recuperação, Reprovado, Aprovado e Recuperação.

contador = 1

while contador <=5:

    nota = float(input("Digite a nota do aluno: "))
    if nota >= 7:
        print("Aprovado")
    elif nota >= 5 and nota < 7:
        print ("Recuperação")
    elif nota < 5:
        print ("Reprovado")
    contador = contador + 1

print ("Classificação encerrada!")
