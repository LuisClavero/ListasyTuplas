#coding: utf-8
a=[]
cant=input("Cuantas palabras tendrá la lista?")
for i in range(1,cant+1):
	aux=raw_input("Dígame la palabra "+str(i)+":")
	a.append(aux)
print "La lista creada es: ",a
aux=raw_input("Sustituir la palabra:")
aux2=raw_input("Por la palabra:")
count=a.count(aux)
for b in range(count):
	p=a.index(aux)
	a[p]=aux2
print "La lista ahora es:",a


