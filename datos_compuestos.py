#--------LISTAS/MATRIZ------------
lista=["Maria", True, 1.85, "curso"]

# print(lista)
#-----------------------------------------------------
#mostrar el elemento en posicion 1
# print(lista[1])
# print(lista[-2])
#print(lista[:]) lista completa
# print(lista[:-3]) 
# print(lista[2:])desde 2 y limite final
# print(lista[2:4])desde 2 y limite 4
# -----------------------------------------------------
#agregar un elemento a una posicion determinada
#lista.insert(2,"sandra") #agrega "Sandra en la posición 2"
# print(lista)
#eliminar un elemento a la lista 

#-----------------------------------------------------
#agregar al final con el elemento append
#se agrega de a 1
#si quiero agregar 2 tengo que hacer 2 veces el método append
# lista.append("luis")
# print(lista)

#------------------------------------------------------
#EXTEND -- EXTENDER LA LISTA, UNA LISTA DENTRO DE LA OTRA LISTA
#agrega detra de la lista que ya se tenía
lista.extend(["Javier", 85, False, "cecilia"])
# print(lista)

#INDEX------ proporciona el indice de determinado elemento
# print(lista.index("cecilia"))
# -------------------------------------------------
#BUSCAR UN ELEMENTO EN LA LISTA
# print("Javier" in lista) #devuelve True o False


#----------------------REMOVE---------------------------------------
#pasomos el elemento que queremos eliminar
# lista.remove("cecilia") #saca un valor de la lista
# print(lista)

#--------------------POP- elimina el ultimo elemento
# lista.pop()


# concatenar otra lista

# lista1 = [3.12, "Erika", False, 9]

# lista2 = lista + lista1 

# print(lista2)
#la diferencia con extend es que podemos pasar la lista que queremos 
#que nos concatene primero. lista1 + lista o lista + lista1

#----------------------------

#si agrego el signo de multiplicacion me replica la lista

# lista=["Maria", True, 1.85, "curso"] * 3

# print(lista)
