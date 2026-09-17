print("| AUTENTICANDO SISTEMA |")
print("-"*60)

usuarios = ["Murilo","João","Kirby","Admin","Hello Kitty"]
senhas = ["kirby","steamverde","rosa","1234","fofo"]

usuario = input(">> Digite o nome do usuário: ")

if usuario in usuarios:
    senha = input(f">> Digite a senha do {usuario}: ")
    
    indice = usuarios.index(usuario)
    
    if senha == senhas[indice]:
        print("** Sistema autenticado! **")
    else:
        print("!! Senha incorreta !!")
else:
    print("!! Usuário não encontrado !!")