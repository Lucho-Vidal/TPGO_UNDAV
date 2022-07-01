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
            cant_dias=29
        else:
            cant_dias=28
    return cant_dias