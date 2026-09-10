#Formatação de Strings/Print

palavra = "garrafA"
frase = "isso aqui é definitivamente uma frase aleatória"
print(palavra)
print(frase)
print("-"*60)

#Formatação de string - usando funções existentes da própria string
#upper() -> deixa tudo maiusculo
print(palavra.upper())

#lower() -> deixa tudo minusculo
print(palavra.lower())

#capitalize() -> deixa o primeiro caractere da string maiuscula e o resto minusculo
print(palavra.capitalize())

#title() -> ele identifica cada palavra na string (separado por espaço) e coloca maiusculo cada 1ª letra
print(frase.title())

a = "A"
b = "a"
if a.lower() == b.lower():
    print("a")