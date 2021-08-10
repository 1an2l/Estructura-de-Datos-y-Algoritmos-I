#include<stdio.h>
#include<windows.h>

/*
 * Autor:Sánchez Estrada Angel Isaac
 * Nacionalidad: Mexicana
 * Fecha de elaboración: 12-03-2021
 * Ultima modificación: 14-03-2021
 * Sistema Operativo: Windows 10
*/

/*
	Programa que realiza la funcion de un sudoku definido
	en el programa
	Incluye:
	-La posibilidad de ver el sudoku sin resolver por si gusta hacerlo en papel
	-La posibilidad de resolverlo en el programa
	-La posibilidad de ver el resultado para realizar una comparación con los 
	 resultados que optuvieron
*/

//Declaracion de funciones
void sudoku();
void descifrarSudoku();
void resuelto();

int main(){
	
	//Declaración de variablesz
	char ao=162, aa=160, au=163;
    short op1=0;
	
	//Titulo del programa
	printf("\n\t*** Bienvenido a el Sudoku en C ***\n\n");
	
	//Menú del programa
	printf("Elija una opci%cn del men%c\n", ao, au);
	printf("  1) Mostrar Sudoku sin Resolver\n");
	printf("  2) Resolver Sudoku en este Programa\n");
	printf("  3) Respuesta Correcta del Sudoku\n");
	printf("  4) Salir\n");
	printf("Elige una opci%cn: ",ao);
	scanf("%d", &op1);
	//Swich para ejecutar la opcion guardada en op1
	switch(op1){
		case 1:
			sudoku();
			break;
		case 2:
			descifrarSudoku();
			break;
		case 3:
			resuelto();
			break;
		case 4:
			return 0;
		default:
			printf("Opci%cn no v%clida.\n",ao ,aa);
		return 0;
 }

 return 0;
}
void sudoku(){
	system("cls");//Funcion del sistema para limpiar pantalla
	//Declaracion de matriz sin resolver
	int matriz[9][9] = {{0,8,0,0,0,0,0,0,9},{0,0,0,8,0,4,3,6,0},{0,5,0,0,6,3,2,0,1},{0,0,0,0,2,0,6,0,0},{0,6,2,0,8,5,0,0,0},{0,4,0,6,7,0,0,0,0},{0,0,7,0,0,0,0,9,0},{0,2,0,0,0,0,4,5,7},{0,3,8,9,4,0,0,2,0}};
	//Declaracion de variables
	int i, j;
	int opcion=0,op2;
	
	//Declariacion de carateres a ocupar
	char ao=162, aa=160, au=163, sp=168;
	
	printf("\nSudoku sin Resolver\n");
	printf("====================\n\n");
	printf("(Si desea resolver el Sudoku en el programa\n""porfavor dirigase a la opci%cn 2 del men%c)\n\n",ao ,au);
	//Muestra el sudoku sin resolver
	for (i=0 ; i<9 ; i++)
	{
		for (j=0 ; j<9 ; j++)
		{
			printf(" %d ",matriz[i][j]);
			if ( j==2 || j==5 )
				printf(" | ");
		}
		printf("\n");
		if ( i==2 || i==5 )
			printf(" -- -- -- |  -- -- -- |  -- -- --\n");
	}
	printf("\n");
	//funcion para regresar al menu cuando se dese ya no ver el sudoku sin resolver
	printf("\nSi deseas dejar de ver el Sudoku coloca 1 y despues enter ",sp); 
	scanf("%d",&op2);
	//Funcion que permite que hasta que se ponga el numero 1 no salga
	if (op2==1)
	{
	main();
	}
}

void descifrarSudoku(){
	//Declaracion de variables
	int *reng,*colu,ren=5,valor=9; 	
	int opcion=0,op2;
	//Declaracion de matrices
	int matriz[9][9] = {{0,8,0,0,0,0,0,0,9},{0,0,0,8,0,4,3,6,0},{0,5,0,0,6,3,2,0,1},{0,0,0,0,2,0,6,0,0},{0,6,2,0,8,5,0,0,0},{0,4,0,6,7,0,0,0,0},{0,0,7,0,0,0,0,9,0},{0,2,0,0,0,0,4,5,7},{0,3,8,9,4,0,0,2,0}};
	int mres[9][9] = {{3,8,6,5,1,2,7,4,9},{2,7,1,8,9,4,3,6,5},{9,5,4,7,6,3,2,8,1},{7,9,5,4,2,1,6,3,8},{1,6,2,3,8,5,9,7,4},{8,4,3,6,7,9,5,1,2},{4,1,7,2,5,6,8,9,3},{6,2,9,1,3,8,4,5,7},{5,3,8,9,4,7,1,2,6}};
	int i, j,a;
	
	//Declaracion de caracteres
	char ao=162, aa=160, au=163, sp=168;
	
	reng=&i;
	colu=&j;

	system("cls");//Funcion para limpiar pantalla
	//Titulo
	printf("\nSudoku a Resolver\n");
	printf("=================\n\n");
	//Código para mostrar sudoku antes de resolver
	for (i=0 ; i<9 ; i++)
	{
		for (j=0 ; j<9 ; j++)
		{
			printf(" %i ",matriz[i][j]);
			if ( j==2 || j==5 )
				printf(" | ");
		}
		printf("\n");
		if ( i==2 || i==5 )
			printf(" -- -- -- |  -- -- -- |  -- -- --\n");
	}
	
	//Funcion para perguntar si esta seguro de resolver
	printf("");
	printf("\n1) Resolver\n2) Salir\n");
	printf("Elige una opci%cn: ",ao);
	scanf("%d",&opcion);
	if (op2==2)
		main();
	


	switch (opcion)
	 
		case 1:
			//Codigo para que se empieze a resolver el sudoku
			while (opcion==1 || op2==1 || matriz != mres ){
				//Menu para preguntar cordenadas a cambiar numeros
				printf("\nIngresar el numero a colocar: ");
				scanf("%i",&valor);
				printf("Renglon:");
				scanf("%i",reng);
				printf("Columna:");
				scanf("%i",colu);
				
				system("cls");
				//Imprime en pantalla que numero se cambio
				printf("\nCambiando %i a %i ",matriz[i-1][j-1],valor);
				matriz[i-1][j-1]= valor;
				printf("\n\nSudoku a Resolver\n");
				printf("=================\n\n");
				//Funcion para resolver sudoku 
				for (i=0 ; i<9 ; i++)
				{
					for (j=0 ; j<9 ; j++)
					{
						printf(" %i ",matriz[i][j]);
						if ( j==2 || j==5 )
							printf(" | ");
					}
					printf("\n");
					if ( i==2 || i==5 )
						printf(" -- -- -- |  -- -- -- |  -- -- --\n");
							a=a+matriz[i][j];
				}

				
				printf("\n%cDesea seguir Resolviendo el Sudoku? \n 1) Si \n 2) No ",sp); 
				printf("\nElige una opci%cn: ",ao);
				scanf("%d",&op2);

				//Funcion que muestra cuando se concluye el codigo correctamente
				if (op2==2)
				{
				main();
				break; 
			}while(a==405)
			printf("Lo lograste en hora buena");
		}
	}
 


void resuelto()
{
	//Declaracion de matrices
	int mres[9][9] = {{3,8,6,5,1,2,7,4,9},{2,7,1,8,9,4,3,6,5},{9,5,4,7,6,3,2,8,1},{7,9,5,4,2,1,6,3,8},{1,6,2,3,8,5,9,7,4},{8,4,3,6,7,9,5,1,2},{4,1,7,2,5,6,8,9,3},{6,2,9,1,3,8,4,5,7},{5,3,8,9,4,7,1,2,6}};
	//Declaración de variables
	int i, j;
	//Titulo
	printf("\nRespuesta:\n");
	printf("==========\n\n");
	//Código que muestra el sudoku resuelto
	for (i=0 ; i<9 ; i++){
		for (j=0 ; j<9 ; j++)
		{
			printf(" %d ",mres[i][j]);
			if ( j==2 || j==5 )
				printf(" | ");
		}
		printf("\n");
		if ( i==2 || i==5 )
			printf(" -- -- -- |  -- -- -- |  -- -- --\n");
	}
	printf("\n");
	main();
}