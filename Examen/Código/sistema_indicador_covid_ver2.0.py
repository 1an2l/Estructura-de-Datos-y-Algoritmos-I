'''
                        Sistema Indicador del Color de el Semaforo COVID

Programado por:            Sánchez Estrada Angel Isaac
País de Origen:            México
Versión:                   2.0
Sistema Operativo:         Windows 10
Versión de Python:         3.9.6 (64-bit)
Ultima Modificación:       12/08/2021 
'''
#Declaración de Módulos
import os # importa modulo os para ocupar método system

#Declaración de Variables
op='0'              #variable para ocupar el menú

datos = []          #matriz para almacenar datos

#Sistema Indicador del Color de el Semaforo COVID
while (op != '4'):
    #Limpiar Pantalla
    os.system("cls")

    #Mensaje de Bienvenida
    print("\t\t\t\t\tBienvenido a el Sistema Indicador del Color de el Semaforo COVID\n\n")

    #Menú
    print(" 1) Ingresar Datos de la Persona\n 2) Consulta la base de datos\n 3) Color del Semaforo y Promedio de Edad de los Infectados\n 4) Salir")
    op=input("\nElige una Opción: ")

    #Ingresar datos de una persona a la base de Datos en opción 1
    if op == '1':
        #Limpiar Pantalla
        os.system("cls")
        
        # Mensaje de Bienvenida para Ingresar datos
        print("\t\t\tBienvenido a el Sistema Indicador del Color de el Semáforo COVID") 
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
        print("\t\t\tBienvenido a el Sistema Indicador del Color de el Semáforo COVID") 
        print("\n\t\t\t\t\tEscogiste consultar la base de datos\n\n")
        print("La Base de Datos Contiene lo siguiente: \n")
        print("EDAD       INDICADOR COVID \n")
        
        print(contenido)

        #Para poder salir de la consulta presionar ENTER
        input("Presiona ENTER continuar...")
    
    elif op == '3':
        contador=0          #Contador para el número de personas contagiadas
        cont_0_18=0         #Contador para el número de personas contagiadas entre 0 y 18 años
        cont_19_29=0        #Contador para el número de personas contagiadas entre 19 y 29 años
        cont_30_39=0        #Contador para el número de personas contagiadas entre 30 y 39 años
        cont_40_49=0        #Contador para el número de personas contagiadas entre 40 y 49 años
        cont_50_59=0        #Contador para el número de personas contagiadas entre 50 y 59 años
        cont_60_69=0        #Contador para el número de personas contagiadas entre 60 y 69 años
        cont_70_79=0        #Contador para el número de personas contagiadas entre 70 y 79 años
        cont_80_89=0        #Contador para el número de personas contagiadas entre 80 y 89 años
        cont_90=0           #Contador para el número de personas contagiadas de 90 o más años

        #Abre los datos para lectura y lo hace en una linea
        base_datos=open("bd.csv", "r")
        datos=base_datos.readlines()
        base_datos.close()

        #Manipulación de la Base de Datos
        for i in range(0, len(datos)):
            edad_ind=datos[i].split(' ')    #Lista que alamacena la edad y el indicador 
            edad=int(edad_ind[0]);           #Se obtiene la edad de la persona
            indicador=float(edad_ind[1]);  #Se obtiene el indicador asociado a la misma person
            
            
            
            #Se determina si una persona tiene COVID-19
            if indicador>=0.8:
                contador+=1

                #Se determina la edad de la persona y se clasifica en algún rango de edad
                if (edad>-1 and edad<19):
                    cont_0_18+=1
                elif (edad>18 and edad<30):
                    cont_19_29+=1
                elif (edad>29 and edad<40):
                    cont_30_39+=1
                elif (edad>39 and edad<50):
                    cont_40_49+=1
                elif (edad>49 and edad<60):
                    cont_50_59+=1
                elif (edad>59 and edad<70):
                    cont_60_69+=1
                elif (edad>69 and edad<80):
                    cont_70_79+=1
                elif (edad>79 and edad<90):
                    cont_80_89+=1
                elif edad>89:
                    cont_90+=1

                #Este caso fue añadido con el fin de detectar errores en los datos ingresados
                else:
                    print("Edad fuera de Rango")

        #Se agrupan en listas el número de personas contagiadas para cada rango de edad
        casos=[[cont_0_18, '0-18'],[cont_19_29, '19-29'],[cont_30_39, '30-39'],[cont_40_49, '40-49'],[cont_50_59, '50-59'],[cont_60_69, '60-69'],[cont_70_79, '70-79'],[cont_80_89, '80-89'],[cont_90, '90 o más']]

        #Se ordenan las listas en orden ascendente con el fin de obtener el rango con mayor número de casos
        casos.sort()
        temp=casos[8]       #Variable que contendra el rango con mayor número de contagios y el número de contagios

        
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
            print("Rango de edad de personas que presentan de contagios: " + str(temp[1]) + " años")
            print("Número de contagios existentes en el rango de edad: " + str(temp[0]))
        
        # Si de 31 a 70 personas tienen COVID
        elif contador>30 and contador<=70:
            print("Color de semáforo: Naranja")
            print("Número de personas infectadas con el virus COVID es:", contador)
            print("Rango de edad de personas que presentan de contagios: " + str(temp[1]) + " años")
            print("Número de contagios existentes en el rango de edad: " + str(temp[0]))
        
        # Si de 71 a 100+ personas tienen COVID
        elif contador>70:
            print("Color de semáforo: Rojo")
            print("Número de personas infectadas con el virus COVID es:", contador)
            print("Rango de edad de personas que presentan de contagios: " + str(temp[1]) + " años")
            print("Número de contagios existentes en el rango de edad: " + str(temp[0]))
        
        # si el rango ya no es posible
        else:
            print("\nFuera de rango\n")
        
        #Para poder salir de la consulta precionar ENTER
        input("Presiona ENTER continuar...")
    
    elif op =='4':
        print("\n\t\t\tGracias por usar mi programa\n")
        input("Presiona ENTER para salir...")
    
    else:
        print("Opción no valida!!!\n Intente de nuevo")
        input("Presiona ENTER para salir...")