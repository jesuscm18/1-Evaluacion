def clasificador_numeros():
    n=input("Desde que numero quiere que clasifique? ")
    f=input("Hasta que numero desea que clasifique? ")
    for i in range(n,f+1):
        if (i%2==0):
            print str(i) + " es un numero par",
        else:
            print str(i) + " es un numero impar",
        if (i%3==0):
            print "y es divisible para 3"
        else:
            print "pero no divisible para 3"
        print "\n"
            
clasificador_numeros()
