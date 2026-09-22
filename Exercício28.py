#Exercício 5: Verificador de Temperatura Corporal (Alerta de Febre)

#Se a temperatura for maior ou igual a 37.8 °C, exiba a mensagem "Atenção: Estado de febre!".

# Caso contrário, exiba "Temperatura normal". Use f-string para exibir o resultado.

temperatura = float(input("Digite a sua temperatura corporal em °C: "))

if temperatura >= 37.8:
    print(f"Atenção: Estado de febre! - Temperatura: {temperatura:.1f} °C")
else:
    print(f"Temperatura normal - Temperatura: {temperatura:.1f} °C")