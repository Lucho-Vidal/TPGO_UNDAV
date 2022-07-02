from Com_3_Carrillo import pide_prod
from Com_3_Fontes import valida_fecha
from Com_3_Maciel import valida_correo
from Com_3_Rando import valida_cant


def main():
    print("Bienvenidos a la Cooperativa de consumo Quinchahue")
    print("A continuación ingrese la fecha de entrega")
    dia = int(input("Por favor, ingrese el día\n"))
    mes = int(input("Por favor, ingrese el mes\n"))
    anio =int( input("Por favor, ingrese el año\n"))
    while not(valida_fecha(dia,mes,anio)):
        print("Hubo un error en la validación, Por favor ingrese una fecha de entrega valida")
        dia = int(input("Por favor, ingrese el dia\n"))
        mes = int(input("Por favor, ingrese el mes\n"))
        anio = int(input("Por favor, ingrese el año\n"))
    print("Fecha de entrega {}/{}/{}".format(dia,mes,anio))

    prec_uni_yerba = valida_cant(11,1000,"Ingrese el precio de Yerba Mate 1kg ")
    prec_uni_ten = valida_cant(11,1000,"Ingrese el precio de Té Negro 100grs ")
    prec_uni_tev = valida_cant(11,1000,"Ingrese el precio de Té Verde 100grs ")
    prec_uni_mielm = valida_cant(11,1000,"Ingrese el precio de Miel Mistol ½ kg ")
    prec_uni_miela = valida_cant(11,1000,"Ingrese el precio de Miel Algarrobo 1kg ")
    # inicializo los contadores en cero
    cant_total_vent=0
    cant_vent_cinco=0
    suma_monto_pedido=0
    total_yerba_vent=0
    total_ten_vent=0
    total_tev_vent=0
    total_mielm_vent=0
    total_miela_vent=0
    monto_max=0

    option = -1
    # Menu principal
    while option !=0:
        print("\nMenu principal\n1.Ingresar nuevo pedido\n2.Estadísticas de ventas\n0.Salir")
        option = int(input("Seleccioné una opción:\n"))
        if option == 1:
            dni = valida_cant(5000001,99000000,"Ingrese el DNI del Socio\n")
            correo = input("Ingrese el correo del Socio\n")
            while not valida_correo(correo):
                print("Ocurrió un error en la validación de correo, ingrese nuevamente!")
                correo = input("Ingrese el correo del Socio\n")
            #pide los productos           
            cant_tipo_prod,uni_soli_yerba,uni_soli_ten,uni_soli_tev,uni_soli_mielm,uni_soli_miela= pide_prod() 
            # sumo los importes de todos los productos
            monto_pedido = prec_uni_yerba*uni_soli_yerba+prec_uni_ten*uni_soli_ten+prec_uni_tev*uni_soli_tev+prec_uni_mielm*uni_soli_mielm+prec_uni_miela*uni_soli_miela
            cant_total_vent+=1
            if cant_tipo_prod == 5:
                cant_vent_cinco += 1
            suma_monto_pedido += monto_pedido
            total_yerba_vent += uni_soli_yerba
            total_ten_vent += uni_soli_ten
            total_tev_vent += uni_soli_tev
            total_mielm_vent += uni_soli_mielm
            total_miela_vent += uni_soli_miela
            if (monto_pedido > monto_max):
                monto_max = monto_pedido
            # Imprimo los resultados de el pedido
            print("El DNI del socio es:{}".format(dni))
            print("El Correo del socio es:{}".format(correo))
            print("La cantidad de unidades solicitadas de Yerba Mate 1kg:{}".format(uni_soli_yerba))
            print("La cantidad de unidades solicitadas de Té Negro 100grs:{}".format(uni_soli_ten))
            print("La cantidad de unidades solicitadas de Té Verde 100grs:{}".format(uni_soli_tev))
            print("La cantidad de unidades solicitadas de Miel Mistol ½ kg:{}".format(uni_soli_mielm))
            print("La cantidad de unidades solicitadas de Miel Algarrobo 1kg:{}".format(uni_soli_miela))
        elif option==2:
            print("Se registraron un total de {} ventas.".format(cant_total_vent))
            print("Por un importe de: ${}".format(suma_monto_pedido))
            if cant_total_vent != 0:
                print("El porcentaje de las ventas con los 5 tipos de productos es del {}%".format(cant_vent_cinco*100/cant_total_vent))
            print("Se solicitaron {} unidades de {}".format(total_yerba_vent,"Yerba Mate 1kg"))
            print("Se solicitaron {} unidades de {}".format(total_ten_vent,"Té Negro 100grs"))
            print("Se solicitaron {} unidades de {}".format(total_tev_vent,"Té Verde 100grs"))
            print("Se solicitaron {} unidades de {}".format(total_mielm_vent,"Miel Mistol ½ kg"))
            print("Se solicitaron {} unidades de {}".format(total_miela_vent,"Miel Algarrobo 1kg"))
            print("El mayor importe registrado fue de:{}".format(monto_max))
    
if __name__== '__main__':
    main()