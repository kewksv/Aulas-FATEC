# Aulas-FATEC 🐍

Exercícios e atividades práticas de **Python** desenvolvidos durante as aulas de Programação I do curso de **Segurança da Informação** na FATEC Araraquara.

Os exercícios seguem os enunciados propostos pela professora, e os comentários originais foram mantidos em cada arquivo. O repositório documenta o meu aprendizado, do primeiro contato com a linguagem até as estruturas de repetição.

## 📁 Estrutura

```text
python/
├── 01-primeiros-passos/            (ex. 01 a 07)
├── 02-booleanos-e-comparacoes/     (ex. 08 a 13)
├── 03-condicionais-e-operadores/   (ex. 14 a 23)
├── 04-exercicios-de-fixacao/       (ex. 24 a 31)
└── 05-repeticao-while/             (ex. 32 a 41)
```

## 🧠 Conceitos praticados

- Entrada e saída de dados com `input()` e `print()`, conversão com `int()`, `float()` e `str()`
- Operadores aritméticos (`+`, `-`, `*`, `/`, `//`, `%`, `**`) e f-strings
- Booleanos, operadores de comparação e lógicos (`and`, `or`)
- Estruturas condicionais: `if`, `elif`, `else`
- Estruturas de repetição com `while`, contadores e acumuladores
- Uso do módulo `time`

## 📚 Índice dos exercícios

### 1. Primeiros passos

Entrada e conversão de dados, operações matemáticas, f-strings, divisão inteira e resto, troca de valores e módulo `time`.

| Nº | Arquivo | O que faz |
|---|---|---|
| 01 | [`ex01_monitoramento_de_login.py`](python/01-primeiros-passos/ex01_monitoramento_de_login.py) | Monitoramento de segurança: calcula as tentativas de login restantes. |
| 02 | [`ex02_calculadora_de_idade.py`](python/01-primeiros-passos/ex02_calculadora_de_idade.py) | Lê a idade como texto, converte e mostra a idade daqui a alguns anos. |
| 03 | [`ex03_valor_em_estoque.py`](python/01-primeiros-passos/ex03_valor_em_estoque.py) | Calcula o valor total em estoque a partir do preço e da quantidade. |
| 04 | [`ex04_desconto_de_15_porcento.py`](python/01-primeiros-passos/ex04_desconto_de_15_porcento.py) | Calcula o desconto de 15% e o preço final de um produto. |
| 05 | [`ex05_media_de_notas.py`](python/01-primeiros-passos/ex05_media_de_notas.py) | Média de três notas com parênteses e verificação de aprovação. |
| 06 | [`ex06_troca_de_valores.py`](python/01-primeiros-passos/ex06_troca_de_valores.py) | Troca o valor de duas variáveis com a sintaxe simplificada do Python. |
| 07 | [`ex07_divisao_de_guloseimas.py`](python/01-primeiros-passos/ex07_divisao_de_guloseimas.py) | Divisão inteira (`//`) e resto (`%`) na divisão de doces entre alunos. |

### 2. Booleanos e comparações

Variáveis booleanas, operadores de comparação, operadores lógicos `and` / `or` e validações com lógica.

| Nº | Arquivo | O que faz |
|---|---|---|
| 08 | [`ex08_maioridade_para_dirigir.py`](python/02-booleanos-e-comparacoes/ex08_maioridade_para_dirigir.py) | Verifica com booleano se a pessoa tem idade para dirigir. |
| 09 | [`ex09_sensor_temperatura_servidor.py`](python/02-booleanos-e-comparacoes/ex09_sensor_temperatura_servidor.py) | Alerta de superaquecimento em sala de servidores. |
| 10 | [`ex10_meta_de_vendas.py`](python/02-booleanos-e-comparacoes/ex10_meta_de_vendas.py) | Verifica se a meta diária de vendas foi atingida. |
| 11 | [`ex11_combustivel_de_viagem.py`](python/02-booleanos-e-comparacoes/ex11_combustivel_de_viagem.py) | Calcula litros, custo total e a divisão do combustível entre os passageiros. |
| 12 | [`ex12_seguranca_parque_de_diversoes.py`](python/02-booleanos-e-comparacoes/ex12_seguranca_parque_de_diversoes.py) | Valida idade `and` altura para entrar na montanha-russa. |
| 13 | [`ex13_desconto_meia_entrada.py`](python/02-booleanos-e-comparacoes/ex13_desconto_meia_entrada.py) | Valida idade `or` estudante para a meia-entrada no cinema. |

### 3. Condicionais e operadores

Aritmética e f-strings, concatenação e conversão de tipos, `if` / `elif` / `else`, operadores `%`, `!=` e `**`.

| Nº | Arquivo | O que faz |
|---|---|---|
| 14 | [`ex14_dobro_da_idade.py`](python/03-condicionais-e-operadores/ex14_dobro_da_idade.py) | Operadores aritméticos e f-string para calcular o dobro da idade. |
| 15 | [`ex15_boas_vindas_concatenacao.py`](python/03-condicionais-e-operadores/ex15_boas_vindas_concatenacao.py) | Concatenação com `+` e conversão com `str()`. |
| 16 | [`ex16_triagem_de_exame.py`](python/03-condicionais-e-operadores/ex16_triagem_de_exame.py) | Triagem com `and`: idade e peso para liberar o exame. |
| 17 | [`ex17_teste_do_toboga.py`](python/03-condicionais-e-operadores/ex17_teste_do_toboga.py) | Acesso ao tobogã com `or`: idade ou altura. |
| 18 | [`ex18_peneira_do_volei.py`](python/03-condicionais-e-operadores/ex18_peneira_do_volei.py) | Condicional simples com altura mínima (`>=`). |
| 19 | [`ex19_par_ou_impar.py`](python/03-condicionais-e-operadores/ex19_par_ou_impar.py) | Usa o operador `%` para verificar se o número é par ou ímpar. |
| 20 | [`ex20_classificacao_de_triangulos.py`](python/03-condicionais-e-operadores/ex20_classificacao_de_triangulos.py) | Valida o triângulo e classifica em equilátero, isósceles ou escaleno. |
| 21 | [`ex21_alerta_da_estufa.py`](python/03-condicionais-e-operadores/ex21_alerta_da_estufa.py) | Classifica a temperatura com `if` / `elif` / `else`. |
| 22 | [`ex22_area_do_circulo.py`](python/03-condicionais-e-operadores/ex22_area_do_circulo.py) | Calcula a área do círculo com o operador de potência `**`. |
| 23 | [`ex23_calculo_de_desconto.py`](python/03-condicionais-e-operadores/ex23_calculo_de_desconto.py) | Aplica 10% de desconto em compras acima de R$ 100. |

### 4. Exercícios de fixação

Reforço dos conceitos de condicionais e operadores lógicos em situações do dia a dia.

| Nº | Arquivo | O que faz |
|---|---|---|
| 24 | [`ex24_login_de_autenticacao.py`](python/04-exercicios-de-fixacao/ex24_login_de_autenticacao.py) | Simula uma tela de login com usuário e senha. |
| 25 | [`ex25_menu_de_atendimento_sac.py`](python/04-exercicios-de-fixacao/ex25_menu_de_atendimento_sac.py) | Menu interativo de atendimento com `if` / `elif` / `else`. |
| 26 | [`ex26_validador_de_cupom.py`](python/04-exercicios-de-fixacao/ex26_validador_de_cupom.py) | Valida cupons de desconto. |
| 28 | [`ex28_alerta_de_febre.py`](python/04-exercicios-de-fixacao/ex28_alerta_de_febre.py) | Alerta de febre a partir da temperatura corporal. |
| 30 | [`ex30_aluguel_de_veiculo.py`](python/04-exercicios-de-fixacao/ex30_aluguel_de_veiculo.py) | Libera o aluguel se tiver 21 anos ou mais `and` CNH. |
| 31 | [`ex31_frete_gratis.py`](python/04-exercicios-de-fixacao/ex31_frete_gratis.py) | Frete grátis para assinantes VIP `or` compras a partir de R$ 150. |

### 5. Repetição com while

Estruturas de repetição: contadores, acumuladores, validação de entrada e jogos simples.

| Nº | Arquivo | O que faz |
|---|---|---|
| 32 | [`ex32_contagem_1_a_20.py`](python/05-repeticao-while/ex32_contagem_1_a_20.py) | Mostra os números de 1 a 20 com `while`. |
| 33 | [`ex33_contagem_regressiva.py`](python/05-repeticao-while/ex33_contagem_regressiva.py) | Contagem regressiva com `while`. |
| 34 | [`ex34_contagem_ate_n.py`](python/05-repeticao-while/ex34_contagem_ate_n.py) | Mostra os números de 1 até o valor informado. |
| 35 | [`ex35_contagem_ate_n_b.py`](python/05-repeticao-while/ex35_contagem_ate_n_b.py) | Mostra os números de 1 até o valor informado. |
| 36 | [`ex36_tabuada.py`](python/05-repeticao-while/ex36_tabuada.py) | Tabuada de 1 a 10 com `while` e f-string. |
| 37 | [`ex37_classificacao_de_notas.py`](python/05-repeticao-while/ex37_classificacao_de_notas.py) | Classifica cinco notas em aprovado, recuperação ou reprovado. |
| 38 | [`ex38_soma_de_cinco_numeros.py`](python/05-repeticao-while/ex38_soma_de_cinco_numeros.py) | Lê cinco números e mostra a soma, usando contador e acumulador. |
| 39 | [`ex39_numero_primo.py`](python/05-repeticao-while/ex39_numero_primo.py) | Verifica se um número é primo contando seus divisores. |
| 40 | [`ex40_jogo_de_adivinhacao.py`](python/05-repeticao-while/ex40_jogo_de_adivinhacao.py) | Jogo de adivinhação com dicas de maior e menor. |
| 41 | [`ex41_validacao_de_senha.py`](python/05-repeticao-while/ex41_validacao_de_senha.py) | Pede a senha até acertar e conta as tentativas. |

## ▶️ Como executar

Com o Python 3 instalado, basta abrir o terminal na pasta do exercício e rodar:

```bash
python ex36_tabuada.py
```

## 👤 Autor

**Gabriel Guirra** ([@kewksv](https://github.com/kewksv)): estudante de Segurança da Informação na FATEC Araraquara.

---

*Aprendendo na prática, um passo de cada vez.*
