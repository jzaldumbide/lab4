import goslate
with open('ingles.txt','r') as f:
 	novel_txt=f.read()
gs=goslate.Goslate()
gs.translate(novel_txt,'en')

#Poner la direccion absoluta del archivo 

