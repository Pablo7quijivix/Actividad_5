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
    # print("==op.6 Buscar si una  venta especifica existe en la lista: ")
    print("==op.6 Clasificar cada venta: alta(>1000), medio (500-1000), baja (<500)")
    print("==op.7  Salir")

    op=input("eliga una opcion 1-7: ")
    match op:
        case "1":
           dia= int(input("Cuantos dias desea ingresar?: "))
           if dia <= 0:
                print("DIGITE UNA CANTIDAD DE DIAS VALIDOS")
           else:
            dias.append(dia)
            for i in range (dia):
                cantidad_ventas = int(input(f"Ingrese cantidad de ventas del dia {i + 1}: "))
                ventas.append(cantidad_ventas) #agrega la cantidad de ventas por dia a la lista "ventas"

        case "2":
            print("=====Mostrando ventas ingresadas=====\n",ventas)
            if not ventas:
                print("No hay ventas ingresadas.")
            else:
                for i in range (dia):
                    print(f"Dia {i+1} Ventas= Q{ventas[i]}")

        case "3":
            for i in ventas:
                print("\n========Calculo de ventas========")
                venta_max = max(ventas)
                venta_min = min(ventas)
                print(f"La venta más alta es: Q{venta_max}")
                print(f"La venta más baja es: Q{venta_min}")

        case "4":
            promedio = sum(ventas) / len(ventas)
            print (f"El promedio de ventas es: {promedio}")

        case "5":
            if not ventas:
                print("aun no existen ventas")
            else:
                dias_mayores_1000 = 0
                for venta in ventas:
                    dias_mayores_1000 +=1
                    print(f"Los dias que superaron las ventas de Q1000.00 son: {dias_mayores_1000}")



