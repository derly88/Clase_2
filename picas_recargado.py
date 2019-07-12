from random import randint

def lista_inicial(tam):
    lista=[]
    while len(lista)<tam:
        num=randint(1,9)
        if num not in lista:
            lista.append(num)

    return lista

def ingreso_num (lista):
    var=[int(x) for x in list(raw_input("ingrese un numero de 3 digitos: "))]
    if len(var)!=len(lista):
        print "el numero ingresado no es de 3 digitos"
        return ingreso_num(lista)
    return var



def comparar (lista,n):
    p=0
    f=0
    for i in range (len(lista)):
        if lista [i]in n:
            if lista[i]==n[i]:
                f+=1
            else:
                p+=1

    return p,f
 



def juego():
    matriz=[]
    lista= lista_inicial(3)
    x=0
    i=4
    while True:
        n = ingreso_num(lista)     
        picas,fijas= comparar (lista,n)
        print "tiene "+ str(picas)+" picas y "+str(fijas)+ " fijas le quedan "+str(i)+" intentos"
        matriz.append([n,picas,fijas])
        x+=1
        i-=1
        if fijas==3:
            print"ganaste"
            break
        if x==5:
            print"perdiste te quedan "+str(i)+" intentos"
            break
    for i in matriz:
        print i
juego()
'''       
def matriz():
    picas,fijas= comparar (lista,n)
    n=ingreso_num(lista)
    matriz_nueva=[]
    for i in n[i]:
        matriz_nueva.append(i)
        matriz_nueva.append 
    return i
matriz()'''
