print("| POSITIVO, NEGATIVO E NEUTRO |")
print("-"*60)

valor = int(input("Digite um valor para ser verificado: "))

if valor > 0:
    print(f"O valor {valor} é positivo!")
elif valor == 0:
    print("O valor é neutro (zero)!")
else:
    print(f"O valor {valor} é negativo")