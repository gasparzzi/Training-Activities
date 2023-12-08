#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

//As funções devem ser declaradas fora do escopo da função principal, e o tipo dos parametros devem ser definidos.
void menuConjuntos () {
		printf("1 - For e While\n2 - Funcoes\n3 - Listas e Tuplas");
	}



//Variáveis globais---------------------------------------------------------------------------------------------------------------------
float ganho_do_hotel;

//--------------------------------------------------------------------------------------------------------------------------------------
//Conjunto 1
void menuProgramas1 (){
		printf("1 - Media de salarios\n2 - Hotel\n3 - Multiplicacao\n4 - QImpares e QPares\n5 - Pesquisa RU\n6 - Pesquisa populacao");
		printf("\n7 - Calculadora\n8 - Pares\n9 - Frigorifico\n10 - Pesquisa populacao 2\n11 - Senha\n12 - Lojas Tabajara\n13 - Departamento de Meteorologia\n14 - Tabuada\n15 - Potencia e Divisao");	
	}

int programas1 (char opcao1[3]){
		if (strcmp(opcao1, "1") == 0){
			system("cls");	
			printf("\n------------------------------------------------\nMedia de Salarios\n------------------------------------------------\n");
            
			printf("Digite a quantidade de funcionarios: ");
            
			int qtdFuncionarios;
            scanf("%d", &qtdFuncionarios);
	        
	        float salarioalt = 0, salariobaixo = 9999999, salariototal = 0, salarioMS=0, mediasalarios=0;
	        char nomeMS[20], nomealt[20], nomebaixo[20];
	        
			for(int i=0; i<qtdFuncionarios; i++){
				
				printf("\nDigite o nome do funcionario: ");
				scanf("%s", nomeMS);
	        
	        	
				printf("\nDigite o salario do funcionario: R$: ");
	        	scanf("%f", &salarioMS);
				
				salariototal = salariototal + salarioMS;
				
				if(salarioMS>salarioalt){
				strcpy(nomealt, nomeMS);
					salarioalt = salarioMS;
				}
				
				if(salarioMS<salariobaixo){
					strcpy(nomebaixo, nomeMS);
					salariobaixo = salarioMS;
				}
			}
			
			mediasalarios = salariototal/qtdFuncionarios;
			printf("\nO maior salario eh de %s", nomealt);
			printf(" que eh: R$ %.2f", salarioalt);
			printf("\nO menor salario eh de %s", nomebaixo);
			printf(" que eh: R$ %.2f", salariobaixo);
			printf("\nA media dos salarios eh: R$ %.2f", mediasalarios);	 
		}


		else if (strcmp(opcao1, "2") == 0){
			system("cls");
			printf("\n------------------------------------------------\nHotel\n------------------------------------------------\n");
			int vagas_ocupadas = 0;

			while (vagas_ocupadas <= 30){
				char nomeHT[20];
				printf("\nDigite o nome do hospede: ");
				scanf("%s", nomeHT);

				
				int hospedagem_clientes;
				printf("\nDigite a quantidade de dias de hospedagem: ");
				scanf(" %d", &hospedagem_clientes);
				
				float taxa_de_servicos;
				
				if (hospedagem_clientes < 15){
					taxa_de_servicos = 4.00;
				}
				else if (hospedagem_clientes == 15){
					taxa_de_servicos = 3.60;
				}
				else{
					taxa_de_servicos = 3.00;
				}
				
				float totalconta;
				totalconta = (50 + taxa_de_servicos)*hospedagem_clientes;
            	ganho_do_hotel = ganho_do_hotel + totalconta;

				vagas_ocupadas++;
				printf("\nCliente: %s\n-------------\nTotal da conta: R$%.2f", nomeHT, totalconta);

				char continuar;
				printf("\n\nDeseja continuar? [S] ou [N]\n");
				scanf(" %c", &continuar);

				while (continuar != 'S' && continuar != 's' && continuar != 'N' && continuar != 'n') {
					printf("\n\nOpção inválida. Digite [S] ou [N]\n");
					scanf(" %c", &continuar);
				}

				if ((continuar == 'N') || (continuar == 'n')) {
					break;
				}
			}
			
			printf("\n\nO lucro total do hotel foi: R$%.2f", ganho_do_hotel);

			
		}


		else if (strcmp(opcao1, "3") == 0){
			system("cls");
			printf("\n\n------------------------------------------------\nMultiplicacao\n------------------------------------------------\n");
			
			float variavelmultiplicacao;
			printf("\nDigite o numero que você deseja multiplicar: ");
			scanf("%f", &variavelmultiplicacao);
			
			int multiplicacao;
			printf("\nInforme quantas vezes voce deseja multiplicar esse numero: ");
			scanf("%d", &multiplicacao);

			float produto = 0;
			
			for (int i=0; i<multiplicacao; i++){
				produto = produto + variavelmultiplicacao;
			}

        printf("\nO resultado da multiplicacao eh: %.1f", produto);
		}
//-------------------------------------------------------------------------------------------------------------------------------------		
		else if (strcmp(opcao1, "4") == 0){
			system("cls");
			printf("\n\n------------------------------------------------\nQÍmpares e QPares\n------------------------------------------------\n");

			int QPares = 0, QImpares = 0, condicao = 1;
			
			while (condicao == 1){
				int verificador;
				printf("\nDigite um numero - [9999] para sair: ");
				scanf("%d", &verificador);
				
				if (verificador == 9999){
					break;
				}
				
				if (verificador % 2 == 0){
					printf("\nEsse numero eh par");
					QPares = QPares + 1;
				}
				else{
					printf("\nEsse numero eh impar");
					QImpares = QImpares + 1;
				}
			
			}		
			printf("\nO total de numeros pares eh de: %d", QPares);
			printf("\nO total de numeros impares eh de: %d", QImpares);
		}
//-------------------------------------------------------------------------------------------------------------------------------------	

		else if (strcmp(opcao1, "5") == 0) {
			system("cls");
			int condicao = 1,  contadoralunos = 0 ;
			float percentual1, percentual2, percentual3, contadorpercen1 = 0, contadorpercen2 = 0, contadorpercen3 = 0;
			while (condicao == 1){
				printf("\n\n------------------------------------------------\nPesquisa RU\n------------------------------------------------\n");
				printf("\nSeja bem vindo a pesquisa de utilizacao do RU! ");

				printf("\nCom que frequencia voce utilizou o RU no ultimo mes? - [9999] para parar: ");
				
				int pesquisaAlunos;
				scanf("%d", &pesquisaAlunos);
				system("cls");

				if(pesquisaAlunos == 9999){
					break;
				}
				
				contadoralunos++;

				if (pesquisaAlunos < 10){
                	contadorpercen1++;
				}
				else if ((pesquisaAlunos >= 10) && (pesquisaAlunos <= 15)){
					contadorpercen2++;
				}
				else if (pesquisaAlunos > 15){
					contadorpercen3++;
				}

				percentual1 = (contadorpercen1/contadoralunos)*100;
				percentual2 = (contadorpercen2/contadoralunos)*100;
				percentual3 = (contadorpercen3/contadoralunos)*100;
			}
				printf("------------------------------------------------");
				printf("\nO percentual de pessoas que utilizaram menos de 10 vezes eh de %.2f porcento", percentual1);
				printf("\nO percentual de pessoas que utilizaram entre 10 e 15 vezes eh de %.2f porcento", percentual2);
				printf("\nO percentual de pessoas que utilizaram mais de 15 vezes eh de %.2f porcento", percentual3);

		}

		else if (strcmp(opcao1, "6") == 0){
			system("cls");
			int contadorsexoM = 0, contadorsexoF = 0 , azuis = 0, verdes = 0, castanhos = 0, condicao = 1;
			int louros = 0, castanhosC = 0, pretos = 0, contadorverdelouro = 0, contadorMulheres = 0, maioridade = 0;
			
			
			while (condicao == 1){
				
				printf("\n\n------------------------------------------------\nPesquisa populacao\n------------------------------------------------\n");
				printf("\nSeja bem vindo a pesquisa de populacao! ");
				
				int idadePesquisa;
				printf("\n------------------------------------------------\nQual sua idade? [-1] para parar: ");
				fflush(stdin);
				scanf("%d", &idadePesquisa);
				if (idadePesquisa == -1){
					break;
				}
				if (maioridade < idadePesquisa){
					maioridade = idadePesquisa;
				}
				char sexopopulacao;
				printf("\n------------------------------------------------\nQual o seu sexo? [m] ou [f]: ");
				fflush(stdin);
				scanf("%c", &sexopopulacao);
				
				if (sexopopulacao == 'f'){
					contadorsexoF++;
				}
				else if (sexopopulacao == 'm'){
					contadorsexoM++;
				}
				else{
					printf("\nOpcao invalida!");
				}
				char cordosolhos;
				printf("\n------------------------------------------------\nQual a cor de seus olhos? \n1 - Azuis\n2 - Verdes\n3 - Castanhos: ");
				fflush(stdin);
				scanf("%c", &cordosolhos);

				if (cordosolhos == '1'){
					azuis++;
				}
				else if (cordosolhos == '2'){
					verdes++;
				}
				else if (cordosolhos == '3'){
					castanhos++;
				}
				else{
					printf("\nOpcao invalida!");
				}
				char cordosCabelos;
				printf("\n------------------------------------------------\nQual a cor dos seus cabelos? \n1 - Louros\n2 - Castanhos\n3 - Pretos: ");
				fflush(stdin);
				scanf("%c", &cordosCabelos);
				//system("cls");

				if (cordosCabelos == '1'){
					louros++;
				}
				else if (cordosCabelos == '2'){
					castanhosC++;
				}
				else if (cordosCabelos == '3'){
					pretos++;
				}
				else{
					printf("Opcao invalida!");
				}
				
				if ((idadePesquisa >= 18) && (idadePesquisa <=  35) && (sexopopulacao == 'f')){
					contadorMulheres++;
				}

				if ((cordosCabelos == '1') && (cordosolhos == '2')){
					contadorverdelouro++;
				}
			}

			printf("\n------------------------------------------------\nA maior idade foi: %d", maioridade);
			printf("\nA quantidade de mulheres com a idade entre 18 e 35 anos eh de: %d", contadorMulheres);
			printf("\nA quantidade de individuos com cabelos verdes e louros eh de: %d", contadorverdelouro);
		}

	else if(strcmp(opcao1, "7") == 0){/*Escreva um programa que exiba uma lista de opções (menu): adição, subtração, 
	divisão, multiplicação e sair. Imprima o cálculo da operação escolhida. Repita até que a opção saída seja escolhida.*/
		system("cls");
		printf("\n\n------------------------------------------------\nCalculadora\n------------------------------------------------\n");
		int condicao = 1;
		while (condicao == 1){
			printf("\n1 - Soma\n2 - Subtracao\n3 - Multiplicacao\n4 - Divisao\n0 - Sair\n");
			fflush(stdin);
			printf("\nEscolha uma opcao: ");
			char opcaocalc;
			scanf("%c", &opcaocalc);
			system("cls");
			
			printf("\nDigite o termo A: ");
			float termoAcalc, termoBcalc;
			scanf("%f", &termoAcalc);
			printf("\nDigite o termo B: ");
			scanf("%f", &termoBcalc);
			
			if (opcaocalc == '0'){
				break;
			}

			else if (opcaocalc == '1'){
				float somcalc;
				somcalc = termoAcalc + termoBcalc;
				printf("\nA soma de A e B eh %.2f", somcalc);
			}
			else if (opcaocalc == '2'){
				float subcalc;
				subcalc = termoAcalc - termoBcalc;
				printf("\nA subtracao de A e B eh %.2f", subcalc);
			}
			else if(opcaocalc == '3'){
				float mulcalc;
				mulcalc = mulcalc + termoBcalc;
				printf("\nA multiplica entre A e B eh %.2f", mulcalc);
			}
			else if(opcaocalc == '4'){
				float divcalc;
				divcalc = termoAcalc + termoBcalc;
				printf("\nA divisao entre A e B eh %.2f", divcalc);
			}
		}
	}
    else if (strcmp(opcao1, "8") == 0){
		system("cls");
		/*Faça um algoritmo que escreva os números pares entre 100 e 200.*/
		printf("\n\n------------------------------------------------\nPares\n------------------------------------------------\n");
		for (int i = 100; i<=200; i = i + 2){
			printf("|%d| ", i);
		}
	}
	else if(strcmp(opcao1, "9") == 0){
		system("cls");
		/*Num frigorífico existem 100 bois. Cada boi traz em seu pescoço um cartão contendo seu 
		número de identificação e seu peso. Faça um algoritmo que escreva o número de identificação do boi e o 
		peso do boi mais gordo e do boi mais magro.*/

		int pesoboi, boigordo = 0, boimagro = 9999, idboi, idboigordo, idboimagro;
		
		for (int i=0; i<=100; i++){
			printf("\nDigite o numero de indentificacao do boi - [0] parar: ");
			fflush(stdin);
			scanf("%d", &idboi);
			while (idboi>100){
				
				if (idboi > 100){
				printf("\n\nID invalido!");
				}
				
				printf("\nDigite o numero de indentificacao do boi - [0] parar: ");
				fflush(stdin);
				scanf("%d", &idboi);
			}
			if(idboi == 0){
				break;
			}
			system("cls");
			printf("\nDigite o peso do boi em kg: ");
			
			scanf("%d", &pesoboi);
			
			if(boigordo < pesoboi){
				boigordo = pesoboi;
				idboigordo = idboi;
			}

			if(boimagro > pesoboi){
				boimagro = pesoboi;
				idboimagro = idboi;
			}
		}
		printf("\nO boi mais gordo eh o de id |%d|, que pesa: %dkg", idboigordo, boigordo);
		printf("\nO boi mais magro eh o de id |%d|, que pesa: %dkg", idboimagro, boimagro);
		
	}

	else if (strcmp(opcao1, "10") == 0){
			/*Foi realizada uma pesquisa de algumas características físicas da população de uma região, a qual coletou os seguintes dados referentes a cada habitante para ser analisado:

			Sexo (M - masculino / F - feminino);

			Cor dos olhos (1-azuis, 2-verdes ou 3-castanhos);

			Cor dos cabelos (1-louros, 2-castanhos, 3-pretos);

			Idade;

			Renda mensal.

			Obs: O final do conjunto de habitantes é reconhecido pelo valor -1 informado como i. Com base nestas informações, escrever um programa que determine e escreva:

			A maior idade dos habitantes do grupo pesquisado; ok

			A média da idade dos habitantes; ok

			A quantidade de indivíduos do sexo masculino e feminino (separadamente); ok

			A quantidade de indivíduos do sexo feminino que está entre 18 e 35 anos de idade e que tenham olhos verdes e cabelos louros; ok

			A porcentagem de indivíduos que recebem até 3 salários mínimos mensais. ok*/

			
			int contadorsexoM = 0, contadorsexoF = 0 , azuis = 0, verdes = 0, castanhos = 0, condicao = 1;
			int louros = 0, castanhosC = 0, pretos = 0, contadorMulheres = 0, maioridade = 0;
			float rendapopu, mediaIdade, acumuladorIdade=0.0, porcenIdade, acumRenda=0.0;
			
			while (condicao == 1){
				system("cls");
				printf("\n\n------------------------------------------------\nPesquisa populacao 2\n------------------------------------------------\n");
				printf("\nSeja bem vindo a pesquisa de populacao! ");
				
				int idadePesquisa;
				printf("\n------------------------------------------------\nQual sua idade? [-1] para parar: ");
				fflush(stdin);
				scanf("%d", &idadePesquisa);
				if (idadePesquisa == -1){
					break;
				}
				if (maioridade < idadePesquisa){
					maioridade = idadePesquisa;
				}
				printf("\n------------------------------------------------\nQual sua renda?: R$");
				scanf("%f", &rendapopu);

				if (rendapopu > 3960){
					acumRenda = acumRenda + 1;
					
				}
				
				char sexopopulacao;
				printf("\n------------------------------------------------\nQual o seu sexo? [m] ou [f]: ");
				fflush(stdin);
				scanf("%c", &sexopopulacao);
				
				if (sexopopulacao == 'f'){
					contadorsexoF++;
				}
				else if (sexopopulacao == 'm'){
					contadorsexoM++;
				}
				else{
					printf("\nOpcao invalida!");
				}
				char cordosolhos;
				printf("\n------------------------------------------------\nQual a cor de seus olhos? \n1 - Azuis\n2 - Verdes\n3 - Castanhos: ");
				fflush(stdin);
				scanf("%c", &cordosolhos);

				if (cordosolhos == '1'){
					azuis++;
				}
				else if (cordosolhos == '2'){
					verdes++;
				}
				else if (cordosolhos == '3'){
					castanhos++;
				}
				else{
					printf("\nOpcao invalida!");
				}
				char cordosCabelos;
				printf("\n------------------------------------------------\nQual a cor dos seus cabelos? \n1 - Louros\n2 - Castanhos\n3 - Pretos: ");
				fflush(stdin);
				scanf("%c", &cordosCabelos);
				//system("cls");

				if (cordosCabelos == '1'){
					louros++;
				}
				else if (cordosCabelos == '2'){
					castanhosC++;
				}
				else if (cordosCabelos == '3'){
					pretos++;
				}
				else{
					printf("Opcao invalida!");
				}
				
				if ((idadePesquisa >= 18) && (idadePesquisa <=  35) && (sexopopulacao == 'f') && (cordosCabelos == '1') && (cordosolhos == '2')){
					contadorMulheres++;
				}
				
				acumuladorIdade = acumuladorIdade + idadePesquisa;
			}
			mediaIdade = acumuladorIdade/(contadorsexoM + contadorsexoF);
			porcenIdade = (acumRenda / (contadorsexoM + contadorsexoF))*100;
			printf("\n------------------------------------------------\nA maior idade foi: %d", maioridade);
			printf("\nA media de idade dos habitantes eh de: %.2f", mediaIdade);
			printf("\nQuantidade de individuos do sexo masculino: %d", contadorsexoM);
			printf("\nQuantidade de individuos do sexo feminino: %d", contadorsexoF);
			printf("\nA quantidade de mulheres com a idade entre 18 e 35 anos com cabelos louros e olhos verdes eh de: %d", contadorMulheres);
			printf("\nA porcentagem de individuos que recebem mais de 3 salarios minimos eh de %.2f porcento", porcenIdade);
		}
	else if(strcmp(opcao1, "11") == 0){
		/*Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.*/
		
		int condicao = 1;

		while (condicao == 1){
			printf("\n\n------------------------------------------------\nSenha\n------------------------------------------------\n");
			
			printf("\nDigite um nome de usuario: ");
			char nomeUsuario[20];
			fflush(stdin);
			scanf("%s", nomeUsuario);
		
			printf("\nDigite uma senha: ");
			char senhaUsuario[20];
			fflush(stdin);
			scanf("%s", senhaUsuario);
			system("cls");

			if (strcmp(nomeUsuario, senhaUsuario)==0){
				printf("\nDados invalidos! Digite novamente: \n");
			}
			else {
				printf("\nConta criada com sucesso. ");
				condicao = 0;
			}

		}
		
	}
	else if (strcmp(opcao1, "12")==0){
		/*O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. 
		O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. 
		O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
		Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
		
		Lojas Tabajara
		1. Produto 1: R$ 2.20
		2. Produto 2: R$ 5.80
		3. Produto 3: R$ 0
		4. Total: R$ 9.00
		5. Dinheiro: R$ 20.00
		6. Troco: R$ 11.00*/

		printf("\n\n------------------------------------------------\nLojas Tabajara\n------------------------------------------------\n");
		float precoproduto1, precoproduto2, precoproduto3, valorpagodinheiro, totalcompratabajara, trocotabajara;
		
		int condicao = 1;
		
		while (condicao == 1){
			while (condicao == 1){

				printf("\nInforme o preco do produto 1 - [0] parar R$: ");
				scanf("%f", &precoproduto1);
				if (precoproduto1 == 0.0){
					break;
				}
				
				printf("\nInforme o preco do produto 2 - [0] parar R$: ");
				scanf("%f", &precoproduto2);
				if (precoproduto2 == 0.0){
					break;
				}

				printf("\nInforme o preco do produto 3 - [0] parar R$: ");
				scanf("%f", &precoproduto3);
				if (precoproduto3 == 0.0){
					break;
				}
			}
		
			printf("\n------------------------------------");
			printf("\nInforme o valor pago em dinheiro: ");
			scanf("%f", &valorpagodinheiro);
			totalcompratabajara = precoproduto1 + precoproduto2 + precoproduto3;
			trocotabajara = valorpagodinheiro - totalcompratabajara;

			printf("\n--------TOTAL--------");
			printf("\nProduto 1:   R$ %.2f", precoproduto1);
			printf("\nProduto 2:   R$ %.2f", precoproduto2);
			printf("\nProduto 3:   R$ %.2f", precoproduto2);
			printf("\nValor total: R$ %.2f", totalcompratabajara);
			printf("\nDinheiro: R$ %.2f", valorpagodinheiro);
			printf("\nTroco: R$ %.2f", trocotabajara);
			printf("\n------------------------------------");
			printf("\n\nDeseja limpar prosseguir para proxima compra? [s] ou [n]: ");
			
			char retornartabajara;
			fflush(stdin);
			scanf("%c", &retornartabajara);

			if (retornartabajara == 's'){
				system("cls");
			}

			else if(retornartabajara == 'n'){
				system("cls");
				printf("\nObrigado por comprar na loja tabajara!");
				condicao = 0;
			}
			else{
				printf("\nOpcao invalida!");
			}
			
		}
	}

	else if(strcmp(opcao1, "13") == 0){
		/*O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto 
		indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas. (use o valor 999 para encerrar)*/
		int condicao = 1;
		float acumTemp = 0.0, menorTemp = 9999, maiorTemp = 0.0, mediaTemp, acumMeteo = 0.0;
		while (condicao == 1){
			system("cls");
			printf("\n\n------------------------------------------------\nDepartamento de Meteorologia\n------------------------------------------------\n");
			printf("\nInforme a temperatura: ");
			float tempMeteo;
			scanf("%f", &tempMeteo);

			if (tempMeteo == 999){
				break;
			}

		
			acumMeteo ++;
			acumTemp = acumTemp + tempMeteo;

			if (maiorTemp<tempMeteo){
				maiorTemp = tempMeteo;
			}

			if (menorTemp>tempMeteo){
				menorTemp = tempMeteo;
			}
		}

		mediaTemp = acumTemp/acumMeteo;
		printf("\nA maior temperatura lida foi: %.2f", maiorTemp);
		printf("\nA menor temperatura lida foi: %.2f", menorTemp);
		printf("\nA media das temperaturas lidas eh de: %.2f", mediaTemp);


	}
	else if(strcmp(opcao1, "14") == 0){
		system("cls");
		printf("\n\n------------------------------------------------\nTabuada\n------------------------------------------------\n");
		printf("\nInforme um numero: ");
		int numTabuada, tabuada;
		scanf("%d", &numTabuada);
		
		int contadorTabuada = 1;
		for(int i=0;i<10;i++){
			
			tabuada = numTabuada * contadorTabuada;
			printf("\n%d x %d = %d",numTabuada, contadorTabuada, tabuada );
			contadorTabuada++;
		}
	}
	else if(strcmp(opcao1, "15") == 0){
		system("cls");
		printf("\n\n------------------------------------------------\nPotencia e Divisao\n------------------------------------------------\n");
		char escolhaPD;
		printf("\nEscolha um programa a ser executado - [1] Potencia [2] Divisao: ");
		fflush(stdin);
		scanf("%c", &escolhaPD);

		if (escolhaPD == '1'){
		/*(Hard)-Faça uma um programa que computa a potência a^b para valores a e b (assuma números inteiros) passados por parâmetro (não use o operador **)*/
		system("cls");
		printf("\nDigite um numero: ");
		int base;
		scanf("%d", &base);

		printf("\nDigite o expoente: ");
		int expoente;
		scanf("%d", &expoente);
		int poten = 1;
		for (int i=0; i<expoente; i++){
			poten = poten * base;
		}

		printf("\nO resultado de %d elevado a %d eh %d", base, expoente, poten);
		}

		else if (escolhaPD == '2'){
			/*(Hard)-Sem utilizar a operação de divisão, escreva um programa que divida dois números inteiros. Pelo algoritmo da subtração sucessiva.*/
			int dividend, divisor, quociente = 0;
			printf("\nDigite o dividendo: ");
			scanf("%d", &dividend);
			printf("\nDigite o divisor: ");
			scanf("%d", &divisor);
			
			while (dividend >= divisor) {
				dividend -= divisor;
				quociente++;
    		}
   			 printf("\nO resultado da divisao eh: %d", quociente);
		}
		else {
			printf("\nOpcao invalida!");
		}

	}


	else{
        printf("\nOpcao invalida!");
	}       
	return 0;
}

//--------------------------------------------------------------------------------------------------------------------------------------
//Conjunto 2
void menuProgramas2(){
	printf("1 - Funcao Nome\n2 - Funcao Par Impar\n3 - Funcao Produto\n4 - Funcao Calculadora\n5 - Funcao True False");
	printf("\n6 - Funcao somaImposto\n7 - Funcao Valor Absoluto\n8 - Funcao FizzBuzz\n9 - Funcao Dobro do Maior Numero");
	printf("\n10 - Funcao Prestacoes");
}

//Atividades de funcoes---------------------------------------------------------------------------------------------------------------- 
//atv1
char nomeF[20];
int idadeF;
int nome (char nomeF[20], int idadeF){
			printf("\n%s possui %d anos", nomeF, idadeF);
			return 0;
		}

//atv2
int parImparF;
int parImpar (int parImparF){
	if (parImparF % 2 == 0){
		printf("\n%d eh par", parImparF);
	}
	else{
		printf("\n%d eh impar", parImparF);
	}
	return 0;
}

//atv3
int prod1, prod2, prod3, resultP;
int produto (int prod1, int prod2, int prod3){
	resultP = prod1 * prod2 * prod3;
	printf("O resultado de %d x %d x %d eh: %d", prod1, prod2, prod3, resultP);
	return 0;
}

//atv4
int termo1c, termo2c, resultadoC;
char opC;
int calculadora (int termo1c, int termo2c, char opC){
	if (opC == '+'){
		resultadoC = termo1c + termo2c;
		printf("A soma de %d e %d eh: %d", termo1c, termo2c, resultadoC);
	}

	if (opC == '-'){
		resultadoC = termo1c - termo2c;
		printf("A subtracao de %d e %d eh: %d", termo1c, termo2c, resultadoC);
	}

	if (opC == '*'){
		resultadoC = termo1c * termo2c;
		printf("A multiplicacao de %d e %d eh: %d", termo1c, termo2c, resultadoC);
	}

	if (opC == '/'){
		resultadoC = termo1c / termo2c;
		printf("A divisao de %d e %d eh: %d", termo1c, termo2c, resultadoC);
	}
	return 0;
}

//atv5
int termo1t, termo2t;
int truefalse (int termo1, int termo2){
	return termo1 % termo2 == 0;
}

//atv6
float custoProdutoSI, impostoSI;
int somaImposto(float custo, float imposto){
	float reducao = imposto/100;
	float total = custo + custo * reducao;
	printf("\nO valor total somando impostos eh: R$ %.2f", total);
	return 0;
}

//atv7
int numAbso;
int valorAbsoluto (int numeroAbso){
	int valorAbso = abs(numeroAbso);
	printf("\nO valor absoluto de %d eh %d", numAbso, valorAbso);
	return 0;
}

//atv8
int FizzBuzz;
int Fizz (int Buzz){
	for(int i=0; i<Buzz; i++){
		
		if((i % 5 == 0) && (i % 3 == 0)){
			printf("\nFizzBuzz");
		}
		else if((i % 3 == 0) && (i!= 0)){
			printf("\nFizz");
		}

		else if((i % 5 == 0) && (i!= 0)){
			printf("\nBuzz");
		}

		else if ((i % 5 != 0) && (i % 3 != 0)){
			printf("\n%d", i);
		}
	}
	return 0;
}

//atv9
int num1DM, num2DM, num3DM;
int maiorDM (int num1DM, int num2DM, int num3DM){
	if ((num1DM>num2DM)&&(num2DM>num3DM)){
		return num1DM;
	}
	else if ((num2DM>num3DM)&&(num3DM>num1DM)){
		return num2DM;
	}
	else{
		return num3DM;
	}
}
int dobroDM(int maiorDM){
	int dobro = maiorDM * 2;
	return dobro;	
}

//atv10
float prestacaoFP, diasAtrasoFP, acumuladorVP = 0;
int valorPagamento (float prestacao, float atraso){
	float totalVP = 0;
	if (atraso>0){
		totalVP = prestacao + (prestacao*0.03 + 0.01*atraso);
		printf("\nO valor a ser pago eh: R$ %.2f\n\n", totalVP);
		acumuladorVP = acumuladorVP + totalVP;
	}
	else{
		printf("\nO valor a ser pago eh: R$ %.2f\n\n", prestacao);
		acumuladorVP = acumuladorVP + prestacao;
	}
	return 0;
}

int programas2(char opcao2[3]){
	if (strcmp(opcao2, "1") == 0){
		/*Faça um programa que solicite o nome do usuário e a idade do 
		usuário, depois disso exiba a mensagem: "{nome} possui {idade} anos.". Esta mensagem deve ser escrita em uma função.*/
		system("cls");
		printf("\n------------------------------------------------\nNome\n------------------------------------------------\n");
		printf("\nDigite seu nome: ");
		scanf("%s", nomeF);

		printf("\nDigite sua idade: ");
		scanf("%d", &idadeF);


		nome(nomeF, idadeF);
	}

	else if(strcmp(opcao2, "2") == 0){
		/*Crie uma função chamada "par_ou_impar" que receba um número como parâmetro e retorne se o número é par ou ímpar.*/
		system("cls");
		printf("\n------------------------------------------------\nPar Impar\n------------------------------------------------\n");
		printf("\nDigite um numero: ");
		scanf("%d", &parImparF);
		parImpar(parImparF);
	}

	else if(strcmp(opcao2, "3") == 0){
		/*Fazer uma função que recebe três argumentos, e que retorne o produto desses três argumentos.*/
		system("cls");
		printf("\n------------------------------------------------\nProduto\n------------------------------------------------\n");
		printf("\nDigite 3 numeros:\n");
		scanf("%d%d%d", &prod1, &prod2, &prod3);
		produto(prod1, prod2, prod3);

	}
	
	else if(strcmp(opcao2, "4") == 0){
		/*Crie uma função chamada "calculadora" que receba dois números e uma operação 
		matemática (soma, subtração, multiplicação ou divisão) como parâmetros e retorne o resultado da operação escolhida.*/
		system("cls");
		printf("\n------------------------------------------------\nCalculadora\n------------------------------------------------\n");
		printf("\nDigite 2 numeros e um operador:\n");
		scanf("%d%d", &termo1c, &termo2c);
		fflush(stdin);
		scanf("%c", &opC);
		calculadora(termo1c, termo2c, opC);
	}

	else if(strcmp(opcao2, "5") == 0){
		/*Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
		Valores esperados:*/
		system("cls");
		printf("\n------------------------------------------------\nTrue False\n------------------------------------------------\n");
		printf("\nDigite dois numeros:\n");
		scanf("%d%d", &termo1t, &termo2t);
		int funcao = truefalse(termo1t, termo2t);
		
		if (funcao == 1){
			printf("\nTrue");
		}
		else{
			printf("\nFalse");
		}
	}

	else if(strcmp(opcao2, "6") == 0){
		/*Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
		taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, 
		que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.*/
		printf("\n------------------------------------------------\nsomaImposto\n------------------------------------------------\n");
		printf("\nDigite o valor de custo do produto: ");
		scanf("%f", &custoProdutoSI);
		printf("\nDigite o valor do imposto do produto: ");
		scanf("%f", &impostoSI);

		somaImposto(custoProdutoSI, impostoSI);

	}
	
	else if(strcmp(opcao2, "7") == 0){
		/*Escreva uma função para imprimir o valor absoluto de um número.*/
		system("cls");
		printf("\n------------------------------------------------\nValor Absoluto\n------------------------------------------------\n");
		printf("\nDigite um numero: ");
		scanf("%d", &numAbso);
		valorAbsoluto(numAbso);
	}
	
	else if(strcmp(opcao2, "8") == 0){
		/*Escreva uma função que recebe um número como parâmetro e para cada número menor que o parâmetro, 
		a função imprime "Fizz" se o número for múltiplo de três, imprime "Buzz" se o número for múltiplo de cinco, 
		e imprime "FizzBuzz" se o número for múltiplo de três e cinco. Caso o número não seja múltiplo nem de três nem de cinco, 
		ele deve ser impresso. Note que, ao contrário das funções anteriores, 
		sua função não deve retornar nada. Ela precisa simplesmente imprimir o que foi pedido.*/
		system("cls");
		printf("\n------------------------------------------------\nFizzBuzz\n------------------------------------------------\n");
		printf("\nDigite um numero: ");
		scanf("%d", &FizzBuzz);
		Fizz(FizzBuzz);
	}

	else if(strcmp(opcao2, "9") == 0){
		/*Faça um programa que solicite ao usuário três números diferentes e exiba o dobro do maior número. Para fazer 
		isso separe seu código em duas funções diferentes: Uma função para retornar o maior dos três números e outra 
		função para dobrar o número.*/
		system("cls");
		printf("\n------------------------------------------------\nDobro do Maior Numero\n------------------------------------------------\n");
		printf("\nDigite 3 numeros:\n");
		scanf("%d%d%d", &num1DM, &num2DM, &num3DM);
		int variDM = maiorDM(num1DM, num2DM, num3DM);
		int variDB = dobroDM(variDM);
		printf("\nO dobro do maior dos numeros fornecidos eh: %d", variDB);
	}

	else if(strcmp(opcao2, "10") == 0){
		/*Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
		O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a 
		função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa 
		deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação 
		e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser 
		encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
		O cálculo do valor a ser pago é feito da seguinte forma. 
		
		Para pagamentos sem atraso, cobrar o valor da prestação. 
		Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.*/
		int condicao = 1, contador = 0;
		while (condicao == 1){
			system("cls");
			printf("\n------------------------------------------------\nPrestacoes\n------------------------------------------------\n");
			printf("\nInforme o valor da prestacao - [0] para parar: R$ ");
			scanf("%f", &prestacaoFP);
			
			if (prestacaoFP == 0){
				condicao = 0;
			}	
			if(condicao!=0){
				printf("\nInforme a quantidade de dias em atraso: ");
				scanf("%f", &diasAtrasoFP);
				valorPagamento(prestacaoFP, diasAtrasoFP);
				system("pause");
				contador ++;
			}
			
		}

		printf("\n\nQuantidade de parcelas pagas: %d\nValor total de prestacoes pagas: R$ %.2f", contador, acumuladorVP);
	}
	
	else{
		printf("\nOpcao invalida!");
	}
	return 0;	
}

void menuProgramas3(){
	printf("1 - ...");
}

int programas3(char opcao3[3]){
	if (strcmp(opcao3, "1") == 0){
		/*Gere uma lista de contendo os múltiplos de 3 entre 1 e 50.*/
		int lista[16];
		int contador = 0;
		
		for (int i = 1; i<=50; i++){
			
			if (i % 3 == 0){
				lista[contador] = i;  //CORRIGIR BUG
			}		
			contador ++;
		}

		for (int contador = 0; contador<16; contador++){
			printf("Lista: %d\n", lista[contador]);
		}
	}

	else{
		printf("\nOpcao invalida!");
	}
	return 0;
}

//--------------------------------------------------------------------função do programa principal----------------------------------------------------------------------------------------
int main (){
	printf("Seja bem vindo ao CodeV3 em C!!\n\
      \nEsse programa serve para guardar todas as atividades do Senac em C.\n"
      );
	
	
//Estrutura de Repetição --------------------------------------------------------------------------------------------------------------
	int condicao = 1;
	while (condicao == 1){
	

	    printf("\n------------------------------------------------\n");
	    menuConjuntos();
	    printf("\n------------------------------------------------\n");
	
	//Conjuntos de atividades  
	    char conjuntos, opcao1[3], opcao2[3], opcao3[3];
		printf("\nPor favor escolha um conjunto - [0] para sair: ");
	    fflush(stdin);
		scanf(" %c", &conjuntos);
		system("cls");
	    
		if (conjuntos == '0'){
			break;
		}
	    else if (conjuntos == '1'){
	    	printf("\n------------------------------------------------\n");
			menuProgramas1();
			printf("\n------------------------------------------------\n");
			printf("\nEscolha uma opcao: ");
			fflush(stdin);
			scanf(" %s", opcao1);
			system("cls");
	        programas1(opcao1);
		}
		else if(conjuntos == '2'){
	    	printf("\n------------------------------------------------\n");
			menuProgramas2();
			printf("\n------------------------------------------------\n");
			printf("\nEscolha uma opcao: ");
			fflush(stdin);
			scanf(" %s", opcao2);
			system("cls");
	        programas2(opcao2);
		}
		else if(conjuntos == '3'){
	    	printf("\n------------------------------------------------\n");
			menuProgramas3();
			printf("\n------------------------------------------------\n");
			printf("\nEscolha uma opcao: ");
			fflush(stdin);
			scanf(" %s", opcao3);
			system("cls");
	        programas3(opcao3);
		}
	//Retornar ao menu---------------------------------------------------------------------------------------------------------------------          
		int retornar = 1;
		char voltar;
		while (retornar == 1){
		
	        printf("\n------------------------------------------------");
	        printf("\nDeseja retornar ao menu principal? [s] ou [n]: ");
	        scanf(" %c", &voltar);
	        
			if ((voltar == 's') || (voltar == 'S')){
				printf("\nRetornando...");
		        break;
			}
	            
	        else if ((voltar == 'n') || (voltar == 'N')){
				printf("\nObrigado por utilizar o CodeV3!\n");
	            condicao = 0;
	            break;
			}
	            
	        else{
	            printf("\nDigite uma opcao valida!");
	        }
		}
	}	
return 0;	
}