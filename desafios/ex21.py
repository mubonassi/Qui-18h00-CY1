print("| EN-PY-VISTA DE EMPREGO! |")
print("-"*60)

print("-- Seja bem vindo --")
print("-> Responda as perguntas com 'sim' ou 'não'")

resposta = input("Você veio para a entrevista de emprego: ")
if resposta == "sim":
    resposta = input("Você trouxe o currículo: ")
    if resposta == "sim":
        resposta = input("Você tem experiência na área: ")
        if resposta == "sim":
            resposta = input("Com tudo isso, deseja trabalhar aqui: ")
            if resposta == "sim":
                print("SEJA BEM VINDO! Seu salário é de R$2,00")
            else:
                print("Então, pra que perdeu meu tempo?")
        else:
            print("Vai lá aprender e depois volta")
    else:
        print("Vai lá correr buscar o currículo então")
else:
    print("Pera, então, tá fazendo o que aqui então")