# Desafio Técnico Target 
## Lista de desafios técnicos para processo seletivo da Target
## Linguagem utilizada: Python 🐍

## Questões:

01) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
R: Será 91
~~~ python
indice = 13
soma = 0 
k = 0
while k < indice:
    k += 1
    soma += k
print(soma)
~~~
##
02) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
~~~ python
#Funções 
def fibonacci (n):
    fib_sequencia = [0, 1]
    #Gerar sequência até o input
    while fib_sequencia[-1] < n:
        prox_fib = fib_sequencia[-1] + fib_sequencia[-2]
        fib_sequencia.append(prox_fib) 
    return fib_sequencia

def fib_checar (numero):
    fib_sequencia = fibonacci(numero)
    if numero in fib_sequencia:
        print(f"O número inserido {numero} pertence à sequência Fibonacci")
    else:
       print(f"O número inserido {numero} não pertence à sequência Fibonacci")

#Input do usuário
n_user = int(input("Insira um número inteiro: "))
comparativo = fib_checar(n_user)
print(comparativo)
~~~
##
03) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
~~~ python
#Importar os dados
import json

#Carregar os dados do faturamento do arquivo JSON
def faturamento_arquivo():
    with open('dados.json', 'r') as i:
        faturamento = json.load(i)
    return faturamento

#Funções
#Calcular o faturamento 
def faturamento_calculo (faturamentos):
    faturamentos_preenchidos = []
    #Seleciona apenas faturamentos com valor diferente de 0
    for i in faturamentos:
        if i["valor"]>0:
            faturamentos_preenchidos.append(i["valor"])
    #Calcula menor, maior e média
    menor_fat = min(faturamentos_preenchidos)
    maior_fat = max(faturamentos_preenchidos)
    media_fat = sum(faturamentos_preenchidos)/len(faturamentos_preenchidos)
    return menor_fat, maior_fat, media_fat

#Calcular quantidade de dias com faturamento acima da média
def fat_dias_acima(faturamentos, media_fat):
    dias_acima = []
    #Compara o indice com o valor médio de faturamento
    for i in faturamentos:
        if i["valor"]>media_fat:
            dias_acima.append(i["valor"])
    return len(dias_acima)

#Atribuindo os dados para as variáveis
faturamentos = faturamento_arquivo()
menor_fat, maior_fat, media_fat = faturamento_calculo(faturamentos)
dias_acima = fat_dias_acima(faturamentos, media_fat)

print(f"Menor valor de faturamento: R${menor_fat:.2f}")
print(f"Maior valor de faturamento: R${maior_fat:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")
~~~
##
04) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP  R$67.836,43
• RJ  R$36.678,66
• MG  R$29.229,88
• ES  R$27.165,48
• Outros  R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  
~~~ python
#Dicionário
faturamento_estadual = {
"SP" : 67836.43,
"RJ" : 36678.66,
"MG" : 29229.88,
"ES" : 27165.48,
"Outros" : 19849.53
}

#Cálculos:
#Faturamento total somando valores do dicionário
fat_total = sum(faturamento_estadual.values())

#Percentual de cada estado 
percentuais = {}
for estado, faturamento in faturamento_estadual.items():
    percentual = (faturamento / fat_total) * 100
    percentuais[estado] = percentual

#Imprime
print(f"Faturamento Total: R$ {fat_total:.2f}")
print("\nPercentual de Representação por Estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
~~~
##
05) Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse.
~~~ python
#Coletar string
entrada = input("Digite uma string para inverter: ")

# String vazia 
string_invert = ""

#Começar do último índice
i = len(entrada) - 1

#Inverter a string
while i >= 0:
    string_invert += entrada[i]
    i -= 1  

print("String original:", entrada)
print("String invertida:", string_invert)
~~~


