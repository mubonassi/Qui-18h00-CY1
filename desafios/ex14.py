print("| AUMENTO E O DESCONTO")
print("-"*60)

num = float(input("Digite aqui o número: "))
porA = float(input("Digite aqui quanto aumenta: "))
valor_aumentado = num * (1 + porA / 100)

print(f"Seu aumento é de {valor_aumentado}")

print()

numD = float(input("Digite aqui o número: "))
porD = float(input("Digite aqui o desconto: "))

valor_com_desconto = numD * (1 - porD / 100)

print(f"Seu o resultado com desconto fica {valor_com_desconto}")