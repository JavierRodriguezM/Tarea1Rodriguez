#Función que devuelve todos los divisores de un número dado
def divisores(n):
    if isinstance(n, int)==True and n>=1:
        resultado=[]
        for a in range(1,n):
            if n%a==0:
                resultado.append(a)
        return resultado
    else:
        return "Error: debe indicar un número >=1"
