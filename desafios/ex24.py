print("| FEIRA DA FRUTA |")
print("-"*60)

frutas = ["Abacaxi","Abacate","Melão","Maracuja","Melancia","Morango","Kiwi","Laranja","Mexirica","Uva"]

print("-- ESCOLHA UMA DAS FRUTAS ABAIXO --")
print(frutas)
escolha = int(input("Digite qual fruta deseja (pelo indice): "))
fruta = frutas[escolha]

print(f"Você escolheu: {fruta}")