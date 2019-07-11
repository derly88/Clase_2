from random import randint

def lista_inicial(tam):
    lista=[]
    while len(lista)<tam:
        num=randint(1,9)
        if num not in lista:
            lista.append(num)
#    return lista
    print lista
    return lista

def ingreso_num (lista):
    var=[int(x) for x in list(raw_input("ingrese un numero de 3 digitos: "))]
    if len(var)!=len(lista):
        print "el numero ingresado no es de 3 digitos"
        return ingreso_num(lista)
    return var

lista= lista_inicial(3)
n = ingreso_num(lista)

def comparar (lista,n):
    x=0
    y=0
    while x<5:
        for ....
        if lista==n:
            print "ganaste"
        elif
            print "le quedan "+str((x-1))+"intentos pruebe nuevamente"
    x+=1
    return comparar(lista,n)

            
            
     
        
        


    
        

