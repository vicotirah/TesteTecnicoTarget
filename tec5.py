'''5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;'''

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
