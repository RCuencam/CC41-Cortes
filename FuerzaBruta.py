def CalcularArea(A,H):
    n=len(A)
    resultado=[]

    for i in range(n):
        producto=A[i]*H[i]
        resultado.append(producto)
    return resultado

def Ordenar(resultado):
    resultado.sort(reverse=True)
    return resultado
    

def Cortes()

A=[4,5,6,7]
H=[1,2,3,4]

print(Ordenar(CalcularArea(A,H)))