#include <stdio.h>
#include <string.h>
#include <windows.h>

/*
Este Programa fue desarrollado con la intencion de resolver una
operación dada en Forma de Cadena de Caracteres.

Desarrollado en:
Windows 10

Programado por :
Sánchez Estrada Angel Isaac
*/


int sumres();
int muldiv();
int term();

char input[101];//matrisz unidimencional donde se guardaran los datos ingresados por el usuario
int pos = 0;//Declaracion de variable que recorrera los caracteres

int term(){
  int n = 0;

  if(input[pos] == '(')//Funcion que hace que detecte el parentesis abierto en la cadena ingresada
  {
    pos++;//Funcion que recorre cada uno de los caracteres
    n = sumres();
    
    if(input[pos] == ')')//Funcion que hace que detecte el parentesis cerrado en la cadena ingresada
    {
      pos++;//Funcion que recorre cada uno de los caracteres
      return n;
    }
  }else
  {
    while('0' <= input[pos] && input[pos] <= '9')
    {
      n = n*10 + (input[pos] - '0');
      pos++;//Funcion que recorre cada uno de los caracteres
    }
  }
  return n;
}

int muldiv(){
  int first,second;
  
  first = term();
  for(;;)
  {
    if(input[pos] == '/')//Funcion que hace que detecte el operador de division en la cadena ingresada
    {
      pos++;//Funcion que recorre cada uno de los caracteres
      second = term();
      first /= second; 
    }
    else if(input[pos] == '*')//Funcion que hace que detecte el operqador de multiplicacion en la cadena ingresada
    {
      pos++;//Funcion que recorre cada uno de los caracteres
      second = term();
      first *= second;
    }
    else
    {
      return first;
    }
  }
}

int sumres(){
    int first,second;
    
    first = muldiv();
    
    for(;;){
        if(input[pos] == '+')//Funcion que hace que detecte el operador de suma en la cadena ingresada
        {
          pos++;//Funcion que recorre cada uno de los caracteres
          second = muldiv();
          first += second; 
        }
        else if(input[pos] == '-')//Funcion que hace que detecte el operador de resta en la cadena ingresada
        {
          pos++;//Funcion que recorre cada uno de los caracteres
          second = muldiv();
          first -= second;
        }
        else
        {
        return first;
        }
    }
    
}

int main(){

    //Declaramos Variables
    int n,i,j,op;
    char dg=6, aa=160, ae=130, ai=161, ao=162, au=163, sp=168, cr=175, sa=33;

    system("cls");//Función para limpiar pantalla

    //Mensaje de Bienvenida
    printf("\033[4;33m");
    printf("\n\n\t\t\t%c Bienvenidos a la Calculadora de Operaciones en Cadena %c\n\n",dg ,dg);
  	printf("\033[0m");

    do
    {
        //Menu Para dar a Elegir si desea resolver una Operación en Cadena
        printf("\nDeseas Realizar una Operaci%cn en Cadena",ao);
        printf("\n1) Si \n2) No");
        printf("\n\nElige una opci%cn de la lista: ",ao);
        printf("%c",cr);
		    scanf("%d",&op);//Duncion que sirve para detectar la opcion del usuario

        switch (op)
        {
        case 1:

            //Funcion para solucitar la operacion a realizar y que tambien da el resultado de la misma
            system("cls");//Función para limpiar pantalla

            printf("\nIntroduce una Operaci%cn en Cadena que contenga las Operaciones B%csicas y N%cmeros Naturales \n",ao,aa,au);
            printf("==========================================================================================\n");
            printf("%c ",cr);
            scanf("%s",input);
            printf("Respuesta: %d\n",sumres());
            break;
        
        case 2:
            //Mensaje de despedida al terminar de utilizar el programa
            printf("\033[01;32m");
            printf("\nGracias por utilizar la Calculadora de Operacion en Cadena\n\n");
            printf("\033[0m");
            break;

        default:

            //Mensaje de Opcion al ingresar una opcion no definida en el menu
            system("cls");//Función para limpiar pantalla

            printf("\033[01;31m");
            printf("\n\tOpci%cn no v%clida!!!\n\n",ao,aa);
            printf("\033[0m");
            break;
        }
    } while (op!=2);//Funcion que hace que no se salga el programa hasta que se coloque 2
    
    return 0;
    }