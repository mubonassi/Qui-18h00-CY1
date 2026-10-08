print("| MOSTRANDO NÚMEROS |")

valor = int(input("> Digite até qual número será mostrado: "))

if valor < 0:
    print("!! Não pode ser número negativo !!")
else:
    for num in range(1,valor+1):
        print(f"#{num}")