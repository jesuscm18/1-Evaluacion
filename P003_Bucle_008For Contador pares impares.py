def contador_par_impar():
    n=input("Hasta que numero deseas contar? ")
    npares=0
    nimpares=0
    for n in range(1,n+1):
        if(n%2==0):
            print str(n)," es par"
            npares=npares+1
        else:
            print str(n)," es impar"
            nimpares=nimpares+1
    print "He contado ",npares, "numeros pares."
    print "He contado ",nimpares, " numeros impares."
contador_par_impar()
