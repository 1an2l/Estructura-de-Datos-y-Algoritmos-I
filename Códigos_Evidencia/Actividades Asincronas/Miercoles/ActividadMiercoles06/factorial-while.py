'''
Binario a Decimal
Desarrollado por           Sánchez Estrada Angel Isaac
Versión:                   1.0
Sistema Operativo:         Windows 10
Versión de Python:         3.9.6 (64-bit)
Ultima Modificación:       05/08/2021 
'''
#Mensaje de bienvenida
import os
os.system("cls")
print("\n\t\t\t\tBienvenido a la Calculadora de Factoriales\n\n")

#Solicitar el factorial de un numero
nf = int(input("Escribe el numero del que quieras conocer su factorial: "))

a=1
i=1
while(i<nf+1):
    a=a*i
    i=i+1

print("\nEl factorial de",nf,"es",a,"\n")
input("Presiona enter para salir...")