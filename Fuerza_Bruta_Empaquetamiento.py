#Ingreso de datos
G=[(4,5),(1,3),(3,4),(5,6)]
Area_Plancha=200


def AreaTotal(resultado):
    n=len(resultado)
    sumaa=0
    for i in range(n):
        sumaa+=resultado[i]
    return sumaa

def Ordenar(resultado):
	n=len(resultado) - 1
	for i in range(n):
		for j in range(n-i):
			if resultado[j]<resultado[j+1]:
				resultado[j],resultado[j+1]=resultado[j+1],resultado[j]
	return resultado

def Mostrar_Areas_de_Cortes(G):
	n=len(G)
	resultado=[]

	for i in range(n):
		producto=G[i][0]*G[i][1]
		resultado.append((producto,G[i][0],G[i][1]))
	return resultado

class Bin:
	def __init__(self):
		self.list = []

	def añadirPieza(self, corte):
		self.list.append(corte)

	def Remover_Corte(self, corte):
		self.list.remove(corte)

	def Suma(self):
		total = 0
		for elem in self.list:
			total += elem
		return total

	def Mostrar(self):
		return self.list

def Contenedores(arreglo, areaTotal):
	Arreglo_de_Planchas = [] 
	Arreglo_de_Planchas.append(Bin()) 

	for corte in arreglo:
		Añadir = False

		for bin in Arreglo_de_Planchas:
			if bin.Suma() + corte <= areaTotal:
				bin.añadirPieza(corte)
				Añadir = True
				break
		
		
		if Añadir == False:
			nuevaPlancha = Bin()
			nuevaPlancha.añadirPieza(corte)
			Arreglo_de_Planchas.append(nuevaPlancha)

	arreglo = []
	for bin in Arreglo_de_Planchas:
		arreglo.append(bin.Mostrar())

	return(arreglo)

def Desperdicio():
    resultado=100-((AreaTotal(Mostrar_Areas_de_Cortes(A,H))/Area_Plancha)*100)
    return resultado

print(Mostrar_Areas_de_Cortes(G))
print(Ordenar(Mostrar_Areas_de_Cortes(G)))
resultado=Contenedores(Ordenar(Mostrar_Areas_de_Cortes(G)),Area_Plancha)
print(resultado)

nroCortes=len(resultado)
print("Los numeros de cortes son: ",nroCortes)
print("La cantidad de area utilizada es:",AreaTotal(Mostrar_Areas_de_Cortes(G)),"m^2")
print("Porcentaje de Area no utilizada: ", Desperdicio(),"%")
