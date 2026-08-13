print("| TEMPO DE VIAGEM |")
print("-"*50)

distancia = float(input("Digite a distancia em km: "))
velocidade = float(input("Digite a distancia em km/h: "))

tempoViagem = distancia/velocidade

print(f"Você levará aproximadamente {tempoViagem}hrs para chegar no seu destino")