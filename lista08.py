#coding: utf-8
listaPal1=[]
listaPal2=[]
cant_lista1=input("Cuantas palabras tendrá la primera lista?")
for i in range(1,cant_lista1+1):
	aux1=raw_input("Dígame la palabra "+str(i)+":")
	listaPal1.append(aux1)
	
print "La primera lista es: ",listaPal1
cant_lista2=input("Cuantas palabras tendrá la segunda lista?")
for x in range(1,cant_lista2+1):
	aux2=raw_input("Dígame la palabra "+str(x)+":")
	listaPal2.append(aux2)
print "La segunda lista es: ",listaPal2
for y in range(listaPal1):
	if listaPal1.count(aux1)==1:
		print 
print "Todas las palabras: ",listaPal1+listaPal2





