print("| QUIZ GEEK |")
print("-"*60)

personagens = ["Kirby","Sub-Zero","Pikachu","Toad","Kuromi"]
franquias = ["Kirby","Mortal Kombat","Pokémon","Mario Bros","Hello Kitty"]

personagem = input(">> Digite o nome do personagem: ")

if personagem in personagens:
    franquia = input(f">> Digite a franquia do {personagem}: ")
    indice = personagens.index(personagem)
    if franquia == franquias[indice]:
        print("** Acertou! **")
    else:
        print("!! Errou !!")
else:
    print("!! Personagem não encontrado !!")