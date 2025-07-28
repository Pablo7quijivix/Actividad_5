#actividad 5 en clase
ventas= []
while True:
    print("========Menu de analisis de ventas=======")
    print("==op.1 Ingresar lista de ventas: ")
    print("==op.2 Mostrar todas las ventas ingresadas: ")
    print("==op.3 Calcular la venta más alta y la más baja: ")
    print("==op.4 Calcular promedio de ventas: ")
    print("==op.5 Contar cuantos días superaron los Q1000: ")
    print("==op.6 Buscar si una  venta especifica existe en la lista: ")
    print("==op.7 Clasificar cada venta: alta(>1000), medio (500-1000), baja (<500)")
    print("==op.8  Salir")

    op=input("eliga una opcion 1-8")
    match op:
        case "1":
            va1= int(input("Ingrese su lista de ventas: "))

        case "2":
            print("Mostrando ventas ingresadas",ventas)

        case "3":
            for i in ventas:
                print("hola")

        case "4":
            suma = sum(ventas)
            cantidad_numeros = len(ventas)
            promedio = suma / cantidad_numeros
            print (f"El promedio de ventas es: {promedio}")

        case "5":

