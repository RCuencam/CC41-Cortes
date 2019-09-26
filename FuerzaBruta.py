A=[4,5,6,7]
H=[1,2,3,4]
def MostrarAreas(A,H):
    n=len(A)
    resultado=[]

    for i in range(n):
        producto=A[i]*H[i]

        resultado.append((producto,A[i],H[i]))
    return resultado
	

def Ordenar(resultado):
	lengthOfArray = len(resultado) - 1
	for i in range(lengthOfArray):
		for j in range(lengthOfArray - i):
			if resultado[j][0] < resultado[j + 1][0]:
				resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
	return resultado


    
def AreaTotal(resultado):
    n=len(resultado)
    sumaa=0
    for i in range(n):
        sumaa+=resultado[i]
    return sumaa


def Desperdicio():
    resultado=100-((AreaTotal(MostrarAreas(A,H))/planchaArea)*100)
    return resultado


print(MostrarAreas(A,H))
print(Ordenar(MostrarAreas(A,H)))



