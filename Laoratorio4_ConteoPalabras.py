# PROGRAMA CONTEO DE PALABRAS

frase="Dado una frase contar el numero de palabra que contiene"
contador=0
for recorrido in range (0, len(frase)):
	if frase[recorrido] == " ":
		contador=contador+1
print(contador + 1)