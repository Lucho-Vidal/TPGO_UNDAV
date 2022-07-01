from Com_3_GAMMA_Rando import cant_dias_mes
def valida_fecha(dia,mes,anio):
    """ Recibe por parámetro una fecha en números (Día, mes y año), 
    Devuelve un valor booleano que indica si esa fecha es válida o no. 
    Invoca a la función cant_dias_mes (mes, anio). ademas la fecha no puede ser inferior a 2022"""
    es_valida = False
    if mes>=1 and mes<=12 and anio>=2022:
        dia_max = cant_dias_mes(mes,anio)
        if dia_max>0 and dia <= dia_max:
            es_valida = True
    return es_valida