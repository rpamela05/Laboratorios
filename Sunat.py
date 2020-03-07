def mes(x):
    if x==12:
        return x
    else:
        b=13-x
        return b

def impuesto():

    print("------------------------------------------")
    print("           Calculo del impuesto           ")
    print("------------------------------------------")
    print("")
    s=int(input("Ingrese remuneracion mensual: "))
    m=int(input("Ingrese mes de ingreso (1 - 12): "))
    g=int(input("Ingrese gratificaciones, remuneracion u otros ingresos: "))
    uit=4300
    prim=(5*uit)*0.08
    seg=(15*uit)*0.14
    ter=(15*uit)*0.17
    cuar=(10*uit)*0.2

    print("")
    print("------------------------------------------")
    print("                Resultados                ")
    print("------------------------------------------")

    f=mes(m)
    if 0<f<=12:
        rba=(s*f)+g
        print("")
        print("La remuneración bruta anual es: ",rba)
    else:
        print("Mes no exitente")


    if rba < 30100:
        print("No paga inpuesto")
    else:
        resta = rba - 30100

        if resta <= 21500:
            impuesto = resta * 0.08
            print("El impuesto anual proyectado es: ",impuesto)    
        elif 21500< resta <= 86000:
            impuesto = ((resta-(5*uit))*0.14)+prim
            print("El impuesto anual proyectado es: ",impuesto)  
        elif 86000<resta<=150500:
            impuesto = ((resta-86000)*0.17)+prim+seg
            print("El impuesto anual proyectado es: ",impuesto)    
        elif 150500<resta<=193500:
            impuesto = ((resta-150500)*0.20)+prim+seg+ter
            print("El impuesto anual proyectado es: ",impuesto)   
        else:
            impuesto = ((resta-193500)*0.3)+prim+seg+ter+cuar
            print("El impuesto anual proyectado es: ",impuesto)

        if 1<=m<=3:
                r_mes=impuesto/12
                print("La retencion del mes es: ",r_mes)
                print("")
        elif m==4:
                r_mes= impuesto/9
                print("La retencion del mes es: ",r_mes)
                print("")
        elif 5<=m<=7:
                r_mes=impuesto/8
                print("La retencion del mes es: ",r_mes)
                print("")
        elif m==8:
                r_mes=impuesto/5
                print("La retencion del mes es: ",r_mes)
                print("")
        elif 9<=m<=11:
                r_mes=impuesto/4
                print("La retencion del mes es: ",r_mes)
                print("")
        else:
                r_mes=impuesto/12
                print("La retencion del mes es: ",r_mes)
                print("")
impuesto()    

        
