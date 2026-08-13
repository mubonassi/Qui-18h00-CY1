print("| POSTO DE PY-TOLINA |")
print("-"*60)

falta = float(input("Digite o quanto que falta no tanque: "))
combustivel = float(input("Digite o quanto será abastecido: "))

if combustivel > falta:
    print("Você está tentando abastecer mais que o limite!")
else:
    print("Abastecido com sucesso!")