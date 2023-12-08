#saudação
print(end = '\r\n')
print("Olá! Seja bem vindo a atividade de Wallace.")
print(end = '\r\n')
nome1 = input("Qual o seu primeiro nome? ")
print(end = '\r\n')
print("Seja bem vindo", nome1 + "!")
print(end = '\r\n')
print("Tenho estas funcionalidades:")
#menu

def exibir_menu():
    print("1 - Soma de termos iguais")
    print("2 - Multiplicador")
    print("3 - Conversor de C° para F°")
    print("4 - Identificador de números pares e ímpares") 
    print("5 - Calculador de IMC")
    print("6 - Identificador de maior número")
    print("7 - Identificador de nome mais curto")
    print("8 - Soma total")
    print("9 - Separador de números pares")
    print("--------------------------------------------------")
    print(end = '\r\n')

#aqui começa a função def de lista
def realizar_opcao(opcao):
    #soma de termos iguais
    if opcao == "1": #continuar daqui""
        print("Soma de termos iguais - digite somente números")
        print(end = '\r\n')
        termo_soma = input("Qual número deseja somar? ")
        print(end = '\r\n')
        resutado_soma = int(termo_soma) + int(termo_soma)
        print("Você escolheu: ", termo_soma)
        print(termo_soma, "+", termo_soma, "=", resutado_soma)
    
    #multiplicador
    elif opcao == "2":
        print("Multiplicador - digite somente números")
        print(end = '\r\n')
        termo_a = input("Digite o primeiro termo: ")
        termo_b = input("Digite o segundo termo: " )
        print(end = '\r\n')
        print(int(termo_a), "vezes", int(termo_b), "é", int(termo_a) * int(termo_b))
    
    #conversor
    elif opcao == "3":
        print("Conversor de °C para °F - digite somente números")
        print(end = '\r\n')
        celsius = input("Digite a temperatura em graus celsius: ")
        print(end = '\r\n')
        fahrenheit = (int(celsius) * 9/5) + 32
        resultado_temp = f'A temperatura em graus celsius {celsius} convertida em fahrenheit é: {fahrenheit: .1f}°F'
        print(resultado_temp) #puxa da função fString o dado
    
    #identificador pares e ímpares
    elif opcao == "4":
        print("Identificador de números pares e ímpares - digite somente números")
        print(end = '\r\n')
        num1 = input("Digite o número: ")
        print(end = '\r\n')
        iden = int(num1) % 2 == 0 #validador, divisão não pode ter resto
        if iden == True:
            print("Esse número é par")
        elif iden == False:
            print("Esse número é impar")
    
    #calculador de IMC
    elif opcao == "5":
        print("Calculador de IMC - digite somente números, separe casas decimais utilizando '.': ")
        print(end = '\r\n')
        altura = input("Digite sua altura: ")
        peso = input("Digite seu peso: ")
        imc = float(peso) / float(altura) ** 2
        print(end = '\r\n')
        resultado_imc = f'{nome1}, seu IMC é:, {imc: .1f}'
        print(resultado_imc)
   
    #identificador de maior número
    elif opcao == "6":
        print("Identificador de maior número:")
        print(end = '\r\n')
        lista_numeros = input("Digite somente números separados por espaço: ")
        list = lista_numeros.split()
        num_list = int(list[0])

        for varredura in list: #procure uma variável chamada lista na variável #num_list
            numero = int(varredura) #daí, a variável numero vair ser igual a variável num_list
            if numero > num_list: #se a variavel número for maior que a variável num_list
                num_list = numero #num_list é igual a número

        print(end = '\r\n')
        print("O maior número dentre eles é:", num_list)   
   
    #identificador de nome mais curto
    elif opcao == "7":
        print("Identificador de nome mais curto:")
        print(end = '\r\n' )
        nomes_recebidos = input("Digite os nomes que você deseja verificar, separados por espaço: ")
        print(end = '\r\n' )
        
        nomes = nomes_recebidos.split() #aqui, define uma nova vaviável 'nomes' que corresponde à lista 'nomes_recebidos'

        nome_mais_curto = nomes[0].strip()  #aqui ele converte a lista 'nomes' em parametros e remove os espaços em branco com a função 'strip'

        for nome in nomes: #procura uma variável na lista 'nomes'
            nome = nome.strip()  # Remove espaços em branco da váriavel 'nome' procurada em 'nomes'
            if len(nome) < len(nome_mais_curto): #compara o comprimento com a função 'len' e aplica a condição que 'nome' deve ser menor que 'os parametros de 'nome_mais_curto'
                nome_mais_curto = nome #define que que a variável 'nome' encontrada e aplicada a condição é igual à variável 'nome'

        print("O nome mais curto é:", nome_mais_curto)

   
   #soma total
    elif opcao == "8":
        print("Soma total - digite somente números:")
        print(end = '\r\n')
        termos = input("Digite os números que você deseja somar, separados por espaço: ")
        lista_termos = termos.split()
        parametro_lista = int(lista_termos[0])
        
        soma = 0 #é necessário definir uma variável com o valor em 0 para que comece a somar a partir dalí
                    #se colocar outra variável, ex.: 1, vai somar a partir do 1
        for termos_1 in lista_termos:
            soma += int(termos_1) #aqui ele puxa os números encontrados pelo for e joga na variável 'soma', somando todos os termos encontrados
        print(end = '\r\n')
        print("A soma de todos os termos que você escolheu é:", soma) #lembre de sempre dar print na variável resultado Wallace -_-
            
    #separador de número
    elif opcao == "9":
        print("Separador de números pares - digite somente números: ")
        print(end = '\r\n')
        coleta_num_sep = input("Digite aqui o os números que você deseja verificar - separados por espaço: ")
        list_num_sep = coleta_num_sep.split()
        numeros = [] #cuido com os iguais quando for definir um valor vazio a ser preenchido por uma função append
        for num_str in list_num_sep:
            if num_str.isdigit():  # Verifica se o valor é um número
                numeros.append(int(num_str)) #aplica todos os 'números' verificados anteriormente no parâmetro 'numeros' 
        num_pares = []
        for num_sep in  numeros: #antes era list_num_pares
            if  num_sep % 2 == 0: #"se o resto do número digitado for zero" antes convertia para inteiro
                num_pares.append(num_sep) #atribui os números pares à lista que será armazenada no espaço vazio na variável 'num_pares'
        print(end = '\r\n')
        print("Os números pares desta lista é: ", num_pares)

            


# Loop principal do menu
while True:
    print(end = '\r\n')
    print("--------------------------------------------------")
    opcao = input("Por favor, digite uma opção: ")
    print(end = '\r\n')
    exibir_menu()
    realizar_opcao(opcao)
    retornar = input("Deseja retornar ao menu principal? ")
    print(end = '\r\n')
    if retornar == "sim":
        print("Ótimo! ")
    else:
        break