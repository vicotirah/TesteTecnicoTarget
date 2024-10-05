'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP  R$67.836,43
• RJ  R$36.678,66
• MG  R$29.229,88
• ES  R$27.165,48
• Outros  R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  
'''

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




    
