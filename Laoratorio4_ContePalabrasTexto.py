# PROGRAMA PARA CONTAR LAS PALABRAS CONTENIDAS EN UN TEXTO
contador=0

def abrirTexto():
	archivo=open('texto.txt', a)
	cadena=archivo.read()
	archivo.close()
	return cadena

def conteoPalabras(texto):
	for i in range (0, len(texto)):
		if text[i]== " ":
			contador=contador+1
	print(contador)

conteoPalabras(abrirTexto())
