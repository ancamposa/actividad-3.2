def dv(rut):
    if len(rut)==9:

        a = int(rut[7]) * 2
        b = int(rut[6]) * 3
        c = int(rut[5]) * 4
        d = int(rut[4]) * 5
        e = int(rut[3]) * 6
        f = int(rut[2]) * 7
        g = int(rut[1]) * 2
        h = int(rut[0]) * 3

    elif len(rut)==8:
        a = int(rut[6]) * 2
        b = int(rut[5]) * 3
        c = int(rut[4]) * 4
        d = int(rut[3]) * 5
        e = int(rut[2]) * 6
        f = int(rut[1]) * 7
        g = int(rut[0]) * 2
        h = 0

    suma = a + b + c + d + e + f + g + h
    suma2 = suma // 11
    suma3 = suma2 * 11
    suma4 = (suma3 - suma) % 11

    if suma4 == 11:
        dv = 0
    elif suma4 == 10:
        dv = "K"
    else:
        dv = suma4

    if len(rut)==9:
        if int(rut[8]) == dv:
            print("El RUT ingresado es válido")
        else:
            print("Este RUT es inválido")
        print("El RUT ingresado es", rut[0] + rut[1], ".", rut[2] + rut[3] + rut[4], ".", rut[5] + rut[6] + rut[7], "-", rut[8])
    else:
        if int(rut[7]) == dv:
            print("El RUT ingresado es válido")
        else:
            print("Este RUT es inválido")
        print("El RUT ingresado es", rut[0], ".", rut[1] + rut[2] + rut[3], ".", rut[4] + rut[5] + rut[6], "-", rut[7])
    return


rut=0
while len(str(rut))<8 or len(str(rut))>9:
    rut = input("Ingresa tu RUT completo (Sin guiones ni puntos): ")
    if len(str(rut))<8 or len(str(rut))>9:
        print("RUT con largo inválido")
dv(rut)