#coding: utf-8
listaPal=[]
cant=input("Cuantas palabras tendrá la lista?")
for i in range(1,cant+1):
	aux=raw_input("Dígame la palabra "+str(i)+":")
	listaPal.append(aux)
print "La lista creada es: ",listaPal
for i in range(len(listaPal)-1,-1,-1):
	if listaPal[i] in listaPal[:i]:
		del listaPal[i]
print "Y la lista sin repeticiones es: ",listaPal



