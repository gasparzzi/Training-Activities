num_inp = input("Digite um número inteiro: ")
num_int = num_inp

if int(num_int) % 2 == 0:
    print("Este número é par")
elif int(num_int) % 2 != 0:

    print("Este número é ímpar")


recebe_hora = input("Que horas são? ")
int_recebe_hora = int(recebe_hora)
if int_recebe_hora >= 0 and 11 >= int_recebe_hora:
    print("Bom dia!")
elif int_recebe_hora >= 12 and 17 >= int_recebe_hora:
    print("Boa tarde!")
elif int_recebe_hora >= 18 and 23 >= int_recebe_hora:
    print("Boa noite!")


recebe_nome = input("Digite seu nome: ")
nome = len(recebe_nome)

if nome < 4:
    print("Seu nome é curto.")

elif nome >= 5 and 6 >= nome:
    print("Seu nome é normal.")

elif nome > 6:
    print("Seu nome é muito grande.")