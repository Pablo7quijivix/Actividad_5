#actividad 5 en clase
dias = []
ventas = []
while True:
    print("========Menu de analisis de ventas=======")
    print("==op.1 Ingresar lista de ventas (ingrese cuantos dias desea agreagar y su respectivo monto): ")
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
            dia= int(input("Cuantos dias desea ingresar?: "))
            dias.append(dia)
            for i in (dia):
                cantidad_ventas= int(input(f"Ingrese cantidad de ventas del dia {i+1}: "))
                ventas.append(cantidad_ventas) #agrega la cantidad de ventas por dia a la lista "ventas"

        case "2":
            print("Mostrando ventas ingresadas",ventas)

        case "3":
            for i in ventas:
                print("hola")

        case "4":
            promedio = sum(ventas) / len(ventas)
            print (f"El promedio de ventas es: {promedio}")

        case "5":
           len

