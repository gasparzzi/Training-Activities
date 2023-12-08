nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# O fatiar, passos e ordem deve ser posto dentro de colchetes (formt. de str)
if nome and idade:  # Se for verdadeiro
    print(f'Seu nome invertido é: {nome [::-1]}')
    if " " in nome:
        print("Seu nome contém espaços")

    else:
        print("Seu nome não contém espaços")

    print(f'Seu nome contém {len(nome)} letras')
    print(f"A primeira letra de seu nome é: {nome[0]}")

    print(f"A última letra de seu nome é: {nome [-1]}")
    # -1 é a posição do último dígito da string
else:
    print("Você digitou campos vazios")  # Se a condição and for descumprida
