#actividad 5 en clase

ventas=0
while True:
    print("____Menu de analisis de ventas____")
    print("op.1 Ingresar lista de ventas: ")
    print ("op2. Mostrar todas las ventas ingresadas: ")
    print("op3. Calcular la venta más alta y la más baja: ")
    print("op4. Calcular promedio de ventas: ")
    print("op5. Contar cuantos días superaron los Q1000: ")
    print("op.6 Buscar si una  venta especifica existe en la lista: ")
    print("op.7 Clasificar cada venta: alta(>1000), medio (500-1000), baja (<500)")
    print("op.8  Salir")

    op= input("ingrese su opcion: ")
    match op:
        case "1":
            va1= int(input("Ingrese su lista de ventas: "))

        case "2"
