'''
Registro de usuario
Desarrollado por           Sánchez Estrada Angel Isaac
Versión:                   1.0
Sistema Operativo:         Windows 10
Versión de Python:         3.9.6 (64-bit)
Ultima Modificación:       05/08/2021 
'''

#Registro de Calificaciones
op='0'
import os


op='0'
while(op!='3'):
    #Menú
    os.system("cls")
    print("\n\t\t\t\tRegistro de Usuario\n\n")
    print(" 1) Registrar nuevo usuario\n 2) Consultar los usuarios registrados\n 3) Salir")
    op=input("\nElige una Opción: ")

    #Resistro de nuevo usuario
    if op=='1':
        usuario=input("Ingrese nombre de Usuario: ")
        contraseña=input("Ingrese una contraseña de almenos 8 caracteres: ")
        #Filtro para contraseñas
        if len(contraseña)<8:
            print("La contraseña ingresada no tiene almenos 8 caracteres")
            input("Presiona enter para intentar de nuevo...")
        else:
            datos=[]
            temp=usuario + ', '+ contraseña + "\n"
            datos.append(temp)

            #Escribir datos en un archivo
            archivo=open("data.csv", "a")
            archivo.writelines(datos)
            archivo.close()

            print("\nEl usuario ha sido registrado\n")
            input("Presiona enter continuar...")
    
    #Muestra los usuarios registrados
    elif op=='2':
        #leer datos del archivo
        archivo=open("data.csv", "r")
        contenido=archivo.read()
        os.system("cls")
        print("\n\t\t\tUsuarios registrados\n")
        print(contenido)
        input("Presiona enter continuar...")

    #Sale del programa
    elif op=='3':
        print("\n\t\t\tGracias por usar mi programa\n")
        input("Presiona enter para salir...")

    else:
        print("Opción no valida")
print(datos)



