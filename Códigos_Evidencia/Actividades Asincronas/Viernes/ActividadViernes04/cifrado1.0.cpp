#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>
using namespace std;

/*
 * Autor:Sánchez Estrada Angel Isaac
 * Nacionalidad: Mexicana
 * Fecha de elaboración: 19-03-2021
 * Ultima modificación: 20-03-2021
 * Sistema Operativo: Windows 10
*/

/*
 Programa que realiza la implementación del cifrado César
 Para cifrar y descifrar un mensaje
*/
//Definimos las variables y les asignamos un valor definido
#define TAM_PALABRA 20
#define TAM_ABC 26

//Declaración de Caracteres
char ao=162, aa=160, au=163, ai=161, ae=130, sp=168 ,aim=214;

//Declaración de matrices
char abecedarioEnClaro[TAM_ABC] =
{'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'
,'U','V','W','X','Y','Z'};
char abecedarioCifrado[TAM_ABC] =
{'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'
,'X','Y','Z','A','B','C'};

//Declaramos las funciones 
void cifrar(char *textoEnClaro);
void descifrar(char *textoCifrado);
int main(){
    
    short opcion = 0, contador;
    char palabra[TAM_PALABRA];
    while (1){
        //Menu del Programa
        cout<<"\n\tCIFRADO CESAR\n"<<endl;

        //Muestra los Abecedarios
        //Abecedario Normal
        for (contador=0 ; contador<26; contador++)
        cout<<*(abecedarioEnClaro+contador);
        cout<<"\n";
        //Abecedario Cifrado
        for (contador=0 ; contador<26; contador++)
        cout<<*(abecedarioCifrado+contador);

        //Opciones del menú
        cout<<"\n";
        cout<<"\nElegir una opcion\n";
        cout<<"1. Cifrar\n";
        cout<<"2. Descifrar\n";
        cout<<"3. Salir\n";
        cout<<">> ";
        cin>>opcion;
        switch(opcion){
            case 1:
            //Mensaje para que ingrese la palabra que quiere cifrar
            cout<<"\nIngresar la palabra a cifrar (en mayusculas)"<<endl;
            cout<<"============================================"<<endl;
            cin>>palabra;
            cifrar(palabra);//Recupera el codigo que se definio en void cifrar
            break;
            case 2:
            //Mensaje para que el usuario ingrese la parabra a descifrar
            cout<<"\nIngresar la palabra a descifrar (en mayusculas)"<<endl;
            cout<<"==============================================="<<endl;
            cin>>palabra;
            descifrar(palabra);//Recupera el codigo que se definio en void descifar
            break;
            case 3:
            return 0;
            default:
            cout<<"Opción no valida."<<endl;//Mensaje que da por defecto si no ingresa un numero que se asigne al menú
        }
    }
    return 0;
}
//Código para Cifrar mensaje
void cifrar(char *textoEnClaro){
    //Código que muestra el mensaje cifrado
    cout<<"\nEl texto cifrado es"<<endl;
    cout<<"==================="<<endl;
    cout<<textoEnClaro<<endl;//Muestra en pantalla el mensaje normal
    //Código que cifra el mensaje
    int contadorAbcedario, contadorPalabra, indice = 0;
    for (contadorPalabra=0 ; contadorPalabra<textoEnClaro[contadorPalabra] ;
    contadorPalabra++)
    for (contadorAbcedario=0 ; contadorAbcedario<TAM_ABC ;
    contadorAbcedario++)
    if (abecedarioEnClaro[contadorAbcedario] ==
    textoEnClaro[contadorPalabra]){
        //Muestra el mensaje cifrado
        cout<<abecedarioCifrado[contadorAbcedario];
        contadorAbcedario = 26;
    }
    cout<<"\n"<<endl;
}
//Código para Descifrar mensaje
void descifrar(char *textoCifrado){
    //Código que muestra el mensaje descifrado
    cout<<"\nEl texto %s descifrado es "<<endl;
    cout<<"========================="<<endl;
    cout<<textoCifrado<<endl;//Muestra en pantalla el mensaje cifrado
    //Código para descifrar el mensaje 
    int contadorAbcedario, contadorPalabra, indice = 0;
    for (contadorPalabra=0 ; contadorPalabra<textoCifrado[contadorPalabra] ;
    contadorPalabra++)
    for (contadorAbcedario=0 ; contadorAbcedario<TAM_ABC ;
    contadorAbcedario++)
    if (abecedarioCifrado[contadorAbcedario] ==
    textoCifrado[contadorPalabra]){
        //Muestra el mensaje descifrado
        cout<<abecedarioEnClaro[contadorAbcedario];
        contadorAbcedario = 26;
    }
    cout<<"\n"<<endl;
}
