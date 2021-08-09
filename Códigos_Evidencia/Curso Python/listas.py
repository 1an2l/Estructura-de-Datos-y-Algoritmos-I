#listas
a=[1,4,-3,2]
print(a)
print("\n")
for i in a:
    print(i+10)

a.append(10)
print(a)
a.remove(10)
print(a)
a.insert(3,10)
print(a)
print("El numero -3 se encuentra en la posición "+str(a.index(-3)))
print("El tamaño de nuestra lista es: "+str(len(a)))

b=sorted(a)
print(b)

a.sort()
print(a)
print(min(a))
print(max(a))