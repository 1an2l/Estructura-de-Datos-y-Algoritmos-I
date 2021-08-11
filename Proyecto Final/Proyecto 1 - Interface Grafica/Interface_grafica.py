'''
                        Interface grafica orientada a una calculadora

Programado por:            Sánchez Estrada Angel Isaac
País de Origen:            México
Versión:                   1.0
Sistema Operativo:         Windows 10
Versión de Python:         3.9.6 (64-bit)
Ultima Modificación:       08/08/2021 
'''

#Módulos
from tkinter import * #Importa todo el módulo tkinter

#Se va a crear una ventana que es donde se incluira todo lo grafico para la calculadora
ventana = Tk()

#Título que aparecerá al ejecutar
ventana.title("CALCULADORA")

#variables
i=0

#Entrada de texto en la ventana con un estilo de letra de calibri 20
e_texto = Entry(ventana, font="Calibri 20")

#Posición donde se ingresará el texto donde despues de agregarlo habra 4 columnas mas
#padx= espacio a los lados y pady= espacio arriba y abajo
e_texto.grid(row = 0, column= 0, columnspan= 4, padx= 5, pady = 5)

#Funciones
#Ingresar valores con click
#Funcion para que se vea en pantalla los valores que en los que se de click
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

#Funcion para borrar todo
def borrar():
    e_texto.delete(0, END)
    i = 0

#Función para que Python haga la operación evaluando la cadena
def resolvedor():
    #agarra el strig de la caja
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    #funcion para borrar lo que este en la caja de texto
    e_texto.delete(0, END)
    e_texto.insert(0,resultado)
    #iniciar de nuevo l cuadro de texto
    i = 0


#Botones
#width = ancho heigt=largo
#para conectar la función con un boton ocuparemos lambda metodo que permite escribir funcion en linea
#Botones de números
boton1 = Button(ventana, text="1", width= 5, height= 2, command= lambda: click_boton(1))
boton2 = Button(ventana, text="2", width= 5, height= 2, command= lambda: click_boton(2))
boton3 = Button(ventana, text="3", width= 5, height= 2, command= lambda: click_boton(3))
boton4 = Button(ventana, text="4", width= 5, height= 2, command= lambda: click_boton(4))
boton5 = Button(ventana, text="5", width= 5, height= 2, command= lambda: click_boton(5))
boton6 = Button(ventana, text="6", width= 5, height= 2, command= lambda: click_boton(6))
boton7 = Button(ventana, text="7", width= 5, height= 2, command= lambda: click_boton(7))
boton8 = Button(ventana, text="8", width= 5, height= 2, command= lambda: click_boton(8))
boton9 = Button(ventana, text="9", width= 5, height= 2, command= lambda: click_boton(9))
boton0 = Button(ventana, text="0", width= 13, height= 2, command= lambda: click_boton(0))

#Botones de funciones
boton_borrar = Button(ventana, text="AC", width= 5, height= 2, command= lambda: borrar())
boton_parentesis1 = Button(ventana, text="(", width= 5, height= 2, command= lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text=")", width= 5, height= 2, command= lambda: click_boton(")"))
boton_punto = Button(ventana, text=".", width= 5, height= 2, command= lambda: click_boton("."))

#Botones de Operaciones
boton_div = Button(ventana, text="/", width= 5, height= 2, command= lambda: click_boton("/"))
boton_mult = Button(ventana, text="x", width= 5, height= 2, command= lambda: click_boton("*"))
boton_sum = Button(ventana, text="+", width= 5, height= 2, command= lambda: click_boton("+"))
boton_rest = Button(ventana, text="-", width= 5, height= 2, command= lambda: click_boton("-"))
boton_igual = Button(ventana, text="=", width= 5, height= 2, command= lambda: resolvedor())

#Agregar botones en pantalla
#primera pocisión
boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_div.grid(row = 1, column = 3, padx = 5, pady = 5)

#segunda posición
boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

#Tercera posición
boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

#Cuarta posición
boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_rest.grid(row = 4, column = 3, padx = 5, pady = 5)

#Quinta posición
boton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)


#Mainloop para reconocer todos los eventos que sucedan
ventana.mainloop()