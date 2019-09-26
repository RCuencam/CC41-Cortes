def MostrarAreas(A,H):
    n=len(A)
    resultado=[]

    for i in range(n):
        producto=A[i]*H[i]
        resultado.append(producto)
    return resultado

def Ordenar(resultado):
    resultado.sort(reverse=True)
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

	def añadirPieza(self, corte):
		self.list.append(corte)

	def removecorte(self, corte):
		self.list.remove(corte)

	def suma(self):
		total = 0
		for elem in self.list:
			total += elem
		return total

	def Mostrar(self):
		return self.list

def Contenedores(arreglo, areaTotal):
	#retorna una lista de placas con corte de entrada dentro
	arregloPlancha = []
	arregloPlancha.append(Bin()) #Agregue el primer contenedor vacío a la lista

	for corte in arreglo:
		# Ir a través de contenedores e intentar asignar
		Añadir = False

		for bin in arregloPlancha:
			if bin.suma() + corte <= areaTotal:
				bin.añadirPieza(corte)
				Añadir = True
				break
		
		# Si el artículo no esta asignado en los contenedores de la lista, cree un nuevo contenedor
		# y asignarselo
		if Añadir == False:
			nuevaPlancha = Bin()
			nuevaPlancha.añadirPieza(corte)
			arregloPlancha.append(nuevaPlancha)

	# Convierta los contenedores en una lista de artículos y devuélvalos
	arreglo = []
	for bin in arregloPlancha:
		arreglo.append(bin.Mostrar())

	return(arreglo)

def Desperdicio():
    resultado=100-((AreaTotal(MostrarAreas(A,H))/planchaArea)*100)
    return resultado

A=[4,5,6,7]
H=[1,2,3,4]
planchaArea=200

resultado=Contenedores(Ordenar(MostrarAreas(A,H)),planchaArea)
print(resultado)
nroCortes=len(resultado)
print("Los numeros de cortes son: ",nroCortes)
print(AreaTotal(MostrarAreas(A,H)))
print(Desperdicio(),"%")
