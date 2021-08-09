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
print("\n\t\t\t\tBienvenido a De Binario a Decimal\n\n")

#Solicitar el numero binario
bin = input("Escibe un numero binario de 4 bits: ")

#Verificar que el numero ingresado es de 4 bits
if len(bin)>4:
    print("El numero que ingreso tiene mas de 4 bits")

#En caso de que el numero si sea de 4 bits 
#Generador de numero decimal
else:
    dec = int(bin[0])*8
    dec = dec + (int(bin[1])*4)
    dec = dec + (int(bin[2])*2)
    dec = dec + (int(bin[3])*1)

    print("\nEl numero en binario ingresado es",bin,"correspondiente al numero en decimal",dec,"\n")