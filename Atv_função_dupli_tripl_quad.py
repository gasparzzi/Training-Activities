# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4


def criar_multiplicador(multiplicador): #função do multiplicador
    def multiplicar(numero): #função do número a ser multiplicado
        return numero * multiplicador #retorna os parametros numero e multiplicador, um vezes o outro, de forma dinâmica
    return multiplicar #atrasando a execução da função multiplicar, para por um argumento posteriormente


duplicar = criar_multiplicador(2) #aplicando o argumento no multiplicador
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2)) #usando closures para aplicar os <números> que serão multiplicados pelo multiplicador, com a função retardada
print(triplicar(2))
print(quadruplicar(2))