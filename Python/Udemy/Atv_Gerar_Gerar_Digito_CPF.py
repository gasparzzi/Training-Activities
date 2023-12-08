"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
------------------------------------------------------------------------
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0

# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
"""

import re
import sys

#método replace - variavel.replace('-','') sendo ''> "nada"
cpf =  input("Digite o CPF: ")
cpf = re.sub(r'[^0-9]', '', cpf) #para remover os caracteres indesejadospattern, replace, str

entrada_seq = cpf == cpf[0] * len(cpf)

if entrada_seq:
    print("Você enviou dados sequenciais")
    sys.exit()

nove_digitos = cpf[:9]

contador = 10

numero_multi = 0

soma_digitos = 0

for digito in nove_digitos:
   
    numero_multi = int(digito) * contador
    
    contador = contador - 1
    
    soma_digitos = numero_multi + soma_digitos

soma_digitos = (soma_digitos*10) % 11

if soma_digitos > 9:
    primeiro_digito = 0

elif soma_digitos <=9:
    primeiro_digito = soma_digitos

#-----------------------------------------------------------------------------------------------------------segundo digito

dez_digitos = cpf[:9] + str(primeiro_digito)

contador2 = 11

numero_multi2 = 0

soma_digitos2 = 0

for digito2 in dez_digitos:
   
    numero_multi2 = int(digito2) * contador
    
    contador2 = contador2 - 1
    
    soma_digitos2 = numero_multi2 + soma_digitos2

soma_digitos2 = (soma_digitos2*10) % 11

if soma_digitos2 > 9:
    ultimo_digito = 0

elif soma_digitos2 <=9:
    ultimo_digito = soma_digitos2

    print (primeiro_digito if primeiro_digito <= 9 else 0)

    print (ultimo_digito if ultimo_digito <= 9 else 0)
