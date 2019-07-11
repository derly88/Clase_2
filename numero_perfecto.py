def divisores(numero):
#lista por comprension
    return [x for x in range(1,numero)if numero % x==0]
print divisores(6)

#lista por recursividad
def divisores_rec(num,aux):
    if aux==num:
        return []
    if num % aux ==0:
        return [aux]+divisores_rec(num, aux+1)
    return divisores_rec(num, aux+1)

def suma (numero):
    if sum (divisores_rec(numero,1))==numero:
        print "el numero es perfecto"
    else:
        print "no es perfecto"


def perfecto (num):
    return sum (divisores(num))==num
n=input("ingrese numero ")

if perfecto(n):
    print str(n)+"es perfecto "
else:
    print str(n)+"no es perfecto "

def primeros(num):
    lista=[]
    i=1
    while len (lista)<num:
        if perfecto(i):
            lista.append(i)
        i+=1
    return lista
print "los primeros 4 son: "+str(primeros(4))

        
        
        
        


