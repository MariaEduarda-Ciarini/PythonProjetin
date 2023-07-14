print("Bem Vindos, a Calculadora Python")
operações = {"+": lambda x,y: x + y,
             "-": lambda x,y: x - y,
             "*": lambda x,y: x * y,
             "/": lambda x,y: x / y}

while True:
    numero_1 = int(input("Digite um número: "))
    operador = input("Digite um operador (+, -, *, /): ")
    numero_2 = int(input("Digite um segundo número: "))

    if operador not in operações:
        print("Invalidação de operador!, olhe novamente os operadores.")
    else:
        resultado = operações[operador](numero_1, numero_2)
        print("Resultado", resultado)
    if input("Você quer continuar  fazendo equações? (S/N)").lower() == 'n':
        break