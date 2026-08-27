print("| VEIFFRVADOR FC DE OVNTEI |")
print("-"*60)

idade = int(input("Digite aqui a sua idade: "))
convite = input("Digite 'sim' ou 'não' se tiver convite: ")

if (convite == "sim" or convite == "Sim") and idade >= 18:
    print("Você pode entrar na festa!")
else:
    print("Você NÃO pode entrar na festa!")
