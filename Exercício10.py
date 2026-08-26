# Ex3. Validador de Meta de Vendas

META_VENDAS_DIARIAS = 1500

print("Olá vendedor(a)! Vamos calcular o seu desempenho de vendas hoje.")

vendas_hoje = float(input("Digite o valor total de vendas realizadas hoje: "))
meta_atingida = vendas_hoje >= META_VENDAS_DIARIAS

print(f"Você atingiu a meta de vendas hoje? {({False:'Não', True:'Sim'})[meta_atingida]}")