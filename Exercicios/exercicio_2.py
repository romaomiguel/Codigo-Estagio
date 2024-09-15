#Função que gera fibonacci
def fibonacci(n):
    sequencia_fib = []
    a, b = 0, 1
    while a <= n:  # Usa <= para garantir que o valor n seja incluído, se desejado
        sequencia_fib.append(a)
        a, b = b, a + b
    return sequencia_fib


n = 100 #Termo usado para definir o limite dos termos de fibonnaci
sequencia_fib = fibonacci(n) #Usado para achar o "terms" na sequencia de Fibonacci

termos = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))

if termos in sequencia_fib:
    print ("A sequencia de Fibonacci é: ", sequencia_fib)
    print("Este termo esta na sequencia de Fibonacci")
else:
    print("Este termo não esta na sequencia de Fibonacci")