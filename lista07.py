#coding: utf-8
listaPal1=[]
listaPal2=[]
cant=input("Cuantas palabras tendrá la lista?")
for i in range(cant-1,-1,-1):
	aux=raw_input("Dígame la palabra "+str(i)+":")
	listaPal1.append(aux)
	listaPal2.append(aux)
	if listaPal2.count(aux)>1:
		listaPal2.remove(aux)
print "La lista creada es: ",listaPal1
print "Y la lista sin repeticiones es: ",listaPal2



