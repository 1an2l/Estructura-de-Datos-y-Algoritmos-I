'''
Binario a Decimal
Desarrollado por           Sánchez Estrada Angel Isaac
Versión:                   1.0
Sistema Operativo:         Windows 10
Versión de Python:         3.9.6 (64-bit)
Ultima Modificación:       05/08/2021 
'''
#Funcion del para calcular el factorial
def factorial(n):
    a=1
    for i in range (1,n+1):
        a=a*i
    return a

#Calculadora con menú
op='0'
while op!='7':
    #Mensaje de bienvenida
    import os
    os.system("cls")
    print("\n\t\t\t\tBienvenido a la Calculadora en Python\n\n")
    print("¿Qué desea hacer?")
    print(" 1) Suma\n 2) Resta\n 3) Multiplicación\n 4) División y Módulo\n 5) Potencia\n 6) Factorial\n 7) Salir")
    op=input("\nElige una opción: ")
    if op=='1':
        os.system("cls")
        print("\n\t\t\tHa seleccionado Suma\n")
        #Pedirle a usuario que ingrese 2 números de tipo float
        n1=float(input("Introduce el primer número: "))
        n2=float(input("Introduce el segundo número: "))
        #Imprimir la suma
        print("\nEl resultado de la suma de ",n1,"+",n2," es igual a: ",n1+n2,"\n")
        input("Presiona enter para continuar...")

    elif op=='2':
        os.system("cls")
        print("\n\t\t\tHa seleccionado Resta\n")
        #Pedirle a usuario que ingrese 2 números de tipo float
        n1=float(input("Introduce el primer número: "))
        n2=float(input("Introduce el segundo número: "))
        #Imprimir la resta
        print("El resultado de la resta de ",n1,"-",n2," es igual a: ",n1-n2,"\n")
        input("Presiona enter para continuar...")

    elif op=='3':
        os.system("cls")
        print("\n\t\t\tHa seleccionado Multiplicación\n")
        #Pedirle a usuario que ingrese 2 números de tipo float
        n1=float(input("Introduce el primer número: "))
        n2=float(input("Introduce el segundo número: "))
        #Imprimir la multiplicación
        print("El resultado de la  multiplicación de",n1,"*",n2," es igual a: ",n1*n2,"\n")
        input("Presiona enter para continuar...")

    elif op=='4':
        os.system("cls")
        print("\n\t\t\tHa seleccionado División y Módulo\n")
        #Pedirle a usuario que ingrese 2 números de tipo float
        n1=float(input("Introduce el primer número: "))
        n2=float(input("Introduce el segundo número: "))
        #Evaluar si n2=0
        if n2==0:
            print("No se puede realizar la división entre 0, por lo tanto no tiene módulo\n")
        else:
            #Imprimir la división
            print("El resultado de la división de ",n1,"/",n2," es igual a: ",n1/n2,"\n")
            #Imprimir el módulo
            print("El resultado del modulo de ",n1,"%",n2," es igual a: ",n1%n2,"\n")
            input("Presiona enter para continuar...")

    elif op=='5':
        os.system("cls")
        print("\n\t\t\tHa seleccionado Potencia\n")
        #Pedirle a usuario que ingrese 2 números de tipo float
        n1=float(input("Introduce tu primer número: "))
        n2=float(input("Introduce tu segundo número: "))
        #Imprimir la potencia
        print("El resultado de la potencia de ",n1,"^",n2," es igual a: ",n1**n2,"\n")
        input("Presiona enter para continuar...")

    elif op=='6':
        os.system("cls")
        print("\n\t\t\tHa seleccionado Factorial\n")
        #Preguntarle al usuario que ingrese un factorial
        nf = int(input("Escribe el numero del que quieras conocer su factorial: "))
        r=factorial(nf)
        print("\nEl factorial de",nf,"es",r,"\n")
        input("Presiona enter para continuar...")

    elif op=='7':
        os.system("cls")
        #Si el usuario decide salir del programa
        print("\n\t\t\tGracias por usar mi programa\n")
        input("Presiona enter para salir...")

    else:
        os.system("cls")
        #Si el usuario selecciona una opción no válida
        print("Opción no válida :(","\n")
        input("Presiona enter para continuar...")