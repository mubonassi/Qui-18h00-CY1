#Estruturas de REPETIÇÃO
#Que são estruturas/controle do código que permite que um bloco de comandos possa ser repetido em uma quantidade de vezes determinada

#Repetição Contada (quantidade definida)
#Que será determinado quantas X vezes o código será executado
#FOR -> Estrutura de repetição contada

#range(x) - função que define quantas vezes(ou o alcance de repetição) que o código será repetido
#i - é uma variável contadora, que irá guardar o estado (indice) da contagem
for i in range(5): #esse código será executado 5x
    print("Teste")
print("-- Fim da Repetição --")

#Exibindo a váriavel de contagem no código
#[0,1,2,3,4]
for num in range(5):
    print(f"Repetição #{num}")
print("-- Fim da Repetição --")

#range(x,y) -> define qual o intervalo inicial e qual o intervalo final
#[2,3,4,5]
for i in range(2,5+1):
    print(f"Repetição #{i}")
print("-- Fim da Repetição --")

#range(x,y,z) -> Define qual o intervalo inicial, qual o intervalo final, o salto entre cada número
#[10,20,30,40,50]
for i in range(10,50+1,10):
    print(i)
print("-- Fim da Repetição --")