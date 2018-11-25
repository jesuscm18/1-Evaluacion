def clasificador_numeros():
    i=input("Hasta que numero quieres que clasifique? ")
    for i in range(0,i+1):
        if (i%2==0):
                print str(i) + " es un numero par "
        else:
                print str(i) + " es un numero impar "
        if (i%3==0):
            print " y es divisible para 3"
        else:
            print " pero no divisible para 3"
            
clasificador_numeros()
