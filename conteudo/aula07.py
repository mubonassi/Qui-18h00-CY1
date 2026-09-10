#Listas -> Array
#Lista permite você guardar uma COLEÇÃO de valores dentro de uma variável

#Criando e Exibindo a Lista
#Lista de String
lista1 = ["Item A","Item B","Item C","Item D"]
print(lista1)

#Lista de Números
lista2 = [1,2,3,4,5,6,7]
print(lista2)

#Lista Mista -> Uma coleção de valores permite qualquer tipo de informação
lista3 = [1,"A",1.5,True,10+20]
print(lista3)

#Exibindo um item específico da lista
#lista[indice] -> indice é um número inteiro que indica a posição do item na lista
indice = 0
item = lista1[indice]
print(f"1º Item: {item}")

#Verificando um item dentro da lista
item = input("Digite um dos itens da lista: ")
if item in lista1:
    print("Você digitou um item existente")
else:
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
    
#Puxando o indice da lista
indice = lista1.index(item)
print(f"O item {item} tem a indice {indice} na lista")