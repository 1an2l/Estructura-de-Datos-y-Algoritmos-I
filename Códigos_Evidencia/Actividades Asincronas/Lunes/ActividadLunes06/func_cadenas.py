import os
os.system("cls")

#Funciones con dadenas
frase="A mi me gusta programar en Python"
print(frase.find("Python"))
print(frase.find("Java"))
print(frase.find("m"))

#Bucar primera m
pm=frase.find("m")
#Buscar la segunda map
print(frase.find("m",pm+1))

#Combierte en mayusculas toda la cadena
print(frase.upper())

pp=frase.find("Python")
print(frase[:pp]+frase[pp:].upper())
print(frase[:pp]+frase[pp:].lower())

print(frase.replace("Python","Java"))

print(frase.split(' '))
print(frase.split('m'))

print(frase.split('programar'))

print(len(frase))