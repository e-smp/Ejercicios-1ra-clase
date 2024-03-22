#Segundo Ejercicio primera clase:
def calcularPago(ingresos, costo_casa):
    if ingresos >= 80000:
        pie = 0.15 * costo_casa
        pagos_mensuales = (costo_casa - pie) / (10 * 12)#pagos mensuales por 10 años.
    else:
        pie = 0.30 * costo_casa
        pagos_mensuales = (costo_casa - pie) / (7 * 12) #pagos mensuales por 7 años.
    
    return pie, pagos_mensuales
#función para que el usuario pueda ingresar sus datos:
def ingresarDatos():
    ingresos = float(input("Ingrese los ingresos del comprador: "))
    costo_casa = float(input("Ingrese el costo de la casa: "))
    return ingresos, costo_casa
#procedimiento que muestra los datos:
def mostrarResultado(pie, pagos_mensuales):
    print("Monto del pie:", pie)
    print("Monto de los pagos mensuales:", pagos_mensuales)
#menú interactivo para el usuario:
def menu():
    print("Bienvenido al calculador de pagos de casas de interés social")
    print("1. Calcular pagos")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ingresos, costo_casa = ingresarDatos()
        pie, pagos_mensuales = calcularPago(ingresos, costo_casa)
        mostrarResultado(pie, pagos_mensuales)
    elif opcion == "2":
        print("Gracias por usar el programa")
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")
        menu()

menu()

        