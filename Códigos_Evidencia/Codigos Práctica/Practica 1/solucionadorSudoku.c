#include <stdio.h>

#define TRUE 1
#define FALSE 0

int sudoku[9][9];
void leeSudoku(void);
void resSudoku(int, int);
int buscaCeldaVacia(int *, int *);
int puedoColocar(int, int, int);
void impSudoku(void);

void main(void)
{
	leeSudoku();
	resSudoku(0,0);
}
void resSudoku(int x, int y)
{
	int nro, hayVacia;
	hayVacia=buscaCeldaVacia(&x, &y);
	if ( !hayVacia ) impSudoku();
	else
	{
		for(nro=1; nro<=9; nro++)
			if ( puedoColocar(x, y, nro) )
			{
				sudoku[x][y]=nro; // lo coloco
				resSudoku(x,y+1); // tomo el sgte
				sudoku[x][y]=0; // lo quito
			}
	}
}

int buscaCeldaVacia(int *x, int *y)
{
	for( ; *x<9; (*x)++)
	{
		for( ; *y<9; (*y)++)
			if( sudoku[*x][*y]==0 ) return TRUE;
		*y=0;
	}
	return FALSE;
}
int puedoColocar(int f, int c, int nro)
{
	int i, j, iniFil, finFil, iniCol, finCol;
	// comprueba fila
	for(j=0; j<9; j++)
	if(sudoku[f][j]==nro)
		return FALSE;
	// comprueba columna
	for(i=0; i<9; i++)
	if(sudoku[i][c]==nro)
		return FALSE;
	// comprueba subcuadrado
	iniCol = (c/3) *3;
	finCol = iniCol+3;
	iniFil = (f/3) *3;
	finFil = iniFil+3;
	for(i=iniFil; i<finFil; i++)
		for(j=iniCol; j<finCol; j++)
			if(sudoku[i][j]==nro)
				return FALSE;
			return TRUE;
}
void impSudoku(void)
{
	int i, j;
	printf("SOLUCION:\n");
	printf("========\n\n");
	for(i=0; i<9; i++)
	{
		for(j=0; j<9; j++)
		{
			printf("%d",sudoku[i][j]);
			if ( j==2 || j==5 ) printf(" | ");
		}
		printf("\n");
		if ( i==2 || i==5 )
			printf("--- | --- | ---\n");
	}
	printf("\n");
}
void leeSudoku(void)
{
	int i, j;
	printf("Introduce SUDOKU (valor seguido de espacio para cada fila,\n");
	printf(" (0 para indicar celda vacia):\n"); printf("\n");
	for(i=0; i<9; i++)
	{ printf("Fila %d : ",i+1);
		for(j=0; j<9; j++) scanf("%d",&sudoku[i][j]);
	}
}