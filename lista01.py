#coding: utf-8
cant=int(input("Cuantas palabras tendrá la lista?"))
if cant<1:
	print "Imposible"
else:
	a=[]
	for i in range(cant):
		pal2=raw_input("Escriba una palabra para añadir en la lista:")
		a.append(pal2)
print "La lista creada es:",(a) 
