# Ex2. Sensor de Temperatura de Servidor
temperatura = input("Digite a temperatura atual em Celsius: ")
alerta_ativo = (float(temperatura)) > 40
print(f"Alerta de superaquecimento ativo? {({False:'Não', True:'Sim'})[alerta_ativo]}")
