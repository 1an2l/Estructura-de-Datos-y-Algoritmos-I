'''
                        Sistema Indicador del Color de el Semaforo COVID

Programado por:            Sánchez Estrada Angel Isaac
País de Origen:            México
Versión:                   1.0
Sistema Operativo:         Windows 10
Versión de Python:         3.9.6 (64-bit)
Ultima Modificación:       08/08/2021 
'''
#Declaración de Módulos
import os # importa modulo os para ocupar método system
from re import findall #importa modulo re para ocupar el método findall

#Declaración de Variables
op='0' #variable para ocupar el menú
contador = 0 #Contador para el número de personas con COVID
contador_edad=0 #Contador para la edad de las personas con COVID
datos = [] #matriz para almacenar datos

#Sistema Indicador del Color de el Semaforo COVID
while (op != '4'):
    #Limpiar Pantalla
    os.system("cls")

    #Mensaje de Bienvenida
    print("\t\t\t\t\tBienvenido a el Sistema Indicador del Color de el Semaforo COVID\n\n")

    #Menú
    print(" 1) Ingresar Datos de la Persona\n 2) Consulta la base de datos\n 3) Color del Semaforo y Promedio de Edad de los Infectados\n 4) Salir")
    op=input("\nElige una Opción: ")

    #Ingresar datos de una persona a la base de Datos en opcion 1
    if op == '1':
        #Limpiar Pantalla
        os.system("cls")
        
        # Mensaje de Bienvenida para Ingresar datos
        print("\t\t\tBienvenido a el Sistema Indicador del Color de el Semaforo COVID") 
        print("\n\t\t\t\t\tEscogiste ingresar tus Datos\n\n")

        #Solicitando Datos a ingresar
        d = []
        edad_ing = int(input("Ingresa tu edad: "))
        indicador = input("Ingrese su Indicador COVID: ")

        #Registro para las Bases de Datos de Edad y Indicador COVID
        Ingreso = str(edad_ing)+'         '+str(indicador)+'\n'
        d.append(Ingreso)

        #Escribe la Base de Datos
        bd = open("bd.csv", "a")
        bd.writelines(d)
        bd.close()

        print("\nEl usuario ha sido registrado\n")
        input("Presiona ENTER continuar...")

    #Consulta de Datos de la base de Datos
    elif op == '2':
        #Leertor de Base de Datos
        bd = open("bd.csv", "r")
        contenido = bd.read()

        #Limpiar Pantalla
        os.system("cls")

        # Mensaje de Bienvenida para Consulta la base de datos
        print("\t\t\tBienvenido a el Sistema Indicador del Color de el Semaforo COVID") 
        print("\n\t\t\t\t\tEscogiste consultar la base de datos\n\n")
        print("La Base de Datos Contiene lo siguiente: \n")
        print("EDAD       INDICADOR COVID \n")
        
        print(contenido)

        #Para poder salir de la consulta precionar ENTER
        input("Presiona ENTER continuar...")
    
    elif op == '3':
        #Abre los datos para lectura y lo hace en una linea
        base_datos=open("bd.csv", "r")
        datos=base_datos.readlines()
        base_datos.close()

        #Manipulación de la Base de Datos
        for i in range(0, len(datos)):
            #Lista que alamacena la edad y el indicador para manipularla como matriz
            edad_ind=findall(r'[\d\.\d]+', datos[i]) 
            indicador = float(edad_ind[1])#Indicador se encuentra en la posicion 1 de la matriz edad_ind
            edad = int(edad_ind[0])#Edad se encuentra en la posicion 0 de la matriz edad_ind

            #Se determina si una persona tiene COVID
            if indicador>=0.8:
                contador = contador + 1
                contador_edad = contador_edad + edad
        
        #Limpiar Pantalla
        os.system("cls")

        # Mensaje de Bienvenida para consultar el color del semaforo y edad promedio de Infectador por COVID
        print("\t\t\t\t\tBienvenido a el Sistema Indicador del Color de el Semaforo COVID") 
        print("\n\t\t\t\tEscogiste consultar el color del semaforo y edad promedio de Infectados por COVID\n\n")

        '''
        De acuerdo a la variable contador se determina el color del semáforo por COVID
        y se muestra el número de personas infectadas con su respectivo promedio de edad 
        de esas personas contagiadas, con la operación contador_edad/contador que seria 
        en otras palabras, la suma de las edades de todos los contagiados
        entre la cantidad de edades que se sumaron.
        '''

        # Si 0 personas tienen COVID
        if contador==0:
            print("Color de semáforo: Verde")
            print("El número de personas infectadas con el virus COVID es: 0")

        # Si de 1 a 30 personas tienen COVID
        elif contador>0 and contador<=30:
            print("Color de semáforo: Amarillo")
            print("Número de personas infectadas con el virus COVID es:", contador)
            print("\nEdad promedio de los Infectados: " + str("{:.1f}".format(contador_edad/contador)) + " años\n")
        
        # Si de 31 a 70 personas tienen COVID
        elif contador>30 and contador<=70:
            print("Color de semáforo: Naranja")
            print("Número de personas infectadas con el virus COVID es:", contador)
            print("\nEdad promedio de los Infectados: " + str("{:.1f}".format(contador_edad/contador)) + " años\n")
        
        # Si de 71 a 100+ personas tienen COVID
        elif contador>70:
            print("Color de semáforo: Rojo")
            print("Número de personas infectadas con el virus COVID es:", contador)
            print("\nEdad promedio de los Infectados: " + str("{:.1f}".format(contador_edad/contador)) + " años\n")
        
        # si el rango ya no es posible
        else:
            print("\nFuera rango\n")
        
        #Para poder salir de la consulta precionar ENTER
        input("Presiona ENTER continuar...")