lista=["Sole", "Marta", "Javier"]
for i in lista:
    print(i)


"""Si necesitamos un índice acompañado con la lista, que tome valores desde 0 hasta n-1,
se puede hacer de la siguiente manera."""

lista=["Sole", "Marta", "Javier"]
for index, i in enumerate (lista):
    print(index, i)

"""O si tenemos dos listas y las queremos iterar a la vez, también es posible hacerlo."""
lista1 = [10, 65, 11]
lista2 = ["Lore", "Rubén", "Ignacio"]
for l1, l2 in zip(lista1, lista2):
    print(l1, l2)