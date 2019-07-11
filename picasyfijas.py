from random import randint


'''
for i in range (30)'''

def generar_lista(tam)
    lista=[]
    while len(lista)<tam:
        numero=randint(1,9)
        if numero not in lista:
            lista.append(numero)
    return lista
        
#print generar_lista(3)
#suma con iteradores
def suma(lista)
acum=0
    for i in lista:
        acum+=i
    return acum
lista=generar_lista
print suma(lista)

#suma recursiva
def sum_recursiva(lista):
    if lista==[]
    return lista [0]+suma_recursiva([1:])


def ordenar (lista):
    for i in range (len(lista)):
        for j in range (i+1,len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista


print lista
print suma(lista), sum_recursiva(lista)

        

    
