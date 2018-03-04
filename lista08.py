#coding: utf-8
listaPal1=[]
listaPal2=[]
cant_lista1=input("Cuantas palabras tendrá la primera lista?")
for i in range(1,cant_lista1+1):
	aux1=raw_input("Dígame la palabra "+str(i)+":")
	listaPal1.append(aux1)
print "La primera lista es: ",listaPal1
for i in range(len(listaPal1)-1,-1,-1):
	if listaPal1[i] in listaPal1[:i]:
		del listaPal1[i]
print "La primera lista sin repeticiones es:",listaPal1

cant_lista2=input("Cuantas palabras tendrá la segunda lista?")
for i in range(1,cant_lista2+1):
	aux2=raw_input("Dígame la palabra "+str(i)+":")
	listaPal2.append(aux2)
print "La segunda lista es: ",listaPal2
for i in range(len(listaPal2)-1,-1,-1):
	if listaPal2[i] in listaPal2[:i]:
		del listaPal2[i]
print "La Segunda lista sin repeticiones es:",listaPal2

listaComunes=[]
for i in listaPal1:
	if i in listaPal2:
		listaComunes.append(i)
print "Palabras que están en las dos listas: ",listaComunes

listaPrimera=[]
for i in listaPal1:
	if not i in listaPal2:
		listaPrimera.append(i)
print "Palabras que están solo en la primera lista: ",listaPrimera

listaSegunda=[]
for i in listaPal2:
	if not i in listaPal1:
		listaSegunda.append(i)
print "Palabras que están solo en la segunda lista: ",listaSegunda

todo=listaComunes+listaPrimera+listaSegunda
print "Todas las palabras: ",todo





