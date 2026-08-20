import time

print("| POSTO DE PY-TOLINA |")
print("-"*60)

tanque = float(input("Digite o tamanho do tanque: "))
falta = float(input("Digite o quanto que falta no tanque: "))

if tanque >= falta:
    combustivel = float(input("Digite o quanto será abastecido: "))
    if combustivel > falta:
        print("Você está tentando abastecer mais que o limite!")
    else:
        litro = float(input("Digite o preço do litro: "))

        print("Calculando o quanto deve ser pago...")
        time.sleep(3)
        total = litro*combustivel
        print(f"Total a ser pago: R${total}")

        pagamento = float(input("Digite o quanto está pagando: R$"))

        if pagamento >= total:
            print("Pagamento concluído! E abastecido com sucesso!")
            if pagamento > total:
                troco = pagamento - total
                print(f"Troco: R${troco}")
            else:
                print("Não tem troco, quer mais dinheiro? Sai daqui")
        else:
            print("Dinheiro insuficiente! Não será abastecido, tchau.")
else:
    print("Quantidade de falta maior que o tanque!")