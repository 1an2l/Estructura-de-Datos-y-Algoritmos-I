'''
calificaciones
Desarrollado por           Sánchez Estrada Angel Isaac
Versión:                   1.0
Sistema Operativo:         Windows 10
Versión de Python:         3.9.6 (64-bit)
Ultima Modificación:       05/08/2021 
'''

#Registro de Calificaciones
op='0'
import re
import os

#funcion para listar todos los registros realizados
def con_datos(datos):
    for i in range(0, len(datos)):
        print(datos[i])
    return None

op='0'
datos=[]

while (op!='4'):
    #Menú
    os.system("cls")
    print("\n\t\t\t\tSistema de Calificaciones\n\n")
    print(" 1) Llenar\n 2) Promedio\n 3) Consulta de Datos\n 4) Salir")
    op=input("\nElige una Opción: ")

    #Resistro de alumnos
    if op=='1':
        nom=input("Nombre: ")
        cal=input("Calificación: ")
        reg=nom+','+cal+'\n'
        datos.append(reg)
    elif op=='2':
        prom=0
        print("\nAlumnos y Calificaciones:") 
        #Mostrar en pantalla los datos registrados
        con_datos(datos)
        for i in range(0,len(datos)):
            #Funcion que encuentra a los numeros en una cadena de caracteres
            temp = re.findall('\d+',datos[i])
            prom = prom +int(temp[0])
        #Se muestra el promedio en pantalla
        print("\nEl promedio del grupo es: "+ str(prom/len(datos)))
        input("Presiona enter para continuar...")
    elif op=='3':
        os.system("cls")
        print("\n\t\t\tAlumnos y sus Calificaciones registradas\n")
        con_datos(datos)
        input("Presiona enter para continuar...")

    elif op=='4':
        print("\n\t\t\tGracias por usar mi programa\n")
        input("Presiona enter para salir...")
    else:
        print("Opción no valida")
print(datos)

a=open("cal.csv","a")
a.writelines(datos)
a.close()

a=open("cal.csv","r")
contenido=a.readlines()
a.close()
print(contenido)

