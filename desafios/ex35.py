print("| Z-TYPER MASTER |")
print("-"*60)

palavras = ["Blabla","Mercado","Capítulo","Xbox Series S"]
acertos = 0
erros = 0

print(">> Digite corretamente as palavras abaixo <<")


for palavra in palavras:
    print(f"> {palavra}")
    tentativa = input("> Digite aqui a tentativa: ")
    
    if tentativa == palavra:
        acertos += 1
        print("!! ACERTOU !!")
    else:
        erros += 1
        print("!! ERROU !!")

print(f"| Acertos: {acertos} | Erros: {erros}")

if erros == 0:
    print("!! GABARITADO !! ACERTOU TUDO !!")
elif acertos == 0:
    print("...caramba, não acertou um?")
else:
    print(f"Muito bom! Você acertou {acertos}, mas pode melhorar!")