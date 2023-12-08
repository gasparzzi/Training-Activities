frase = input("Digite uma frase: ")

i = 0 #variável do índice
qtd_apareceu_mais_vezes = 0 #variável que é somada as vezes que cada letra é lida
letra_apareceu_mais_vezes = '' #variável que onde é posta a letra lida

while i < len(frase):
    letra_atual = frase[i] #variável que pega letra por letra de acordo com o índice 'i' da variavel 'frase'

    if letra_atual == ' ':
        i += 1 #+= iteração, pega i e soma i com o próximo item, no caso do primeiro caracter ser uma string vazia
        continue #continua o loop do while

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual) #variável que é posta a quantidade de vezes de cada letra encontrada no count, da letra do 
                                                             #do 'letra_atual' separada pelo índice da variável 'i' que é o indice da variável 'frase'
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual: #adiciona os valores iterados na variável fora do while
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1 #outra variável 'i' para continuar analisando índice por indice da variável frase

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)