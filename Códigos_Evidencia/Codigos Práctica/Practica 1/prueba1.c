#include <stdio.h>

int main(){

int *reng,*colu,ren=5,valor=9; 	
int opcion=0,op2;


 
 int i,j,matriz[9][9] = {{5,3,0,0,7,0,0,0,0},{6,0,0,1,9,5,0,0,0},{0,9,8,0,0,0,0,6,0},{8,0,0,0,6,0,0,0,3},{4,0,0,8,0,3,0,0,1},{7,0,0,0,2,0,0,0,6},{0,6,0,0,0,0,2,8,0},{0,0,0,4,1,9,0,0,5},{0,0,0,0,8,0,0,7,9}};
 int mres[9][9] = {{5,3,4,6,7,8,9,1,2},{6,7,2,1,9,5,3,4,8},{1,9,8,3,4,2,5,6,7},{8,5,9,7,6,1,4,2,3},{4,2,6,8,5,3,7,9,1},{7,1,3,9,2,4,8,5,6},{9,6,1,5,3,7,2,8,4},{2,8,7,4,1,9,6,3,5},{3,4,5,2,8,6,1,7,9}};

reng=&i;
colu=&j;


 printf("Imprimir Matriz\n");
 for (i=0 ; i<9 ; i++){
 for (j=0 ; j<9 ; j++){
 printf(" %i ",matriz[i][j]);
 }
 printf("\n");
 }
 
 printf("1) descifrar\n2)Salir\n");
 printf("Elige una opcion: ");
scanf("%d",&opcion);


 switch (opcion)
 
 case 1:

while (opcion==1 || op2==1 || matriz != mres ){
	

printf("\nIngresar el numero para ingresar: \n");
 scanf("%i",&valor);


 printf("\nRenglones:");
 scanf("%i",reng);
 printf("\nColumnas:");
 scanf("%i",colu);

printf("\nCambiando %i a %i \n",matriz[i][j],valor);

matriz[i][j]= valor;
printf("\nImprimir Matriz\n");
 for (i=0 ; i<9 ; i++){
 for (j=0 ; j<9 ; j++){
 printf(" %i ",matriz[i][j]);
 }
 
 printf("\n");
 }

printf("Quieres seguir?:\n1) Si \n 2)no \n"); 
scanf("%d",&op2);

if (op2==2)
{main();
break; }
}}
