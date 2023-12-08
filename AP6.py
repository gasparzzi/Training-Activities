import os
lista = []

while True:
    os.system("clear")
    try:
        print("Selecione uma opção:")
        opcao = input("[i]nserir, [l]istar, [a]pagar: ")
        if opcao == "i":
           adicionar =  input("Digite o ítem que deseja adicionar: ")
           lista.append(adicionar)
        elif opcao == "l":
           for indice, valor in enumerate(lista):
               print(indice, valor)
        elif opcao == "a":
            apagar = int(input("Digite o índice do ítem que deseja apagar: "))
            del(lista[apagar])
        else:
            print("Digite uma opção válida")
    except:
        print("Digite um índice válido!")