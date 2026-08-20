#Tipos de Condição/Ifs

numero = int(input("Digite um número: "))

#Condição Composta -> Trabalhando com múltiplas condições
#OR (ou) -> Uma das condições necessita ser verdadeira
if numero == 30 or numero == 10:
    print("UAU, É 30 OU 10!")
else:
    print("uau, não é 30 ou 10...")

#AND (e) -> TODAS as condições necessitam ser verdadeiras
if numero >= 10 and numero <= 40:
    print("O numero está entre 10 e 40")
else:
    print("O número é menor que 10 ou maior que 40")

#Condição Encadeada -> Trabahando com múltiplas perguntas
#elif -> else if -> senão se -> uma condição/pergunta adicional
if numero == 10:
    print("Você digitou 10")
else:
    print("Você não digitou nenhum dos números")