#Início
print("Seja bem vindo ao CodeV2 em Python!!\n\
      \nEsse programa serve para guardar todas as atividades do Senac em Python.\n"
      )

def menu ():
    print("1: Exercício 1.1 - Caixa D'Água\
          \n2: Exercício 1.2 - Antecessor e Sucessor\
          \n3: Exercício 1.3 - Resto e Quociente\
          \n4: Exercício 1.4 - Mamão com Açucar\
          \n5: Exercício 1.5 - Quadrado e Cubo\
          \n6: Exercício 2.1 - Maior entre eles\
          \n7: Exercício 2.2 - Positivo e Negativo\
          \n8: Exercício 2.3 - Feminino e Masculino")
    
def programas (opcao):
 #Exercício1.1 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    if opcao == '1':
        '''1-Crie um programa no qual o usuário deverá inserir os
        valores da altura, largura e profundidade de uma caixa dágua, em cm. No final, exiba o volume dessa caixa dágua.
        Dica: Volume = Altura x Largura x Profundidade'''
      
        print("\n------------------------------------------------\
              \nCaixa D'Água\n------------------------------------------------\n")
        altura = float(input("Digite a altura da Caixa D'água: "))
        largura= float(input("\nDigite a largura da Caixa D'água: "))
        profundidade = float(input("\nDigite a profundidade da Caixa D'água: "))
        volume = altura * largura * profundidade

        print("\nO volume da caixa D'água é: ", str(volume) + "m³")
        
#Exercício1.2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    elif opcao == '2':
        '''Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.'''
        print("\n------------------------------------------------\
              \nAntecessor e Sucessor\n------------------------------------------------\n")
        numMeio = int(input("Digite um número: "))
        antecessor = numMeio - 1
        sucessor = numMeio + 1

        print("\nO antecessor de", numMeio, "é: ", antecessor, "\nO sucessor de ", numMeio, " é: ", sucessor)

#Exercício1.3 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif opcao == '3':
        '''Faça um algoritmo que leia dois valores inteiros A e B, imprima na tela o quociente e o resto da divisão inteira entre eles.'''
        print("\n------------------------------------------------\
              \nResto e Quociente\n------------------------------------------------\n")
        valorintA = int(input("Digite um número inteiro: "))
        valorintB = int(input("\nDigite outro número inteiro: "))

        resto = valorintA % valorintB
        quociente = valorintA//valorintB

        print(f"\nO resto da divisão inteira entre {valorintA} e {valorintB} é: {resto}\n")
        print(f"Quociente da divisão inteira entre {valorintA} e {valorintB} é: {quociente}")
        
    
    elif opcao == '4': 
        '''A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.'''
        print("\n------------------------------------------------\
              \nMamão com Açucar\n------------------------------------------------\n")
        valormamao = float(input("Digite o valor do produto: R$ "))

        totalmamao = valormamao/5

        print("O valor das prestações é 5x de R$: ", totalmamao)

    elif opcao == '5':
        '''Faça um algoritmo que leia um valor inteiro e apresente os resultados do quadrado e do cubo do valor lido.'''
        print("\n------------------------------------------------\
              \nQuadrado e Cubo\n------------------------------------------------\n")
        baseqc = int(input("Digite um número: "))

        quadradoqc = baseqc ** 2
        cuboqc = baseqc ** 3

        print(f"\nO quadrado de {baseqc} é {quadradoqc}\nO cubo de {baseqc} é {cuboqc}")

    elif opcao == '6':
        '''Faça um Programa que peça dois números e imprima o maior deles.'''
        print("\n------------------------------------------------\
              \nMaior entre eles\n------------------------------------------------\n")
        maiorentre1 = float(input("Digite um número: "))
        maiorentre2 = float(input("\nDigite outro número: "))

        if maiorentre1 > maiorentre2:
            print("\nO maior valor entre eles é: ", maiorentre1)
        else:
            print("\nO valor maior valor entre eles é: ", maiorentre2)

    elif opcao == '7':
        '''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''
        print("\n------------------------------------------------\
              \nPositivo e Negativo\n------------------------------------------------\n")
        posneg = float(input("Digite um número: "))

        if posneg > 0:
            print("\nEsse número é positivo")
        elif posneg < 0:
            print("\nEsse número é negativo")

    elif opcao == '8':
        '''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''
        print("\n------------------------------------------------\
              \nFeminino e Masculino\n------------------------------------------------\n")
        FeMasc = input("Digigite [F] ou [M]: ").lower()

        if FeMasc == 'f':
            print("\nF - Feminino")
        elif FeMasc == 'm':
            print("\nM - Masculino")
        else:
            print("\nSexo Inválido")

    
    else:
        print("\nOpção inválida!")



    
#while pós menu
condicao = 1
while True:
    #while do menu
    print("------------------------------------------------")
    menu()
    print("------------------------------------------------")
    opcao = input("\nPor favor escolha uma opção - [0] para sair: ")
    if opcao == '0':
        break
    programas(opcao)
#----------------------------------------------------------------------          
    print("------------------------------------------------")
    voltar = input("Deseja retornar ao menu principal? [s] ou [n]: ")
    if voltar == 's' or voltar == 'S':
        print("\nRetornando...")
    elif voltar == 'n' or voltar == 'N':
        print("Obrigado por utilizar o CodeV2!")
        break
    else:
        print("Digite uma opção válida!")
        break