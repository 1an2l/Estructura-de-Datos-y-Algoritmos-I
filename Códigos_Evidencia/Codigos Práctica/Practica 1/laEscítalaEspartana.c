#include<stdio.h>//Es el archivo de cabecera que contiene las definiciones de macros, 
				 //las constantes,  las declaraciones de las funciones de 
				 //la biblioteca estandar del lenguaje C para hacer operaciones,
				 //estandar, de entrada y salida, asi como definiciones de tipos
				 //necesarias para dichas operaciones

/*
 * Autor:Sánchez Estrada Angel Isaac
 * Nacionalidad: Mexicana
 * Fecha de elaboración: 12-03-2021
 * Ultima modificación: 14-03-2021
 * Sistema Operativo: Windows 10
*/

/*
	Programa que realiza la implementación de la escitala espartana
	Para cifrar y descifrar.
*/

//Declaración de funciones.
void crearMensaje();
void descifrarMensaje();

int main()
{
	//Declaracion de Variables para "int main"
	short opcion=0;//Inicia el valor de las variables en cero
	char ao=162, aa=160, au=163, ai=161, ae=130, sp=168 ,aim=214;//Caracteres a ocupar
	
	while (1){
		//Titulo de el Programa
		printf("\n\n\t*** ESCITALA ESPARTANA ***\n",aim);
		//Menú de opciones
		printf("\n%cQu%c desea realizar?\n",sp,ae);
		printf("  1) Crear mensaje cifrado.\n");
		printf("  2) Descifrar mensaje.\n");
		printf("  3) Salir.\n");
		printf("Elige una opci%cn: ",ao);
		scanf("%d", &opcion);//Leer opcion ingresada
		switch(opcion){//Estructura para evaluar lo que se ingrese a &opcion
			case 1:
				crearMensaje();
				break;
			case 2:
				descifrarMensaje();
				break;
			case 3:
				return 0;
			default:
				printf("Opci%cn no v%clida.\n",ao ,aa);
		}
	}
	return 0;
}

//Función de crearMensaje para ejecutar su codigo contenido cuando se llame en el int main
void crearMensaje(){
	//Declaración de Varibles para "void crearMensaje"
	int ren, col, i, j, k=0;
	char ao=162, aa=160, au=163, ai=161, ae=130, sp=168 ,aim=214 , na=164;//Caracteres

	//Peticion de variables para definir a la matriz
	printf("\nIngresar el tama%co de la esc%ctala:\n",na ,ai);
	printf("====================================\n");
	
	//Lectura del numero que ira en renglones de la matriz para la escitala
	printf("Renglones:");
	scanf("%i",&ren);
	
	//Lectura del numero que ira en columnas del la matriz para la escitala
	printf("Columnas:");
	scanf("%i",&col);
	
	//Declaracion de matrices
	char escitala[ren][col];
	char texto[ren*col];
	
	//Peticion de texto a cifrar
	printf("\nEscriba el texto a cifrar sin espacios:\n");
	printf("=======================================\n");
	scanf("%s", texto);
	
	//Codigo para cifrar el mensaje
	for (i=0 ; i<ren ; i++)
		for (j=0 ; j<col ; j++)
			escitala[i][j] = texto[k++];
	
	//Codigo para mostrar el mensaje ya cifrado
	printf("\nEl texto en la tira queda de la siguiente manera:\n");
	printf("=================================================\n");
	for (i=0 ; i<col ; i++)
		for (j=0 ; j<ren ; j++)
			printf("%c", escitala[j][i]);

	printf("\n");
}

void descifrarMensaje(){
	
	//Declaracion de variables para "descifrarMensaje"
	int ren, col, i, j, k=0;
	char ao=162, aa=160, au=163, ai=161, ae=130, sp=168 ,aim=214 ,na=164;//Caracteres.

	//Petición de Variables para 
	printf("\nIngresar el tama%co de la esc%ctala:\n",na ,ai);
	printf("====================================\n");
	
	//Lectura del numero que ira en renglones de la matriz para la escitala
	printf("Renglones:");
	scanf("%i",&ren);
	
	//Lectura del numero que ira en columnas del la matriz para la escitala
	printf("Columnas:");
	scanf("%i",&col);
	
	//Declaracion de matrices
	char escitala[ren][col];
	char texto[ren*col];
	
	//Peticion de texto a descifrar
	printf("\nEscriba el texto a descifrar sin espacios:\n");
	printf("==========================================\n");
	scanf("%s", texto);
	
	//Codigo para descifrar el mensaje
	for (i=0 ; i<col ; i++)
		for (j=0 ; j<ren ; j++)
			escitala[j][i] = texto[k++];

	//Codigo para mostrar el mensaje ya descifrado
	printf("\nEl texto descifrado es:\n");
	printf("=======================\n");
	for (i=0 ; i<ren ; i++)
		for (j=0 ; j<col ; j++)
			printf("%c", escitala[i][j]);
}