print("| Autenticação de Sistema |")

usuarios = ["Admin","Oi","Murilo","João","Pietro","Pizza","Aquele Rodrigo"]

autenticado = True

for i in range(3):
    tentativa = input("> Digite o nome do usuário: ")
    if tentativa in usuarios:
        autenticado = False
        break
    elif tentativa == "Sair":
        quit()
    else:
        print("!! Errado: Tente novamente !!")

if autenticado == 1:
    print("! Seja bem vindo ao sistema !")
else:
    print("!!!! Acesso bloqueado !!!!")