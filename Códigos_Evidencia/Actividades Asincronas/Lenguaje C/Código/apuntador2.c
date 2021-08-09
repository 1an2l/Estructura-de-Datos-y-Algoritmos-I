/*
 * Autor:Sánchez Estrada Angel Isaac
 * Nacionalidad: Mexicana
 * Fecha de elaboración: 22-03-2021
 * Ultima modificación: 22-03-2021
 * Sistema Operativo: Windows 10
*/
#include <stdio.h>
#include <windows.h>

int main() {
    //Declaración de matrices
    int matriz[2][3];//Matriz Princial
    int *apMatriz = matriz[0];
    system("cls");//Función para limpiar pantalla
    //Apuntador(apMatriz se convierte en un apuntador
    printf("\n\n\t\tBienvenido al Programa\n\n");
    printf("Simplificando recorrido de una matriz\n\n");
    
    //Función para solicitar los valores que se ingresen
    for(int i = 0; i < sizeof(matriz)/sizeof(int);i++)
    {
        printf("\nDame el dato %i de la matriz: \n",i+1);
        printf("==============================\n");
        printf(">> ");
        scanf("%i",apMatriz);
        apMatriz ++;
    }
    printf("\n\n");
    
    //Función que imprime los valores registrados
    apMatriz = matriz[0];
    for (int i=0; i < sizeof(matriz)/sizeof(int); i++)
    {
        printf("Dato %d: %d\n",i+1,*apMatriz);
        apMatriz++;
    }
    return 0;
}
