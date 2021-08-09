/*
 * Autor:Sánchez Estrada Angel Isaac
 * Nacionalidad: Mexicana
 * Fecha de elaboración: 22-03-2021
 * Ultima modificación: 22-03-2021
 * Sistema Operativo: Windows 10
*/

#include <stdio.h>
#include <windows.h>

int main()
{
	//Definimos a las matrices
	char palabra[30];
	int i=0;
	//Impresión en pantalla para pedir que ingrese una palabra
	printf("Ingrese una palabra:\n");
	printf("====================\n");
	printf(">>");
	scanf("%s", palabra);

	//imprime la palabra que escribimos
	printf("\nLa palabra ingresada es:\n");
	printf("========================\n");
	printf("%s", palabra);

	//Función para colocar la palabra ingresada de forma vertical
	for (i = 0 ; i < 20 ; i++)
	{
	printf("\n\n%c\n", palabra[i]);
	}
	return 0;
}