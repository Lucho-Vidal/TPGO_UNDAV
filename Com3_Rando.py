def valida_cant(minimo, maximo, texto):
    """ Recibe por parámetro una cadena de caracteres, un
        valor mínimo y un valor máximo.
        Pide al usuario que ingrese por teclado un número
        mostrando la cadena de caracteres como texto.
        Devuelve un número natural válido entre los rangos
        especificados (Techo no incluido)."""
    numero = int (input (texto))
    while (numero not in range (minimo, maximo)):
        numero = int (input ('Valor inválido. Intente nuevamente: '))
    return numero