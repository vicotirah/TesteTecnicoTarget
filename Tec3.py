'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

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