print("| VERIFICANDO MÉDIA |")
print("-"*60)

n1 = float(input("Digite a #1 Nota: "))
n2 = float(input("Digite a #2 Nota: "))
n3 = float(input("Digite a #3 Nota: "))

media = (n1+n2+n3)/3
mediaMin = 7

print(f"Média Final: {media}")

if media >= mediaMin:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado!")