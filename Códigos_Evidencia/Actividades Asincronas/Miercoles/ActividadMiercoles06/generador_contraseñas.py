'''
Generador de Contraseñas
Desarrollado por           Sánchez Estrada Angel Isaac
Versión:                   1.0
Sistema Operativo:         Windows 10
Versión de Python:         3.9.6 (64-bit)
Ultima Modificación:       03/08/2021 11:50 
'''
#Funcion para limpiar pantalla
import os
os.system("cls")

#Mensaje de bienvenida al programa
print("\n\t\t\t\tBienvenidos al Generador de Contraseñas")

#Funcion para solicitar el nombre
nombre=input(str("\nEscribe tu nombre: "))

#Saludo para el usuario
print("\nHola",nombre)

#Muestra en pantalla el nombre en Mayusculas y minusculas
print("\nTu nombre en Mayusculas es: ",nombre.upper())
print("Tu nombre en Minusculas es: ",nombre.lower())

#Función para solicitar edad
edad=int(input("\nEscribe tu Edad: "))

#Generador de la contraseña
contraseña=nombre[2] + str((edad*3)/2) +nombre[0].lower()

#Muesestra en pantalla la contraseña optenida con el generador
print("\nTu contraseña es: ",contraseña)