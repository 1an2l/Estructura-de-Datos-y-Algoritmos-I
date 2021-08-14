#include <stdio.h>     //Directiva de Prosesamiento
#include <stdlib.h>    //Directiva de Prosesamiento
#include <windows.h>   //Directiva de Prosesamiento

/*
Creado por:            Sánchez Estrada Angel Isaac
Nacionalidad:          Mexicana
Idioma:                Español
Sistema Operativo:     Windows 10
Fecha de Creación:     1 de junio del 2021
Ultimma modificacion:  20 de junio del 2021 
*/


int main ()//Función principal
{
    //Declaración de Variables
    int i, j, op, rs=175, sp=168, aa=160, ae=130, ai=161, ao=162, au=163, dg=6;

    //Declaracion de la matriz que contendra a la palabra
    char p[10];
    // Declaracion de la variable que servira para dar opcion de salir
    char opc;

    do//Ciclo do-While para permitir reproducir el codigo varias veces
    {
        system("cls");//Funcion del sistema Windows para limpiar pantalla
        fflush(stdin);//Funcion para limpiar la memoria

        //Mensaje de Bienvenida
        printf("\033[01;33m");//Funcion para dar color
        printf("\n\t\t\t%c Bienvenidos al juego D reversa %c\n\n",dg,dg);//Mensaje de Bienvenida
        printf("\033[0m");//Función para terminar el color y que regrese al original

        //Apartado de Instruciones
        printf("\033[01;36m");
        printf("INSTRUCCIONES:\n");
        printf("\033[0m");
        printf("Escribe una palabra para darle el efecto de D reversa, en donde al obtener este efecto en su palabra la tendras que leer tal cual para que el otro jugador pueda adivinar que palabra es.\n\n");
        
        //Apartado de jugadores necesarios
        printf("Jugadores necesarios ");
        printf("\033[01;36m");
        printf("2 +\n\n");//Numero de jugadores
        printf("\033[0m");

        //Apartado de como se maneja el marcador
        printf("\033[01;36m");
        printf("Puntaje:\n");
        printf("\033[0m");
        printf("Si acierta = ");
        printf("\033[01;36m");
        printf("1 ");//Puntaje si sabe la palabra
        printf("\033[0m");
        printf("punto\n");
        printf("Si no acierta = ");
        printf("\033[01;36m");
        printf("-1 ");//Puntaje si no sabe la palabra
        printf("\033[0m");
        printf("punto\n\n");

        //Apartado de Aclaracion de como se gana en el juego
        printf("\033[01;36m");
        printf("Forma de ganar:\n");
        printf("\033[0m");
        printf("El jugador que primero tenga ");
        printf("\033[01;36m");
        printf("10 ");//Puntaje limite para ganar
        printf("\033[0m");
        printf("puntos gana\n\n");

        //Apartado para escribir la Palabra a invertir
        printf("Escribe una Palabra que tendra el efecto de ");
        printf("\033[01;35m");
        printf("D reversa");
        printf("\033[0m");
        printf(" para comenzar ");
        printf("\n===================================================================\n%c ",rs);//Separador para decorar
        for ( i = 0; (p[i]=getchar())!='\n'; i++);//Funcion que permite ingresar la palabra a invertir
        printf("\nTu ");
        printf("\033[01;35m");
        printf("D reversa");
        printf("\033[0m");
        printf(" esta lista y es:\n");
        printf("=============================");//Separador para decorar
        printf("\033[1;33m");
        for ( j = i; j>=0; j--)//Funcion que permite invertir la palabra ingresada
        printf(" %c",p[j]);//Funcion que imprime la palabra ingresada de forma alrevez
        printf("\n\n\n");
        printf("\033[0m");

        //Apartado de salida o continuar jugando
        printf("Si quieres volver a jugar escriba ");
        printf("\033[01;32m");
        printf("S");// 's' dando referencia a la opcion de seguir jugando
        printf("\033[0m");
        printf(" en caso de ya no querer escriba ");
        printf("\033[01;31m");
        printf("N");// 'N' dando referencia a la opcion salir del juego
        printf("\033[0m");
        printf("\n%c ",rs);//Decorativo para señalar donde se esta escribiendo
        scanf("%c",&opc);//Funcion para capturar la opcion de salir
    }while (opc == 's' || opc == 'S');//Funcion que permite repetir el codigo al colocar 's' o 'S'

    //Apartado de mensaje de salida y de gratitud por usar el juego
    system("cls");//Funcion del sistema Windows para limpiar pantalla para mostrar texto de salida
    printf("\033[01;32m");
    printf("\n\tElegiste la opci%cn salir\n\nGracias por jugar D reversa regrese pronto \n\n",ao);//Texto de salida
    printf("\033[0m");

    system("PAUSE");//Funcion de Windows que permite no cerrar el programa antes de que aparezca el texto de gratitud

    
    return 0;
}

