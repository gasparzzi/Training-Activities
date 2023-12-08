import random
import sys

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0, 9))
    
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

dez_digitos = nove_digitos + str(primeiro_digito)

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

    
prim_dig = primeiro_digito if primeiro_digito <= 9 else 0
ult_dig = ultimo_digito if ultimo_digito <= 9 else 0
print(nove_digitos + str(prim_dig) + str(ult_dig))