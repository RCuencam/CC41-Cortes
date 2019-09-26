#Ingreso de datos
A=[4,2,7,3]
H=[5,4,2,9]
Area_de_Placa=200

def AreaTotal(resultado):
    n=len(resultado)
    Sumaa=0
    for i in range(n):
        Sumaa+=resultado[i]
    return Sumaa

def Ordenar(resultado):
    resultado.sort(reverse=True)
    #ordenamiento default 
    return resultado
    
def Mostrar_Areas_de_Cortes(A,H):
    n=len(A)
    resultado=[]

    for i in range(n):
        producto=A[i]*H[i]
        resultado.append(producto)
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
	Arreglo_de_Planchas = [] #retorna una lista de placas llena de cortes
	Arreglo_de_Planchas.append(Bin()) #Agregue el primer contenedor vacío a la lista

	for corte in arreglo:
		# Ir a través de contenedores e intentar asignar
		Añadir = False

		for bin in Arreglo_de_Planchas:
			if bin.Suma() + corte <= areaTotal:
				bin.añadirPieza(corte)
				Añadir = True
				break
		
		# Si el artículo no esta asignado en los contenedores de la lista, cree un nuevo contenedor
		# y asignarselo
		if Añadir == False:
			nuevaPlancha = Bin()
			nuevaPlancha.añadirPieza(corte)
			Arreglo_de_Planchas.append(nuevaPlancha)

	# Convierta los contenedores en una lista de artículos y devuélvalos
	arreglo = []
	for bin in Arreglo_de_Planchas:
		arreglo.append(bin.Mostrar())

	return(arreglo)

def Desperdicio():
    resultado=100-((AreaTotal(Mostrar_Areas_de_Cortes(A,H))/Area_de_Placa)*100)
    return resultado

resultado=Contenedores(Ordenar(Mostrar_Areas_de_Cortes(A,H)),Area_de_Placa)
print(resultado)

nroCortes=len(resultado)

print("Los numeros de placas utilizadas son: ",nroCortes)
print("La cantidad de area utilizada es:",AreaTotal(Mostrar_Areas_de_Cortes(A,H)),"m^2")
print("Porcentaje de Area no utilizada: ", Desperdicio(),"%")
