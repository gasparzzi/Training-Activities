#Início
import os
print("Seja bem vindo ao CodeV3 em Python!!\n\
      \nEsse programa serve para guardar todas as atividades do Senac em Python.\n"
      )

def menuConjuntos():
    print("1 - For e While")

def menuProgramas1 ():
    print("1 - Média de Salários\
          \n2 - Hotel\
          \n3 - Multiplicação\
          \n4 - QÍmpares e QPares\
          \n5 - Pesquisa RU\
          \n6 - Pesquisa população")

def programas1 (opcao):
    if opcao == '1':
        '''Faça um programa que calcule a média de salários de uma empresa, pedindo ao usuário a quantidade de funcionários, 
        o nome e o salário de cada funcionário e devolvendo a média, o salário mais alto e o salário mais baixo.'''
        
        print("\n\n------------------------------------------------\
              \nMédia de Salários\n------------------------------------------------\n")

        qtdFuncionarios = int(input("Digite a quantidades de funcionários: "))
        salarioalto = 0
        salariobaixo = 99999
        nomebaixo = ''
        nomealto = ''
        salariototal = 0
        
        
        for i in range(qtdFuncionarios):
            nomeMS = input("\nDigite o nome do funcionário: ")
            salarioMS = float(input("\nDigite o salário do funcionário: "))

            salariototal = salariototal + salarioMS
            mediasalarios = salariototal/qtdFuncionarios
            
            
            if salarioMS>salarioalto:
                nomealto = nomeMS
                salarioalto = salarioalto + salarioMS
                
            if salarioMS < salariobaixo:
                nomebaixo = nomeMS
                salariobaixo = salariobaixo + salarioMS
                
        print("A média de salários é: ", mediasalarios)
        print(f"\nO maior salário é o de: {nomealto}, que é: {salarioalto}")
        print(f"\nO menor salário é o de: {nomebaixo}, que é: {salariobaixo}")

    elif opcao == '2':
        '''2-Um hotel com 30 quartos cobra R$ 50,00 por diária e mais uma taxa de serviços. A taxa de serviços é de:
        • R 4,00 por diária, se o número de diárias for < 15;

        • R 3,60 por diária, se o número de diárias for = 15;

        • R 3,00 por diária, se o número de diárias for > 15.

        Faça um programa que imprima o nome e o total da conta de cada cliente do hotel. Imprima também o total ganho pelo hotel.
        '''

        print("\n\n------------------------------------------------\
            \nHotel\n------------------------------------------------\n")
        ganho_do_hotel = 0
        vagasocupadas = 0
        while vagasocupadas <= 30:
            nomeHT = input("\nDigite o nome do hóspede - [0] para parar: ")

            if nomeHT == '0':
                break
            
            diariasHT = int(input("\nDigite o numero de dias de hospedágem: "))

            if diariasHT < 15:
                taxa_de_servicos = 4.00
            elif diariasHT == 15:
                taxa_de_servicos = 3.60
            else:
                taxa_de_servicos = 3.00

            totalconta = (50 + taxa_de_servicos)*diariasHT

            ganho_do_hotel = ganho_do_hotel + totalconta

            print(f"\nNome do cliente: {nomeHT}\nValor total da conta: R${totalconta}")

            vagasocupadas += 1

        print("\nO lucro total do hotel foi: R$", ganho_do_hotel)


    elif opcao == '3':
        '''Sem utilizar a operação de multiplicação, 
        escreva um programa que multiplique dois números inteiros. Por exemplo: 2 * 2 = 2 + 2.'''
        print("\n\n------------------------------------------------\
              \nMultiplicação\n------------------------------------------------\n")

        variavelmultiplicao = float(input("Digite o número que você deseja multiplicar: "))
        multiplicacao = int(input("\nInforme quantas vezes você deseja multiplicar esse número: "))
        
        produto = 0
        for i in range(multiplicacao):
            produto = produto + variavelmultiplicao

        print("\nO resultado da multiplicação é: ", produto)
        
#-------------------------------------------------------------------------------------------------------------------------------------------
    elif opcao == '4':
        '''Faça um programa que leia um conjunto de números (X) e imprima a quantidade de números pares (QPares) 
        e a quantidade de números impares (QImpares) lidos. Admita que o valor 9999 é utilizado como sentinela para fim de leitura.'''
        print("\n\n------------------------------------------------\
            \nQÍmpares e QPares\n------------------------------------------------\n")

        QPares = 0
        QImpares = 0
        while True:
            verificador = int(input("\nDigite um número - [9999] para sair: "))
            
            if verificador == 9999:
                break
            if verificador % 2 == 0:
                print("\nEsse número é par")
                QPares = QPares + 1
            else:
                print("\nEsse número é impar")
                QImpares = QImpares + 1
    
        print("\nO total de números pares é de: ", QPares)
        print("\nO total de números impares é de: ", QImpares)

#-------------------------------------------------------------------------------------------------------------------------------------------
#   
    elif opcao == '5':
        '''Foi feita uma pesquisa com um grupo de alunos de uma universidade, na qual 
        se perguntou para cada aluno, o número de vezes que utilizou o restaurante da universidade no último mês. 
        Construa um programa que determine:
        O percentual de alunos que utilizaram menos que 10 vezes o restaurante;
        O percentual de alunos que utilizaram entre 10 e 15 vezes;
        O percentual de alunos que utilizaram o restaurante acima de 15 vezes.'''
        contadoralunos = 0
        contadorpercen1 = 0
        contadorpercen2 = 0
        contadorpercen3 = 0

        while True:
            print("\n\n------------------------------------------------\
                \nPesquisa RU\n------------------------------------------------\n")
            print("\nSeja bem vindo a pesquisa de utilização do RU! ")
            pesquisaAlunos = int(input("\nCom que frequencia você utilizou o RU no ultimo mês? - [0] para parar: "))
            os.system("cls")
            
            if pesquisaAlunos == 0:
                break
            
            contadoralunos = contadoralunos + 1
                
            if pesquisaAlunos < 10:
                contadorpercen1 = contadorpercen1 + 1
            

            elif pesquisaAlunos >= 10 and pesquisaAlunos <= 15:
                contadorpercen2 = contadorpercen2 + 1

            elif pesquisaAlunos > 15:
                contadorpercen3 = contadorpercen3 + 1

        percentual1 = (contadorpercen1/contadoralunos)*100
        percentual2 = (contadorpercen2/contadoralunos)*100
        percentual3 = (contadorpercen3/contadoralunos)*100

        print("------------------------------------------------")
        print(f"\nO percentual de pessoas que utilizaram menos de 10 vezes é de {percentual1: .2f}%")
        print(f"\nO percentual de pessoas que utilizaram entre 10 e 15 vezes é de {percentual2: .2f}%")
        print(f"\nO percentual de pessoas que utilizaram mais de 15 vezes é de {percentual3: .2f}%")

    elif opcao == '6':
        '''Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, 
            a qual coletaram os seguintes dados referentes a cada habitante para serem analisados:

            sexo (masculino e feminino)
            cor dos olhos (azuis, verdes ou castanhos)
            cor dos cabelos (louros, castanhos, pretos)
            idade
            Faça um um programa que determine e escreva:

            a maior idade dos habitantes;
            a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
            a quantidade de indivíduos que tenham olhos verdes e cabelos louros;
            O final do conjunto de habitantes é reconhecido pelo valor -1 informado como idade.'''
        contadorsexoM = 0
        contadorsexoF = 0
        azuis = 0
        verdes = 0
        castanhos = 0
        louros = 0
        castanhosC = 0
        pretos = 0
        contadorverdelouro = 0
        contadorMulheres = 0
        maioridade = 0
        
        while True:
            print("\n\n------------------------------------------------\
                \nPesquisa população\n------------------------------------------------\n")
            print("\nSeja bem vindo à pesquisa de população! ")
            
            idadePesquisa = int(input("\n------------------------------------------------\nQual sua idade? [-1] para parar: "))

            if idadePesquisa == -1:
                break
            
            if maioridade < idadePesquisa:
                maioridade = idadePesquisa
            
            sexopopulacao = input("\n------------------------------------------------\nQual o seu sexo? [m] ou [f]: ")
            
            if sexopopulacao == 'f':
                contadorsexoF += 1
            elif sexopopulacao == 'm':
                contadorsexoM += 1
            else:
                print("Opção inválida!")

            cordosolhos = input("\n------------------------------------------------\nQual a cor de seus olhos? \n1 - Azuis\n2 - Verdes\n3 - Castanhos: ")

            if cordosolhos == '1':
                azuis += 1
            elif cordosolhos == '2':
                verdes += 1
            elif cordosolhos == '3':
                castanhos += 1
            else:
                print("Opção inválida!")

            cordosCabelos = input("\n------------------------------------------------\nQual a cor dos seus cabelos? \n1 - Louros\n2 - Castanhos\n3 - Pretos: ")
            os.system("cls")

            if cordosCabelos == '1':
                louros += 1
            elif cordosCabelos == '2':
                castanhosC += 1
            elif cordosCabelos == '3':
                pretos += 1
            else:
                print("Opção inválida!")
            
            if idadePesquisa >= 18 and idadePesquisa <=  35 and sexopopulacao == 'f' :
                contadorMulheres += 1

            if cordosCabelos == '1' and cordosolhos == '2':
                contadorverdelouro += 1

        print(f"\n------------------------------------------------\nA maior idade foi: {maioridade}")
        print(f"\nA quantidade de mulheres com a idade entre 18 e 35 anos é de: {contadorMulheres}")
        print(f"\nA quantidade de individuos com cabelos verdes e louros: {contadorverdelouro}")



            
    else:
        print("\nOpção Inválida!")




#Estrutura de Repetição --------------------------------------------------------------------------------------------------------------
condicao = 1
while condicao == 1:
    #while do menu
    print("------------------------------------------------")
    menuConjuntos()
    print("------------------------------------------------")

#Conjuntos de atividades  
    conjuntos = input("\nPor favor escolha um conjunto - [0] para sair: ")
    if conjuntos == '0':
        break
  
    elif conjuntos == '1':
        print("------------------------------------------------")
        menuProgramas1()
        print("------------------------------------------------")
        opcao = input("\nEscolha uma opção: ")
        programas1(opcao)
   

#Retornar ao menu---------------------------------------------------------------------------------------------------------------------          
    while True:
        print("------------------------------------------------")
        voltar = input("Deseja retornar ao menu principal? [s] ou [n]: ")
        if voltar == 's' or voltar == 'S':
            print("\nRetornando...")
            break
        elif voltar == 'n' or voltar == 'N':
            print("\nObrigado por utilizar o CodeV3!")
            condicao = 0
            break
        else:
            print("\nDigite uma opção válida!")