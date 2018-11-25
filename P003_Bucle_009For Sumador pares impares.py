def sumador_par_impar():
    n=input("Hasta que numero deseas contar? ")
    sumapares=0
    sumaimpares=0
    for n in range(1,n+1):
        if(n%2==0):
            print str(n)," es par"
            sumapares=sumapares+n
        else:
            print str(n)," es impar"
            sumaimpares=sumaimpares+n
    print "La suma de los pares es: ", sumapares
    print "La suma de los impares es: ", sumaimpares
sumador_par_impar()
