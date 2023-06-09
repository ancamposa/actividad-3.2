rut = input("Ingresa tu RUT completo (Sin guiones ni puntos): ")
a = int(rut[7]) * 2
b = int(rut[6]) * 3
c = int(rut[5]) * 4
d = int(rut[4]) * 5
e = int(rut[3]) * 6
f = int(rut[2]) * 7
g = int(rut[1]) * 2
h = int(rut[0]) * 3

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

if int(rut[8]) == dv:
    print("El RUT ingresado es válido")
else:
    print("Este RUT es inválido")

print("El RUT ingresado es", rut[0] + rut[1], ".", rut[2] + rut[3] + rut[4], ".", rut[5] + rut[6] + rut[7], "-", rut[8])
