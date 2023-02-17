mes = input("Ingrese un mes: ")
importe= float(input("ingrese el importe de la cuota: "))
compra_descuento= importe - (importe * 0.15)
if mes == "octubre" or mes== "Octubre":
    print("El importe a cobrar con el descuento es de: $", compra_descuento)
else:
    print("El importe a cobrar es: ", importe)