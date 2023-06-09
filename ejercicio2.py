def fibonacci(numero):
    numeroAnterior=0
    numeroActual=0
    pivote=0
    resultado=""
    for i in range(numero):
        if i==0 or i==1:
            numeroAnterior=1
            numeroActual=1
            pivote=1
            resultado=resultado+str(numeroActual)
        else:
            numeroActual=numeroAnterior+pivote
            numeroAnterior=pivote
            pivote=numeroActual
            resultado=resultado+str(numeroActual)
        if i<numero-1:
            resultado=resultado+"-"
    print(resultado)
    return

main=int(input("Ingrese número positvo y entero para la serie fibonacci: "))
fibonacci(main)
