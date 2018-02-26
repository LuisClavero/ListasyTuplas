#coding: utf-8
a=[]
cant=input("Cuantas palabras tendrá la lista?")
for i in range(1,cant+1):
	aux=raw_input("Dígame la palabra "+str(i)+":")
	a.append(aux)
print "La lista creada es: ",a
aux=raw_input("Palabra a eliminar:")
for p in range(0,a.count(aux)):
	a.remove(aux)
print "La lista ahora es:",a
