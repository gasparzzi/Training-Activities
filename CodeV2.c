#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() { // o tipo de retorno da função main deve ser int
//Declarações de variáveis-------------------------------------------------------------------------------------------------------------------------------------------------------------  
	int condicao = 1, resto, valorintA, valorintB, quociente, numMeio, antecessor, sucessor, baseqc, quadradoqc, cuboqc;
    char opcao, voltar, FeMasc;
    float valormamao, totalmamao, maiorentre1, maiorentre2, posneg;







//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    printf("Seja bem vindo ao CodeV2 em C!!\n\
      \nEsse programa serve para guardar todas as atividades do Senac em C.\n"
      );
    while(condicao == 1) { 
        printf("1: Exercicio 1.1 - Caixa D'Agua\
          \n2: Exercicio 1.2 - Antecessor e Sucessor\
          \n3: Exercicio 1.3 - Resto e Quociente\
          \n4: Exercicio 1.4 - Mamao com Acucar\
		  \n5: Exercicio 1.5 - Quadrado e Cubo\
		  \n6: Exercicio 2.1 - Maior entre eles\
		  \n7: Exercicio 2.2 - Positivo e Negativo\
		  \n8: Exercicio 2.3 - Feminino e Masculino");
        printf("\n------------------------------------------------");
        printf("\nPor favor escolha uma opcao - [0] para sair: ");
        scanf(" %c", &opcao);

        switch(opcao) {
            case '1':
                /*1-Crie um programa no qual o usuário deverá inserir os
                valores da altura, largura e profundidade de uma caixa dágua, em cm. No final, exiba o volume dessa caixa dágua.
                Dica: Volume = Altura x Largura x Profundidade*/
                printf("------------------------------------------------\
                \nCaixa D'Agua\n------------------------------------------------");
                float altura, largura, profundidade;
                printf("\nDigite a altura da Caixa D'agua:\n");
                scanf("%f", &altura);
                printf("\nDigite a largura da Caixa D'agua:\n");
                scanf("%f", &largura);
                printf("\nDigite a profundidade da Caixa D'agua:\n");
                scanf("%f", &profundidade);
                printf("\nO volume e: %f", altura * largura * profundidade);
                break;
            
			case '2':
				/*Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.*/
                
				printf("\n------------------------------------------------\
                \nAntecessor e Sucessor\n------------------------------------------------\n");
                printf("\nDigite um numero: \n");
                scanf("%d", &numMeio);
                
                antecessor = numMeio - 1;
                sucessor = numMeio + 1;
                
                printf("\nO antecessor de %d, eh %d", numMeio, antecessor);
                printf("\nO sucessor de %d, eh %d", numMeio, sucessor);
                break;
            case '3':
            	printf("\n------------------------------------------------\
                \nResto e Quociente\n------------------------------------------------\n");
                printf("\nDigite um numero inteiro\n");
                scanf("%d", &valorintA);
                printf("\nDigite outro numero inteiro\n");
                scanf("%d", &valorintB);
                
                resto = valorintA % valorintB;
                quociente = valorintA/valorintB;
                
                printf("\nO valor do resto entre divisao de %d e %d eh: %d", valorintA, valorintB, resto);
                printf("\nO valor do quociente entre divisao de %d e %d eh: %d\n", valorintA, valorintB, quociente);
                break;
                
            case '4':
            	printf("\n------------------------------------------------\
                \nMamao com Acucar\n------------------------------------------------\n");
                printf("\nDigite o valor do produto: R$ ");
                scanf("%f", &valormamao);
            	
            	totalmamao = valormamao/5;
            	
            	printf("O valor das prestacoes é 5x de R$: %f", totalmamao);
            	break;
            
            case '5':
            	printf("\n------------------------------------------------\
                \nQuadrado e Cubo\n------------------------------------------------\n");
                printf("\nDigite um numero: \n");
                scanf("%d", &baseqc);
                
    			double expoenteq = 2;
    			double expoentec = 3;
    			double quadradoqc = pow(baseqc, expoenteq);
    			double cuboqc = pow(baseqc, expoentec);
    			
				int quadradoqcint = (int) quadradoqc;
				int cuboqcint = (int) cuboqc;
                
                printf("\nO quadrado de %d eh %d\nO cubo de %d eh %d\n", baseqc, quadradoqcint, baseqc, cuboqcint);
                break;
                
            	
			case '6':
				printf("\n------------------------------------------------\
                \nMaior entre eles\n------------------------------------------------\n");
                printf("\nDigite um numero: ");
                scanf("%f", &maiorentre1);
                printf("\nDigite outro numero: ");
                scanf("%f", &maiorentre2);
                
                if (maiorentre1 > maiorentre2) {
                	printf("O maior entre eles é: %f", maiorentre1);
				}	
                else {
        			printf("O maior entre eles é: %f", maiorentre2);
				}
                break;
			
			case '7':
				printf("\n------------------------------------------------\
                \nPositivo e Negativo\n------------------------------------------------\n");
            	printf("\nDigite um numero: ");
            	scanf("%f", &posneg);
            	
            	if (posneg > 0){
            		printf("\nEsse numero eh positivo");
				}
				else if (posneg < 0){
					printf("\nEsse numero eh negativo");
				}
				break;
			
			case '8':
				printf("\n------------------------------------------------\
                \nFeminino e Masculino\n------------------------------------------------\n");
            	printf("\nDigite [F] ou [M]");
            	scanf("%c", &FeMasc);
            	
            	if (FeMasc == 'F'){
            		FeMasc = 'f';
				}
				if (FeMasc == 'M'){
					FeMasc = 'm';
        		}
                
			case '0':
            	printf("\nObrigado por utilizar o CodeV2!");
                return 0;
            
			default:
            	printf("Opcao invalida!");
            	break;
        
		}
        int condicao2 = 1;
        while(condicao2 == 1) { 
            printf("\nDeseja retornar ao menu principal? [s] ou [n]: ");
            scanf(" %c", &voltar);
            
			if((voltar == 's') || (voltar == 'S')){
			printf("Retornando...");
            condicao2 = 0;
            }  
			
			
			else if((voltar == 'n') || (voltar == 'N')) {
                printf("\nObrigado por utilizar o CodeV2!");
                condicao = 0;
                return 0;
            }
            else {
                printf("\nOpcao invalida!");
            }
    	}
    
	}
return 0;
}
