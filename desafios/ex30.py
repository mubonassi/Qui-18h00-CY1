print("| REALIZANDO A TABUADA |")
print("-"*60)
valor = int(input("> Digite qual o valor que deseja realizar a tabuada: "))

for i in range(1,11):
    tabuada = valor*i
    print(f"{valor}x{i} = {tabuada}")