#Saudação
print(end = '\n')
print("Olá! Sou o segundo programa de Wallace, o Atividade_LL2.")
print(end = '\n')
print("                ˅˅˅˅")
nome = input("Qual o seu nome? ")
print(end = '\n')
print("Seja bem vindo", nome + "!")
print(end = '\n')
print("Lembre-se que [ctrl + shift + barra_invert], mata o terminal")
print("Eis meu menu:")  

#Menu
def exibir_menu():
    print("-------------------------------------------------------")
    print("1 - Sequência de Fibonacci")
    print("2 - Número de Catalan")
    print("3 - Calculadora de desvio padrão")
    print("4 - Elementor")
    print("5 - Matriz")
    print("6 - NMax Edition")
    print("7 - Ocorrências")
    print("8 - The Perfect Number Validator") #sim, não tenho mais criatividade pros nomes.
    print("9 - String mais Frequente")
    print("10 - End of the Pain") #esse sim foi complicado.......
    print("parar - encerra o programa")
    print("-------------------------------------------------------")

#opções
def opcoes_menu (opcao):
    
#opção 1------------------------------------------------------------------------------------------------------
    if opcao == "1":
        print(end = '\n')
        print("----------------------")
        print("Sequência de Fibonacci")
        print("----------------------")
        print(end = '\n')
        print("A sequência de Fibonacci é uma sequência de números inteiros iniciados por zero e um,")
        print("no qual cada termo subsequente corresponde a soma dos dois números anteriores.")
        print(end = '\n')
        
        #função para aplicar a formula da sequência de Fibonacci
        def fibonacci(n): 
            fibonacci_seq = [0, 1] #inicia a variável com dois valores, 0 e 1
            while len(fibonacci_seq) < n: #enquanto a variável for menor que o valor digitado no input
                next_term = fibonacci_seq[-1] + fibonacci_seq[-2] #condição fórmula aplicada numa variável
                fibonacci_seq.append(next_term) #joga a variável next_term em 'fibonacci_seq'

            return fibonacci_seq #puxa a variável pós fórmula aplicada

        condicao = 1 #condição inicial para o while funcionar inicialmente
        while condicao == 1:
            try: #caso o usuário digite algo que não seja um número
                print("                                    ˅˅˅˅")
                n = int(input("Digite um número inteiro positivo: "))
                print(end = '\n')
                sequence = fibonacci(n) #variável que puxa a função 'fibonacci' e aplica no termo input do usuário
                n = str(n) #preciso converter em string para concatenar
                print(nome, "esta é a Sequência de Fibonacci até o", n + "°-ésimo termo:")
                print(end = '\n')
                for term in sequence: #"lê os termos na variável sequence e joga na variável term"
                    print(term)
                condicao = 0 #para o while
            except:
                print("-------------------------------------------------------")
                print("Digite um número inteiro positivo válido!")
                print("-------------------------------------------------------")

    
#opção 2------------------------------------------------------------------------------------------------------
    elif opcao == "2":
        print(end = '\n')
        print("-----------------")
        print("Número de Catalan")
        print("-----------------")
        print(end = '\n')
        print("Em combinatória, os números de Catalan formam uma sequência de números naturais que")
        print("ocorrem em vários problemas de contagem, frequentemente envolvendo objetos definidos recursivamente.")
        print(end = '\n')
        
        import math #importa uma biblioteca herdada da linguagem C

        def calcular_catalan(c): #função que aplica a fórmula
            numerador = math.factorial(2 * c) #puxa a função fatorial do math e aplica no númerador para a fórmula
            denominador = math.factorial(c + 1) * math.factorial(c) #também puxa a função do math, mas aplica no numer. e denom.
            catalan = numerador // denominador #define que a variável 'catalan' é a divisão int entre o numer. e denomi.
            return catalan #puxa a variável catalan
        
        condicao = 1
        while condicao == 1:
            try:
                print(end = '\n')
                print("                                  ˅˅˅˅")
                c = int(input("Digite um número inteiro positivo: "))
                catalan = calcular_catalan(c) #aplica o número do input na função 'calcular_catalan' e joga numa variável
                print(end = '\n')
                c = str(c)
                print(f'{nome} o número de catalan na posição de {c}°-ésimo termo é: {catalan}') #printa a variável 'catalan'
                print(end = '\n')
                condicao = 0
            except:
                print("-------------------------------------------------------")
                print("Digite um número inteiro positivo válido!")
                print("-------------------------------------------------------")


#opção 3------------------------------------------------------------------------------------------------------
    elif opcao == "3":
        import math #importa a função math herdada do C
        #Função para calcular a soma dos termos
        def calcular_soma(lista):
            soma = 0
            for num in lista:
                soma += num #soma os números encontrados, na variável soma que foi inciada em 0
            return soma
        #função para calcular a média
        def calcular_media(lista):
            soma = calcular_soma(lista)
            media = soma / len(lista)
            return media
        #função para calcular o desvio padrão
        def calcular_desvio_padrao(lista):
            media = calcular_media(lista)
            soma_diferencas_quadrado = 0 #iniciado em zero
            for num in lista: #procura um número na lista
                soma_diferencas_quadrado += (num - media) ** 2
            variancia = soma_diferencas_quadrado / len(lista) #divide a soma_diferencas_quadrado pela quantidade de números presentes na lista
            desvio_padrao = math.sqrt(variancia) #Calcula a raiz quadrada da variável 'variancia'
            return desvio_padrao
        
        print(end = '\n')
        print("----------------------------")
        print("Calculadora de desvio padrão")
        print("----------------------------")
        print(end = '\n')
        print("Este programa calcula a soma, média e desvio padrão de uma lista de números.")
        condicao = 1       
        while condicao == 1:
            try:
                print("                                                                                            ˅˅˅˅")
                numeros = input("Digite uma lista de números separados por espaço. Caso haja casas decimais, separar com '.': ")
                '''o 'map' converte a lista do split em um objeto de mapeamento, iterando os números da lista, e o 'list' converte em uma lista
                os objetos flutuantes mapeados, tudo isso é jogado numa variável'''
                numeros = list(map(float, numeros.split()))
                soma = calcular_soma(numeros) #daqui pra baixo é só aplicação de função
                media = calcular_media(numeros)
                desvio_padrao = calcular_desvio_padrao(numeros)
                condicao = 0
            except:
                print(end = '\n')
                print("-------------------------------------------------------")
                print("Digite uma lista de números válida!")
                print("-------------------------------------------------------")
                print(end = '\n')
        print(end = '\n')
        print(f'{nome}, aqui está a soma: {soma}, média: {media}, desvio padrão: {desvio_padrao: .4f}')
#opção 4------------------------------------------------------------------------------------------------------
    elif opcao == "4":
        print(end = '\n')
        print("---------")
        print("Elementor")
        print("---------")
        print(end = '\n')
        print("A função do Elementor é mostrar o segundo maior número de uma lista de números.")
        
        def encontrar_segundo_maior(lista): #função para encontrar os maiores e menores números de uma lista
            if len(lista) < 2: #se a soma dos índices encontrados na lista é menor que 2
                return None #retorna "None"(nulo) pois não há um número anterior para comparar
            maior = max(lista[0], lista[1]) #define uma variável que busca um número máximo, entre 2 números
            segundo_maior = min(lista[0], lista[1]) #aqui procura o número mínimo

            for i in range(2, len(lista)): #procura um número a partir do segundo indice da lista para que haja dois números a serem comparados
                if lista[i] > maior: #se o número encontrado for maior que o número máximo
                    segundo_maior = maior
                    maior = lista[i]
                elif lista[i] > segundo_maior and lista[i] < maior: #porém, se o número encontrado for maior(min) e for menor que o max (intervalo)
                    segundo_maior = lista[i] #o segundo maior é justamente esse número entre os dois termos.

            return segundo_maior
        print(end = '\n')

        while True:
            try:
                print("                                                         ˅˅˅˅")
                numeros = input("Digite os números que deseja testar separados por espaço: ").split() #coleta a lista
                print(end = '\n')
                numeros = [int(num) for num in numeros]
                segundo_maior = encontrar_segundo_maior(numeros)
                if segundo_maior == None: #caso não exista um segundo número
                    print(nome, "você digitou apenas um número.")
                    print(end = '\n')
                    print("Tente novamente:")

                else:
                    print(f'{nome} o segundo maior número na lista é: {segundo_maior}')
                    print(end = '\n')
                    break
            except:
                print("-------------------------------------------------------")
                print("Digite uma lista de números válida!")
                print("-------------------------------------------------------") 
#opção 5------------------------------------------------------------------------------------------------------   
    elif opcao == "5":
        print(end = '\n')
        print("------")
        print("Matriz")
        print("------")
        print(end = '\n')
        print("Este programa lê uma matriz quadrada e determina a soma dos elementos da diagonal principal.")
        print(end = '\n')
        print("Para uma matriz quadrada de ordem n, os elementos da diagonal principal são denotados por a[1,1],")
        print("a[2,2], ..., a[n,n], onde a[i,j] representa o elemento na linha i e coluna j da matriz.")
        print(end = '\n')
        def soma_diagonal_principal(matriz):
            soma = 0
            tamanho = len(matriz) #aqui ele vê o tamanho da matriz
            for i in range(tamanho): #aqui lê a lista de números com o range definido em 'tamanho' menos 1
            
            #Dentro do for, soma += matriz[i][i] adiciona o elemento na posição i da diagonal principal à variável soma.
                soma += matriz[i][i]
            return soma
        condicao = 1
        while condicao == 1:
            try:
                print("                                               ˅˅˅˅")
                numeros = input("Digite a lista de números separados por espaço: ")
                numeros = list(map(int, numeros.split())) #aqui ele pega a lista de substrings, converte em inteiros, mapeia e converte em uma lista de números
                condicao = 0
            except:
                print(end = '\n')
                print("-------------------------------------------------------")
                print("Digite uma lista de números válida!")
                print("-------------------------------------------------------") 
        tamanho_matriz = int(len(numeros) ** 0.5) #raiz quadrada aplicada na quantidade de elementos da lista de números

        matriz = [] #matriz iniciada como um parametro vazio
        for i in range(tamanho_matriz):
            linha = numeros[i * tamanho_matriz : (i + 1) * tamanho_matriz] #aqui pega os números da matriz, de cada linha, do primeiro ao ultimo número e coloca na variável linha
            matriz.append(linha) #coloca os objetos da variável 'linha' na variável matriz

        soma_diagonal = soma_diagonal_principal(matriz) #aplica a função da fórmula da matriz na variável 'matriz'
        print(end = '\n')
        print(nome, "a soma dos elementos da diagonal principal é", soma_diagonal)
        print(end = '\n')

   
#opção 6------------------------------------------------------------------------------------------------------  
    elif opcao == "6":
        print(end = '\n')
        print("-----------------")
        print("NMax Edition")
        print("-----------------")
        print(end = '\n')
        print("A função do NMax Edition é determinar, por comparação de matrizes, quantas edições são")
        print("necessárias para converter uma string em outra.")
        print(end = '\n')
        
        def min_edit_distance(s1, s2): #aqui, define a função em dois parâmetros (strings), e joga em duas variáveis
            m = len(s1)
            n = len(s2)

 
            dp = [[0] * (n+1) for _ in range(m+1)] #matriz utilizando as duas strings 'm' e 'n', 


            for i in range(m+1): #lê um número i num range de m (lembrando do len) + 1
                    dp[i][0] = i #determina que a matriz em i e 0 é igual a i. i é o número de caracteres que ele está lendo no range m+1 


            for j in range(n+1): #mesma linha de pensamento que a anterior, porém, aqui, j está em 0 e j
                    dp[0][j] = j


            for i in range(1, m+1): #aqui ele percorre o a matriz nas determinadas posições e compara as informações para determinar
                    for j in range(1, n+1): #se precisa editar a string ou quantas edições precisa
                        if s1[i-1] == s2[j-1]:
                            dp[i][j] = dp[i-1][j-1]
                        else:
                            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

            return dp[m][n]
       
        print("                                          ˅˅˅˅")
        s1 = input("Digite a primeira string a ser verificada: ")
        print(end = '\n')
        print("                                         ˅˅˅˅")
        s2 = input("Digite a segunda string a ser verificada: ")
        distancia = min_edit_distance(s1, s2)
        print(end = '\n')
        print(f'{nome}, {distancia} edições são necessárias.')
    
#opção 7------------------------------------------------------------------------------------------------------   
    elif opcao == "7":
        print(end = '\n')
        print("-----------")
        print("Ocorrências") #já tô sem criatividade :p
        print("-----------")
        print(end = '\n')
        print("A função de Ocorrências é mostrar quantas vezes um número aparece numa lista, utilizando um dicionário.")
        print(end = '\n')
        
        def contar_ocorrencias(lista):
            ocorrencias = {} #inicia a variável 'ocorrencias' com dicionário vazio
            for num in lista:
                if num in ocorrencias: 
                    ocorrencias[num] += 1 #coloca todos os números no dicionário ocorrência e acrescenta mais uma, que for encontrada
                else:
                    ocorrencias[num] = 1 #caso haja apenas 1 ocorrência no dicionário
            return ocorrencias
        condicao = 1
        while condicao == 1:
            try:
                print("                                                 ˅˅˅˅")
                numeros = input("Digite uma lista de números separados por espaço: ").split()
                numeros = [int(num) for num in numeros] 
                condicao = 0
            except:
                print(end = '\n')
                print("-------------------------------------------------------")
                print("Digite uma lista de números válida!")
                print("-------------------------------------------------------") 


        ocorrencias = contar_ocorrencias(numeros)

        print(end = '\n')
        print(f'{nome}, esta é a quantidade de vezes que cada número foi digitado:')
        
        for num, quantidade in ocorrencias.items(): #o método items puxa a chave do dicionário e seu respectivo valor, nesse caso, a chave e as ocorrencias
            print(f"{num}: {quantidade}")

    
#opção 8------------------------------------------------------------------------------------------------------  
    elif opcao == "8":
        print(end = '\n')
        print("----------------------------")
        print("The Perfect Number Validator")
        print("----------------------------")
        print(end = '\n')
        print("A função do T.P.N.V. é verificar se um número é perfeito ou não. Um número é perfeito se ")
        print("a soma de todos os divisores próprios do número (!= do número em si), é equivalente ao número.")
        print(end = '\n')
        
        def verificar_numero_perfeito(n): #vou comentar apenas o que não foi feito nos programas anteriores
            soma_divisores = 0
            for i in range(1, n): #procura um número i num range de 1 e n-1 
                if n % i == 0: 
                    soma_divisores += i #soma todos os divisores e acrecenta o i a cada soma, se o bool for verdadeiro
            if soma_divisores == n:
                return True
            else:                          
                return False
        condicao = 1         
        while condicao == 1:
            try:
                print("                                  ˅˅˅˅")
                n = int(input("Digite um número inteiro positivo: "))
                print(end = '\n')

                if verificar_numero_perfeito(n):
                    print(f"{nome}, {n} é um número perfeito.") #caso o return for True
                    print(end = '\n')
                else:
                    print(f"{nome}, {n} não é um número perfeito.") #caso o return for False
                    print(end = '\n')
                condicao = 0
            except:
                print(end = '\n')
                print("-------------------------------------------------------")
                print("Digite um número inteiro positivo válido!")
                print("-------------------------------------------------------")
#opção 9------------------------------------------------------------------------------------------------------    
    elif opcao == "9":
        print(end = '\n')
        print("---------------------")
        print("String mais frequente")
        print("---------------------")
        print(end = '\n')
        print("A função deste programa é verificar a string que mais aparece em uma lista.")
        print(end = '\n')
        
        def determinar_string_mais_frequente(lista):
            contador = {} #utilizando dicionário novamente
            for string in lista:
                if string in contador:
                    contador[string] += 1 #joga as strings lidas na lista, no dicionário, caso haja mais de uma
                else:
                    contador[string] = 1 #caso tenha só uma
            
            string_mais_frequente = None #é necessário iniciar esta variável como nula.
            max_frequencia = 0 #e essa aqui em 0
            
            for string, frequencia in contador.items(): #como anteriormente, aqui dividimos o dicionario em itens
                if frequencia > max_frequencia: #caso a frequencia for maior que max frequência (lembrando que tá iniciada em 0)
                    string_mais_frequente = string
                    max_frequencia = frequencia
            
            return string_mais_frequente
        
        print("                                                 ˅˅˅˅")
        strings = input("Digite uma lista de strings separadas por espaço: ").split()

        mais_frequente = determinar_string_mais_frequente(strings) #aplica a função na variável strings
        condicao = 0
        if mais_frequente:
            print(end = '\n')
            print(f"{nome}, a string mais frequente é: {mais_frequente}")
        else:
            print(end = '\n')
            print(nome,"a lista está vazia.")

#opção 10------------------------------------------------------------------------------------------------------    
    elif opcao == "10":
        print(end = '\n')
        print("---------------------")
        print("End of the Pain")
        print("---------------------")
        print(end = '\n')
        print("Brincadeiras a parte, esse programa verifica qual a maior soma possivel entre elementos em um subconjunto")
        print("composto por números, que não sejam pares adjacentes na lista original.")
        print(end = '\n')
        
        def calcular_maior_soma(nums): #função para verificar os intervalos
            n = len(nums) #é necessário verificar se a lista está vazia ou se tem apenas 1 número
            if n == 0:
                return 0
            elif n == 1:
                return nums[0]
            
            dp = [0] * n #para colocar n números na lista (esse n é definido lá em cima pelo len)
            dp[0] = nums[0] #define que a variável iniciada por 0 esse vai ser o primeiro número da lista
            dp[1] = max(nums[0], nums[1]) #esse aqui vai ser o maior valor entre o primeiro e segundo número da lista
            
            for i in range(2, n): #aqui procura o i, aplicando a restrição de que não pode usar números adjacentes na soma. observe o range
                dp[i] = max(dp[i-1], dp[i-2] + nums[i]) #o range é 2 pq iniciamos apenas duas variáveis anteriormente, vai de 2 até n-1
            
            return dp[n-1]

        condicao = 1
        while condicao == 1:
            try:
                print("                                                          ˅˅˅˅")
                numeros = input("Digite uma lista de números inteiros separados por espaço: ").split()
                numeros = [int(num) for num in numeros] #lê todos os números da lista digitada pelo usuário
                maior_soma = calcular_maior_soma(numeros) #aplica a função
                condicao = 0
            except:
                print(end = '\n')
                print("-------------------------------------------------------")
                print("Digite uma lista de números válida!")
                print("-------------------------------------------------------") 

        print(end = '\n')
        print(f"{nome}, a maior soma possível é: {maior_soma}")
#fim-----------------------------------------------------------------------------------------------------------
    else:
        print(end = '\n')
        print("Não reconheço esta opção.")
        print(end = '\n')
#Repetição
retornar = "s"
while retornar == "s":
    print(end = '\n')
    exibir_menu()
    print("                              ˅˅˅˅")  
    opcao = input("Por qual opção deseja navegar?  ")
    opcoes_menu(opcao)
    definicao = 1
    if opcao == "parar":
        print("Obrigado por utilizar o Atividade_LL2! Encerrando...")
        break
    while definicao == 1:
        print("------------------------------------------------------ ˅˅˅˅")
        voltar = input("Deseja retornar ao menu principal? - digite 's' ou 'n':  ")
        print("------------------------------------------------------------")
        if voltar == "s":
            print(end = '\n')
            print("Ótimo!")
            definicao = 0
        elif voltar == "n":
            print(end = '\n')
            print("Obrigado por utilizar o Atividade_LL2! Encerrando...")
            print(end = '\n')
            retornar = 0
            break
        else:
            print(end = '\n')
            print("Por favor digite um texto válido.")
            print(end = '\n')