#Estruturas de Condição -> Criam condições para que um bloco de código seja executado
#Um comando/uma instrução só irá acontecer se determinada condição retornar verdadeira
#Condição > Ação

#Exemplo: Se a palavra digitada for 'abacaxi', a gente mandará uma mensagem confirmando que foi digitado
palavra = input("Digite a palavra 'abacaxi': ")

#if
#se (condição) então {ação}
if palavra == "abacaxi":
    print("Você digitou a palavra que eu pedi!")

#Exemplo: Se o número digitado for maior que zero mandará mensagem falando sobre, senão, falará que não digitou
numero = int(input("Digite um numero maior que zero: "))

if numero > 0:
    print("Você digitou um número maior que zero!")
#senão {ação}
else:
    print("Você NÃO digitou um número maior que zero!")

#Comparadores
# == - Igual a (valor == valor)
# > - Maior que (valor > valor)
# < - Menor que (valor < valor)
# >= - Maior ou igual a (valor >= valor)
# <= - Menor ou igual a (valor <= valor)
# != - Diferente de (valor != valor)

#Diferença entre = e ==
# = - Atribuição -> nome = 'João' -> O seu nome É João
# == - Comparação -> nome == 'João' -> O seu nome é João?