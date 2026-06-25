#Recebendo Valores + Variaveis

#Variaveis -> Pequenos espaços na memória do programa que guarda UMA INFORMAÇÃO
#Declarando/Criando uma Variavel
#nome = valor

nome = "Murilo Bonassi" #string
idade = 32 #int
altura = 1.68 #float
calculo = 10/80

#Exibindo variaveis
print(nome)
print(idade)
print(altura)
print(calculo)

#Exibindo as variaveis em um texto
#Método 1 - Concatenando
print("Meu nome é",nome)
print("E eu tenho",idade,"anos")

#Método 2 - Formatando String - usando o F String
print(f"E eu tenho {altura}m de altura")
print(f"10/80 = {calculo}")