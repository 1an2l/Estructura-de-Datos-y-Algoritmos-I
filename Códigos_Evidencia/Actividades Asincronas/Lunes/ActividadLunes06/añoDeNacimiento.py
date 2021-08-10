'''
Programa que calcula el año de nacimiento
Sistema Operativo:        Windows 10
Creador:                  Sánchez Estrada Angel Isaac                  
'''
import os
import datetime

#Mensaje de bienvenida
os.system("cls")
print("\n\t\t\t\tBienvenidos a mi calcula edad:)\n\n")
#Solicitar edad
edad=int(input("Escibe tu edad: "))

#Calcula la fecha actual
añoA=datetime.datetime.now()

#Calcular años de nacimiento
año=añoA.year-edad

#Mostrar el año de nacimiento
print("Tu año de nacimiento es: ",año)