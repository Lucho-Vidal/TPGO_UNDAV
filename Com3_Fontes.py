def es_bisiesto (anio):
    """ Recibe por parámetro un número que representa un año. se considera bisiesto aquellos
    que sean divisibles por 4 y no divisible por 100 o divisible por 400 
    Devuelve un valor booleano que indica si el año es bisiesto o no lo es."""
    bisiesto = False
    if anio % 4 == 0:
        if (anio % 100 != 0) or (anio % 400 == 0):
            bisiesto = True
    return bisiesto

#Mes -> Día: 1 -> 31; 2 -> 28/29; 3 -> 31; 4 -> 30; 5 -> 31; 6 -> 30;
#            7 -> 31; 8 -> 31; 9 -> 30; 10 -> 31; 11 -> 30; 12 -> 31.

def cant_dias_mes (mes, anio):
    """ Recibe por parámetro 2 números que representen el mes y el año.
        Devuelve como resultado la cantidad de días de ése mes.
        Invoca a la función es_bisiesto (anio) """
    if (mes == 2):
        if (es_bisiesto(anio)== True):
            return (29)
        else:
            return (28)
    elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        return (30)
    else:
        return (31)
                
def valida_fecha (dia, mes, anio):
    """ Recibe por parámetro una fecha en números (Día, mes, año)
        Devuelve True si la fecha es válida y mayor o igual a 2022
        o False si no lo es.
        Invoca a la función cant_dias_mes (mes, anio) """
    if (mes > 0) and (mes <= 12) and (anio >= 2022):
        if dia > 0 and dia <= cant_dias_mes (mes, anio):
            return True
        else:
            return False
    else:
        return False
