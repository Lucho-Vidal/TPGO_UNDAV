def es_bisiesto (anio):
    """ Recibe por parámetro un número que representa un año. se considera bisiesto aquellos
    que sean divisibles por 4 y no divisible por 100 o divisible por 400 
    Devuelve un valor booleano que indica si el año es bisiesto o no lo es."""
    bisiesto = False
    if anio%4 == 0:
        if anio%100 != 0 or anio%400==0:
            bisiesto = True
    return bisiesto   
def cant_dias_mes (mes, anio): 
    """Recibe por parámetro 2 números que representen el mes y el año. 
    Devuelve como resultado la cantidad de días de ése mes. 
    Invoca a la función es_bisiesto (anio)."""
    cant_dias=0#si el mes o el año no son correctos devuelve 0
    if mes == 1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        cant_dias=31
    elif mes == 4 or mes==6 or mes==9 or mes==11:
        cant_dias=30
    elif mes == 2:
        if es_bisiesto(anio):
            mes=29
        else:
            mes=28
    return cant_dias
def valida_fecha(dia,mes,anio):
    """ Recibe por parámetro una fecha en números (Día, mes y año), 
    Devuelve un valor booleano que indica si esa fecha es válida o no. 
    Invoca a la función cant_dias_mes (mes, anio). ademas la fecha no puede ser inferior a 2022"""
    es_valida = False
    dia_max = cant_dias_mes(mes,anio)
    if dia_max>0 and dia <= dia_max and anio>=2022:
        es_valida = True
    return es_valida
def valida_cant (cantidad):
    """ Valida que cantidad de productos este dentro de los parámetros solicitados. """
    return cantidad >= 0 and cantidad <= 10
def dni_valido(dni):
    """Cada número de DNI de socia/o debe ser mayor a 5 millones y menor que 99 millones.
    Devuelve un boolean"""
    return dni>5000000 and dni<99000000
def precio_valido(precio):
    """El precio unitario de venta de cada producto debe ser mayor a 10 y menor que 1000"""
    return precio >10 and precio < 1000
def valida_correo (correo):
    """ Recibe por parámetro una cadena de caracteres. Devuelve un valor booleano que indica
     si la cadena de caracteres cumple con el formato de un correo electrónico. 
     El correo electrónico (debe contener un único carácter "@", uno o más caracteres "." 
     y ningún carácter espacio, además, ni el primero ni el último carácter puede ser "@" ni ".") """
    valido = False
    cont_arroba=0
    cont_punto=0
    # el primer y ultimo carácter no pueden ser: 64 -> '@', 46 -> '.'
    if ord(correo[0])!=64 or ord(correo[0])!=46 or ord(correo[len(correo)-1])!=64 or ord(len(correo)-1)!=46:
        valido = True
        for c in correo:
            # no pueden haber espacios (32) 
            if ord(c)==32:
                valido = False
            # cuento la cantidad de '@'
            if ord(c)==64:
                cont_arroba+=1
            # cuento la cantidad de '.'
            if ord(c)==46:
                cont_punto+=1
        if cont_arroba!=1 or cont_punto==0:
            valido=False
    return valido
def pedir_fecha():
    print("A continuación ingresé la fecha de entrega")
    dia = int(input("Por favor, ingrese el dia\n"))
    mes = int(input("Por favor, ingrese el mes\n"))
    anio =int( input("Por favor, ingrese el año\n"))
    while not(valida_fecha(dia,mes,anio)):
        print("Hubo un error en la validación, Por favor ingrese una fecha de entrega valida")
        dia = int(input("Por favor, ingrese el dia\n"))
        mes = int(input("Por favor, ingrese el mes\n"))
        anio = int(input("Por favor, ingrese el año\n"))
    print("Fecha de entrega {}/{}/{}".format(dia,mes,anio))
def pedir_precios():
    """Solicito precio unitario de cada producto a la venta, valido entre 10<precio<1000"""
    productos = ("Yerba Mate 1kg","Té Negro 100grs","Té Verde 100grs","Miel Mistol ½ kg","Miel Algarrobo 1kg")
    precio_productos={}
    for producto in productos:
        precio=int(input("Ingrese el precio de {}\n".format(producto)))
        while not precio_valido(precio):
            print("Ocurrió un error en la validación de precio, Por favor introducir valores entre $10 y $1000")
            precio=int(input("Ingrese el precio de {}\n".format(producto)))
        precio_productos[producto] = precio
    # imprimo los precio
    for clave in precio_productos:
        print("{} -> ${} ".format(clave,precio_productos[clave]) )
    return precio_productos
def hacer_pedido(productos):
    """por cada socio se pide: DNI, Mail, cantidad unidades de cada producto solicitado.
    Cada venta debe tener al menos 1 producto y no más de 10 unidades por producto"""
    dni = int(input("Ingrese DNI del Socio\n"))
    while not dni_valido(dni):
        print("Ocurrió un error en la validación de DNI, ingrese nuevamente!")
        dni = int(input("Ingrese DNI del Socio\n"))
    correo = input("Ingrese mail del Socio\n")
    while not valida_correo(correo):
        print("Ocurrió un error en la validación de correo, ingrese nuevamente!")
        correo = input("Ingrese correo del Socio\n")
    productos_vendidos={}
    prod_no_comprado = 5
    while prod_no_comprado == 5:
        for producto in productos:
            cant_producto = int(input("Ingrese cantidad de {} al pedido.\n".format(producto)))
            while not valida_cant(cant_producto):
                print("Ocurrió un error en la validación de la cantidad de productos, la cantidad no puede ser superior a 10 unidades por producto. Por favor ingrese nuevamente!")
                cant_producto = int(input("Ingrese cantidad de {} al pedido.\n".format(producto)))
            productos_vendidos[producto] = cant_producto
        # reviso que se haya vendido al menos un producto de lo contrario pide rehacer pedido
        prod_no_comprado = 0
        for producto in productos_vendidos:
            if productos_vendidos[producto] == 0: 
                prod_no_comprado +=1
        if prod_no_comprado == 5:
            print("\nNo se detecto que haya solicitado algún producto. Vuelva a intentarlo")
        else:
            print("\nDNI:{}".format(dni))
            print("Correo:{}".format(correo))
            print("Productos solicitados: ")
            suma_total=0
            for producto in productos_vendidos:
                print("Producto:{}  Cant: {} Importe unitario:$ {} Importe total producto: ${}".format(producto,productos_vendidos[producto],productos[producto],productos_vendidos[producto]*productos[producto]))
                suma_total +=productos_vendidos[producto]*productos[producto]
            print("El importe total del pedido es:$ {}".format(suma_total))
    return productos_vendidos
def calcular_ingresos(precios,pedidos):
    """se recibe un diccionario con los precios y una lista con los pedidos
    se calcula: la cantidad total de ventas informadas, 
    el monto total resultante de esas ventas, 
    el porcentaje de los casos que incluyan los 5 tipos de productos,
    la cantidad de unidades vendidas por producto,
    y la mayor venta ingresada"""
    monto_total = 0
    ventas_5tipos = 0
    cant_uni_prod = {}
    for producto in precios:
        cant_uni_prod[producto] = 0
    mayor_venta = 0
    # recorro la lista
    for pedido in pedidos:
        prod_vend = 0
        monto_pedido = 0
        # recorro el diccionario
        for producto in pedido:
            # pedido[producto]=Cantidad // precios[producto]=precio
            monto_pedido = monto_pedido + pedido[producto]*precios[producto]
            # cuento si se vendieron todos los productos
            if pedido[producto] != 0:
                prod_vend += 1
            # voy a sumar la cantidades que se vendieron por producto
            cant_uni_prod[producto] = cant_uni_prod[producto] + pedido[producto]
        monto_total = monto_total + monto_pedido
        # busco que pedido tiene el mayor importe
        if mayor_venta < monto_pedido:
            mayor_venta = monto_pedido
        # si se vendieron todos los producto sumo al contador
        if prod_vend == 5:
            ventas_5tipos += 1

    print("\nLa cantidad de ventas realizadas fueron: {}".format(len(pedidos)))
    print("El monto total de las ventas es: ${}".format(monto_total))
    print("El porcentaje de las ventas de los 5 tipos de productos es: {}%".format((ventas_5tipos*100)/len(pedidos)))
    print("La cantidades de unidades vendidas por producto:")
    for producto in cant_uni_prod:
        print("{}: {}".format(producto,cant_uni_prod[producto]))
    print("El importe de la mayor venta ingresada es: {}\n".format(mayor_venta))
def main():
    print("Bienvenidos a la Cooperativa de consumo Quinchahue")
    pedir_fecha()
    precio_productos = pedir_precios()
    productos_vendidos = []
    option = -1
    # Menu principal
    while option !=0:
        print("\nMenu principal\n1.Ingresar nuevo pedido\n2.Calcular ingresos\n0.Salir")
        option = int(input("Seleccioné una opción:\n"))
        if option == 1:
            productos_vendidos.append(hacer_pedido(precio_productos))
        elif option==2:
            calcular_ingresos(precio_productos,productos_vendidos)


if __name__ == '__main__':
    main()