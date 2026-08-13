print("| CALCULANDO UM RETÂNGULO |")
print("-"*40)

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = base * altura
perimetro = (base + altura) * 2
diferenca = base - altura
diametro = (base**2+altura**2)**0.5

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")
print(f"Diferença: {diferenca}")
print(f"Diâmetro: {diametro}")