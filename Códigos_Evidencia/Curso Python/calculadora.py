'''
Calculadora en Python
Desarrollado por           Sánchez Estrada Angel Isaac
Versión:                   1.0
Sistema Operativo:         Windows 10
Versión de Python:         3.9.6 (64-bit)
Ultima Modificación:       05/08/2021 
'''
#Mensaje de Bienvenida
import os
os.system("cls")
print("\n\t\t\t\tBienvenidos a mi Calculadora :)\n\n")

#Instrucciones
print("En esta calculadora se solicitan dos valores lo cuales realizaran las operaciones en orden de la asignacion que le den a los valores solicitados\n")

#Solicitar 2 numeros
n1=float(input("Escribe el primer número: "))
n2=float(input("Escribe el segundo numero: "))

#Calculos
rsuma=n1+n2
rresta=n1-n2
rmultiplicación=n1*n2 
rpotencia=n1**n2 

#Mostrar los resultados
#suma
print("\nEl resultado de la suma de ",n1,"+",n2," es igual a: ",rsuma,"\n")
#resta
print("El resultado de la resta de ",n1,"-",n2," es igual a: ",rresta,"\n")
#multiplicación
print("El resultado de la  multiplicación de",n1,"*",n2," es igual a: ",rmultiplicación,"\n")

if n2==0:
    print("No se puede realizar la división entre 0, por lo tanto no tiene módulo\n")
else:
    #división
    print("El resultado de la división de ",n1,"/",n2," es igual a: ",n1/n2,"\n")
    #módulo
    print("El resultado del modulo de ",n1,"%",n2," es igual a: ",n1%n2,"\n")

#potencia
print("El resultado de la potencia de ",n1,"**",n2," es igual a: ",rpotencia,"\n")