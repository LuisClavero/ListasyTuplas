#coding: utf-8
a=[]
b=[]
cant=input("Cuantas palabras tendrá la lista?")
for i in range(1,cant+1):
	aux=raw_input("Dígame la palabra "+str(i)+":")
	a.append(aux)
print "La lista creada es: ",a
cant=input("Cuantas palabras tendrá la lista a eliminar?")
for e in range(1,cant+1):
	aux=raw_input("Dígame la palabra "+str(e)+":")
	b.append(aux)
	while aux in a:
		a.remove(aux)
print "La lista de palabras a eliminar es:",b
print "La lista ahora es:",a
