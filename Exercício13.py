# VALIDADOR DE DESCONTO NO CINEMA
#     UM CINEMA LOCAL CONCEDE O BENEFICIO DE MEIA-ESTRADA PARA CLIENTE QUE CUMPREM PELO MENOS UM DOS SEGUINTES CRITÉRIOS
import time
idade = int(input("Digite a sua idade: "))
time.sleep(0.5)
print ("Perfeito!")
estudante = input("Você é estudante? (S/N): ")
e_estudante = estudante == "S"
time.sleep(0.5)
tem_desconto = ( idade >= 60 or e_estudante )
print("Aguarde um instante, estamos verificando se você tem direito ao desconto de meia-entrada...")
time.sleep(1)
print(f"Você tem direito ao desconto de meia-entrada? {tem_desconto}")