#coding: utf-8
a=[]
cant=input("Cuantas palabras tendrá la lista?")
for i in range (1,cant+1):
	aux=raw_input("Dígame la palabra "+str(i)+":")
	a.append(aux)
print "La lista creada es: ",a
aux2=raw_input("Dígame la palabra a buscar:")
if a.count(aux2)==1:
	print "La palabra '",aux2,"' aparece una vez en la lista"
if a.count(aux2)>1:
	print "La palabra '",aux2,"' aparece",a.count(aux2)," veces en la lista"
if a.count(aux2)<1:
	print "La palabra '",aux2,"' no aparece en la lista"



