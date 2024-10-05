'''Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''

#funções 
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
