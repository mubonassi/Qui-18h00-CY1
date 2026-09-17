print("| SORVETERIA PYTHONESCA |")
print("-"*60)

sabores = ["Chocolate","Baunilha","Flocos","Creme","Trufa","Ninho"]
coberturas = ["Granulada","Nutella","MM's","Paçoca","Fini"]

print("-- Sabores --")
print(sabores)
print("-- Coberturas --")
print(coberturas)

("--- Monte o Seu Pedido ---")
sabor = input("> Digite aqui o sabor desejado: ").capitalize()

if sabor in sabores:
    cobertura = input("> Agora digite a cobertura: ").capitalize()
    if cobertura in coberturas:
        print("-- Pedido Finalizado --")
        print(f">> Sorvete de {sabor} com {cobertura}")
    else:
        print("!! Cobertura não encontrada !!")
        print("-- Pedido Finalizado --")
        print(f">> Sorvete de {sabor}")
else:
    print("!! Sabor não encontrado !!")