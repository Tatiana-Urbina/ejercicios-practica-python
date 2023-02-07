"""Manipulación de una lista
1- capturar lista.
2- Mostrar Lista
3- Agregar un elemento a la Lista.
4- Eliminar un elemento de la lista
5- Modificar un elemento de la lista.
6- Salir"""


#Def. la Función Capturar
def capturar():
    global lista
    lista=[]
    print ("¿Cuantos elementos va a tener la Lista?")
    n= input()
    n= int(n)
    for i in range(0,n):
        print ("Ingrese el Elemento del índice ", i)
        elemento=input()
        lista.insert(i, elemento)

#capturar()

#def. Función Mostrar
def mostrar():
    print(lista)

#Función agregar un elemnto a la lista
def agregar():
    print("Ingrese el elemento que desea agregar:")
    elemento=input()
    print("Ingrese el índice donde desea agregarlo:")
    indice=input()
    indice=int(indice)
    longitud=len(lista)
    longitud=int(longitud)
    if(indice>longitud or indice<0):
        print("el indice debe estar entre 0 y ", longitud)
    else:
        lista.insert(indice,elemento)
        print("Elemento Agregado")
        
#Def. función eliminar

def eliminar():
    print("Ingrese el índice del elemento que desea eliminar:")
    indice=input()
    indice=int(indice)
    longitud=len(lista)
    longitud=int(longitud)
    if(indice>longitud or indice<0):
        print("el indice debe estar entre 0 y ", longitud-1)
    else:
        del lista[indice]
        print("Elemento Eliminado")


#Def. función Modificar
def modificar():
    print("Ingrese el indice del elemento que desea modificar: ")
    indice=input()
    indice=int(indice)
    print("Ingrese el Nuevo valor del elemento:")
    elemento=input()
    longitud=len(lista)
    longitud=int(longitud)
    if(indice>longitud or indice<0):
        print("El índice debe estar entre 0 y ", longitud-1)
    else:
        lista[indice]=elemento
        print("Elemento Modificado")    

#Def. función principal

def principal():
    opcion= "1"
    while (opcion != "6"):
        print("¿Qué deseas hacer?")
        print("1 Capturar lista")
        print("2 Mostrar Lista")
        print("3 Agregar un Elemento a la Lista")
        print("4 Eliminar un elemento de la lista")
        print("5 modificar un elemento de la lista")
        print("6 salir")
        opcion=input()
        if (opcion=="1"):
            capturar()
        elif (opcion=="2"):
            mostrar()
        elif (opcion=="3"):
            agregar()
        elif(opcion=="4"):
            eliminar()
        elif(opcion=="5"):
            modificar()
        elif(opcion=="6"):
            print("Programa terminado")
        else:
            print("¡Opción Incorrecta!")



#LLamando a la función principal
principal()