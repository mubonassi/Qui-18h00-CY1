#Break e Quit()

#Break é uma palavra chave que funciona apenas em fluxo de repetição
#O break encerra o fluxo de repetição independente se ele era pra ter chego no final do loop ou não

for i in range(1000000000000000000000000000000000000):
    print(i)
    if i >= 5:
        break
print("Fim da Repetição")

#Função quit()
#Encerra o algoritmo
for i in range(1000000000000):
    print(i)
    if i >= 5:
        quit()
print("VOCÊ NÃO VERÁ ESSE PRINT!")