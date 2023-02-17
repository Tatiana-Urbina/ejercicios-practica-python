#Condicional compuesto
"""Ingresar un número y devolver por pantalla si es positivo o negativo"""

num= int(input("Ingrese un número: "))
if num>0:
    print("El número ingresado es positivo", num)
elif num==0:
    print("El número ingresado es neutro", num)
else: 
    print("El número ingresado es negativo:", num)