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