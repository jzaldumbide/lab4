contador=int(0)
frase =input("ingrese una frase \n")
fraux=frase.split (" ")
for i in fraux:
	contador=contador+1
print("El numero de palabras ingresadas es"+str(contador))
 