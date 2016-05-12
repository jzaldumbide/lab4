# PROGRAMA PARA CONTAR LAS PALABRAS CONTENIDAS EN UN TEXTO
cont=0

def abrirTexto():
	archivo=open('texto.txt', 'r')
	cadena=archivo.readline()
	archivo.close()
	return cadena

def conteoPalabras(texto):
	for i in range (0, len(texto)):
		if texto[i]==" ":
			cont+=cont
	print(cont)

conteoPalabras(abrirTexto())