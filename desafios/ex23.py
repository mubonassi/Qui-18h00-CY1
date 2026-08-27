print("| SISTEMAS DE PONTUAÇÃO DE AMONGUS BLOCK BLAST |")
print("-"*60)

pontos = float(input(">> Digite aqui sua pontuação: "))

if pontos == 0:
    print("Rank: ...só zero?")
elif pontos > 1000:
    print("Rank: Lendário")
elif pontos > 700:
    print("Rank: Mestre")
elif pontos > 500:
    print("Rank: Campeão")
elif pontos > 200:
    print("Rank: Veterano")
else:
    print("Rank: Iniciante")