print("| CALCULANDO COM TODOS OS OPERADORES! |")
print("-"*40)

#recebendo os numeros do usuario
numero1 = float(input("Digite o 1º número: "))
numero2 = float(input("Digite o 2º número: "))

#calculando cada operação
soma = numero1+numero2 #adição
sub = numero1-numero2 #subtração
mult = numero1*numero2 #multiplicação
div = numero1/numero2 #divisão
pot = numero1**numero2 #potência - elevado
resto = numero1%numero2 #resto de divisão
divint = numero1//numero2 #divisão por inteiro

#mostrando a conta inteira de cada um
print(f"{numero1} + {numero2} = {soma}")
print(f"{numero1} - {numero2} = {sub}")
print(f"{numero1} * {numero2} = {mult}")
print(f"{numero1} / {numero2} = {div}")
print(f"{numero1} ^ {numero2} = {pot}")
print(f"{numero1} % {numero2} = {resto}")