print("| FEIRA DA FRUTA |")
print("-"*60)

frutas = ["Abacaxi","Abacate","Melão","Maracuja","Melancia","Morango","Kiwi","Laranja","Mexirica","Uva"]

print("-- ESCOLHA UMA DAS FRUTAS ABAIXO --")
print(frutas)

escolha = int(input("Digite qual fruta deseja (pelo indice): "))

if escolha < 0 or escolha > 9:
    print("ESCOLHA UMA FRUTA CERTA!")
else:
    fruta = frutas[escolha]
    print(f"Você escolheu: {fruta}")