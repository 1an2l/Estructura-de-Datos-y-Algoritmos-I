#Funciones
def gauss(n):
    a=0
    for i in range (1,n+1):
        a=a+i
    return a

n1=100
r=gauss(n1)
print("La suma de los primeros "+str(n1)+" números en: "+str(r))


