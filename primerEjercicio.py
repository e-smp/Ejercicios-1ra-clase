"""Un teatro otorga descuentos según la edad del cliente. Determinar la cantidad de dinero que el teatro
deja de percibir por cada una de las categorías. Tomar en cuenta que los niños menores de 5 años
no pueden entrar al teatro y que existe un precio único en los asientos. Los descuentos se hacen
tomando en cuenta el siguiente cuadro:
Edad Descuento
 Categoría 1 5 - 14 35 %
 Categoría 2 15 - 19 25 %
 Categoría 3 20 - 45 10 %
 Categoría 4 46 - 65 25 %
 Categoría 5 66 en adelante 35 %
Desarrollar haciendo uso de:
a.1) Usar estructura condicional/selección simple
a.2) Usar estructura condicional/selección doble
Ejercicios a desarrollar
"""

edadComprador=int(input("Ingrese la edad para indicar el descuento según su categoría: "))
precioEntrada=10000
descuentoEntrada=float

if edadComprador <5:
    print("Las personas con una edad menor a 5 años no pueden ingresar al teatro.")
elif edadComprador >=5 and edadComprador <=14:
    descuentoEntrada = precioEntrada*0.35
    print(f"El descuento de la categoría 1 es de: {descuentoEntrada}$")
elif edadComprador >=15 and edadComprador <=19:
    descuentoEntrada = precioEntrada*0.25
    print(f"El descuento de la categoría 2 es de: {descuentoEntrada}$")
elif edadComprador >=20 and edadComprador <=45:
    descuentoEntrada = precioEntrada*0.10
    print(f"El descuento de la categoría 3 es de: {descuentoEntrada}$")
elif edadComprador >=46 and edadComprador <=65:
    descuentoEntrada = precioEntrada*0.25
    print(f"El descuento de la categoría 4 es de: {descuentoEntrada}$")
else:
    descuentoEntrada = precioEntrada*0.35    
    print(f"El descuento de la categoría 5 es de: {descuentoEntrada}$")