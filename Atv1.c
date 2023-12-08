#include<stdlib.h>
#include<stdio.h> //utilizar 
#include<locale.h>

void main(){ //função principal
    int a = 5; //para declarar uma variável
    int b = 2;

    setlocale(LC_ALL, ""); //para usar acentos!!   
    printf("Olá!"); //texto
    printf("\n%d", a); //<%d> é para numeros inteiros
    printf("\nO valor de a = %d", a); // para juntar texto e numeros
    printf("\nQuebrando\nLinha");
    printf("\n%d", a + b, "\n"); //para calculos matemáticos
    
    //Para ler um valor
    int c;
    float d = 5.5;
    printf("\nDigite um valor para C:\n");
    scanf("%d", &c); //<&> se refere ao endereço na memória a ser alocado a variável
    printf("\nA soma de c + d é: %f", c+d); //<&f> para variável tipo float

    char f;
    printf("Digite o valor de f");
    fflush(stdin);
    scanf("%c", &f); //para limpar a entrada de buffer principal, ou seja, onde é armazenada as variáveis da entrada
    printf("\nO valor de f é: %c", f);
}