def multi (*args):
    total = 1
    for num in args:
       total *= num
    return total
  
multiplicacao = multi(1, 2, 3, 4, 5)
print(multiplicacao)



def parImpar(numero):
    comparador = numero % 2 == 0

    if comparador == True:
        return comparador
    
    return comparador


teste = parImpar(numero = int(input("Digite um número: ")))
print (teste)