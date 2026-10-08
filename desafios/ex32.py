print("| SOMANDO NA REPETIÇÃO |")
print("-"*60)

valor = int(input("> Digite o valor até qual número será somado: "))
resultado = 0
conta = ""

#[1,2,3,4,5]
for i in range(1,valor+1):
    resultado += i
    conta += str(i)
    if i < valor:
        conta += " + "
    
print(f"{conta} = {resultado}")