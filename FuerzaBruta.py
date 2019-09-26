def MostrarAreas(G):
	n=len(G)
	resultado=[]

	for i in range(n):
		producto=G[i][0]*G[i][1]
		resultado.append((producto,G[i][0],G[i][1]))
	return resultado

def AreaTotal(resultado):
    n=len(resultado)
    sumaa=0
    for i in range(n):
        sumaa+=resultado[i]
    return sumaa

class Bin:
    def __init__(self):
        self.list = []
 
    def AñadirPlaca(self, item):
        self.list.append(item)
 
    def suma(self):
        total = 0
        for elem in self.list:
            total += elem
        return total
 
    def Mostrar(self):
        return self.list
 
def BinPacking(arreglo, areaPlancha):
    """ Returns list of bins with input items inside. """
    a = []
    a.append(Bin()) 
 
    for item in arreglo:
       
        añadir = False
 
        for bin in a:
            if bin.suma() + item <= areaPlancha:
                bin.AñadirPlaca(item)
                añadir = True
                break
       
        
        if añadir == False:
            nuevo = Bin()
            nuevo.AñadirPlaca(item)
            a.append(nuevo)
 
    arreglo = []
    for bin in a:
        arreglo.append(bin.Mostrar())
 
    return(arreglo)

def SepararArea(arreglo):
	n=len(arreglo)
	a=[]

	for i in range(n):
		a.append(arreglo[i][0])
	
	return a

'''def BinPacking(arreglo,araPlancha):


	a=[]
	opcional=[]
	resultado=[]
	suma=0

	for item in arreglo:
		añadir=False

		for Cortes in a:
			suma+=arreglo[i][0]
			if suma<=15:
				Cortes.añadir(item)
				añadir=True
				break

	for i in range(len(arreglo)):
		suma+=arreglo[i][0]
		if suma<=15:
			Cortes.añadir a.append((arreglo[i]))
		else:
			opcional.append((arreglo[i]))

	resultado.append(a)
	resultado.append(opcional)
	return resultado'''
	
def Desperdicio(volumen):
	resultado=100-((volumen/planchaArea)*100)
	return resultado

def imprimir():
	print("Area,ancho,alto")
	print(MostrarAreas(G))
	volumen=SepararArea(MostrarAreas(G))
	
	print("Sólo las areas")
	print(volumen)
	
	print("Separando los cortes en cada plancha")
	resultado=BinPacking(volumen,planchaArea)
	print(resultado)
	
	nroCortes=len(resultado)
	print("Numero de Planchas: ",nroCortes)
	
	print("Area Total:")
	print(AreaTotal(volumen))
	print(Desperdicio(AreaTotal(volumen)),"%")


#Entrada de datos
G=[(4,5),(1,3),(2,4),(5,6)]
planchaArea=30
print(imprimir())