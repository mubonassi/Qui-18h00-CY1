print("| PARES E IMPARES |")
print("-"*60)

valor = int(input("> Digite até qual número irá ser mostrado: "))

print("-- PARES --")
pares = ""
for n in range(2, valor+1, 2):
    pares += str(n) + " "
print(pares)
    
print("-- IMPARES --")
impares = ""
for n in range(1, valor+1, 2):
    impares += str(n) + " "
print(impares)