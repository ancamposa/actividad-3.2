import numpy as np

def numPrimo(numero):
    primo=np.array([2,3,5,7,11,13])
    if np.isin(numero,primo)==True:
        print(numero, "es primo")
    else:
        print(numero, "no es primo")
    return

def numFactorial(numero):
    fact=1
    for i in range(numero+1):
        if i>0:
            fact=fact*i
    print(fact)
    return

def palindrome(frase):
    frase = frase.translate({ord(' '): None})
    frase=frase.lower()

    palindrome1=np.array(list(frase))
    palindrome2=palindrome1[::-1]
    if np.array_equal(palindrome1,palindrome2)==True:
        print("Es palíndrome")
    else:
        print("No es palíndrome")
    return

menu=0
num=0
while menu<1 or menu>4:
    print("1. Número primo")
    print("2. Factorial")
    print("3. Palíndrome")
    print("4. Salir")
    menu=int(input("Seleccione opción: "))

    if menu==1:
        while num<1 or num>15:
            num=int(input("Ingrese un número entre 1 y 15: "))
            if num<1 or num>15:
                print("Debe ser entre 1 y 15")
        numPrimo(num)

    elif menu==2:
        while num<3 or num>10:
            num=int(input("Ingrese un número entre 3 y 10: "))
            if num<3 or num>10:
                print("Debe ser entre 3 y 10")
        numFactorial(num)

    elif menu==3:
        frase=input("Ingrese una frase: ")
        palindrome(frase)
        
    elif menu==4:
        print("Se cerró el programa \n Creadores: Antonio Campos & Alonso Cruz")

    else:
        print("Opción inválida")