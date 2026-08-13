print("| Calculo de Compras |")

produto1 = input("Digite o nome do 1º produto: ")
produto2 = input("Digite o nome do 2º produto: ")
produto3 = input("Digite o nome do 3º produto: ")

valor1 = float(input("Digite o valor do 1º produto: "))
valor2 = float(input("Digite o valor do 2º produto: "))
valor3 = float(input("Digite o valor do 3º produto: "))

total = valor1+valor2+valor3

credito = total * 1.078
debito = total
vista = total * 0.95

print("-"*30)
print("> Produtos <")
print(f"{produto1} - {valor1}")
print(f"{produto2} - {valor2}")
print(f"{produto3} - {valor3}")

print("> Formas de Pagamento <")
print(f"Crédito: R${credito}")
print(f"Débito: R${debito}")
print(f"À Vista: R${vista}")