import os
os.system("cls")

pnombre=input(str("\n\nEscribe tu nombre: "))
snombre=input(str("Escribe tu segundo nombre si no tienes pon un espacio y da enter: "))
apellidop=input(str("Escibe tu apellido paterno: "))
apellidom=input(str("Escibe tu apellido materno: "))

print("\nTu nombre Completo es: \n",pnombre,snombre,apellidop,apellidom)
print("\nTus iniciales en forma respectiva son: \n",pnombre[0],", ",snombre[0],", ",apellidop[0],", ",apellidom[0])