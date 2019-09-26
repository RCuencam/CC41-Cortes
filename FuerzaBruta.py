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


def Desperdicio():
    resultado=100-((AreaTotal(MostrarAreas(A,H))/planchaArea)*100)
    return resultado

A=[4,5,6,7]
H=[1,2,3,4]
planchaArea=200


print(AreaTotal(MostrarAreas(A,H)))
print(Desperdicio(),"%")
