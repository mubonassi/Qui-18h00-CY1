print("| PERSONALIZANDO A REPETIÇÃO |")
print("-"*60)

num1 = int(input("> Digite o número inicial: "))
num2 = int(input("> Digite o número final: "))
num3 = int(input("> Digite o salto entre cada número: "))

if num1 < 0 or num2 < 0 or num3 < 0:
    print("!! Não pode número negativo !!")
elif num1 > num2:
    print("!! O número final não pode ser menor que o primeiro !!")
elif num3 == 0:
    print("!! O salto não pode ser zero !!")
else:
    for num in range(num1,num2+1,num3):
        print(f"#{num}")