#coding: utf-8
a=[]
cant=input("Cuantas palabras tendrá la lista?")
for i in range(1,cant+1):
	aux=raw_input("Dígame la palabra "+str(i)+":")
	a.append(aux)
print "La lista creada es: ",a
a.reverse()
print "Y la lista inversa es: ",a
