from Com_3_GAMMA_Vera import valida_cant

def pide_prod():
    """ Función dedicada a solicitar la cantidad de unidades
        requeridas de Yerba Mate 1kg, Té Negro 100grs, Té
        Verde 100grs, Miel tipo Mistol 500grs y Miel tipo
        Algarrobo 1kg, además de contabilizar cuántos tipos
        distintos de productos se solicitó. Exige el
        reingreso hasta que se solicite al menos una unidad
        de algún tipo de producto.
        Recibe por teclado un valor numérico, valida mediante
        valida_cant (minimo, maximo, texto) que el valor se
        encuentre entre minimo (Incluido) y maximo.
        Devuelve el valor para asignar a las variables:
        cant_tipo_prod, uni_soli_yerba, uni_soli_ten,
        uni_soli_tev, uni_soli_mielm, y uni_soli_miela. """
    cant_tipo_prod = 0
    while (cant_tipo_prod == 0):
        minimo = 0
        maximo = 11
        texto = 'De 0 a 10 ¿Cuántas unidades desea solicitar de '
        uni_soli_yerba = valida_cant(minimo, maximo, (texto + 'Yerba Mate 1kg? '))
        if uni_soli_yerba != 0:
            cant_tipo_prod = cant_tipo_prod + 1
        uni_soli_ten = valida_cant(minimo, maximo, (texto + 'Té Negro 100grs? '))
        if uni_soli_ten != 0:
            cant_tipo_prod = cant_tipo_prod + 1
        uni_soli_tev = valida_cant(minimo, maximo, (texto + 'Té Verde 100grs '))
        if uni_soli_tev != 0:
            cant_tipo_prod = cant_tipo_prod + 1
        uni_soli_mielm = valida_cant(minimo, maximo, (texto + 'Miel tipo Mistol 500grs? '))
        if uni_soli_mielm != 0:
            cant_tipo_prod = cant_tipo_prod + 1
        uni_soli_miela = valida_cant(minimo, maximo, (texto + 'Miel tipo Algarrobo 1kg? '))
        if uni_soli_miela != 0:
            cant_tipo_prod = cant_tipo_prod + 1
    return cant_tipo_prod, uni_soli_yerba, uni_soli_ten, uni_soli_tev, uni_soli_mielm, uni_soli_miela
