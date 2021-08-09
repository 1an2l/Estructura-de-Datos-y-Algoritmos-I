import os
#Menú
op=1
while(op !='6'):
    os.system("cls")
    print("\n\t\t\t\tBienvenido a mi calculadora en Python\n")
    print(" 1) Suma\n 2) Resta\n 3) Multiplicación\n 4) División\n 5) Conversiones\n 6) Salir")
    op=input("Elige una opción: ")
    if op=='1':
        print("Elegiste Suma :)")
        input("Presiona enter para continuar...")

    elif op=='2':
        print("Elegiste Resta :)")
        input("Presiona enter para continuar...")

    elif op=='3':
        print("Elegiste Multiplicación :)")
        input("Presiona enter para continuar...")

    elif op=='4':
        print("Elegiste Divición :)")
        input("Presiona enter para continuar...")

    elif op=='5':
        print("Elegiste Conversiones :)")
        input("Presiona enter para continuar...")

        op2='0'
        while(op2!='3'):
            os.system("cls")
            print("\n\t\t\tSistema de Conversiones\n")
            print(" 1) Binario - Decimal\n 2) Octal - Decimal\n 3) Salir\n")
            op2=input("Elige una Opción: ")
            if op2=='1':
                print("Elegiste Binario - Decimal")
                input("Presiona enter para continuar...")
            elif op2=='2':
                print("Elegiste Octal - Decimal")
                input("Presiona enter para continuar...")
            elif op2=='3':
                print("Elegiste Salir")
                input("Presiona enter para regresar al menu principal")
            else:
                print("Opción no valida")
                input("Presiona enter para continual...")
        

    elif op=='6':
        print("Elegiste Salir, gracias por usar mi programa :)")
        input("Presiona enter para salir...")

    else:
        print("Opción no válida :(")
        input("Presiona enter para continuar...")